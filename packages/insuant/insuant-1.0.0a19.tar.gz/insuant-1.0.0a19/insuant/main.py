from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional
from urllib.parse import urlencode

import nest_asyncio  # type: ignore
import socketio  # type: ignore
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger
from rich import print as rprint

from insuant.api import router
from insuant.initial_setup.setup import create_or_update_starter_projects
from insuant.interface.utils import setup_llm_caching
from insuant.services.plugins.langfuse_plugin import LangfuseInstance
from insuant.services.utils import initialize_services, teardown_services
from insuant.utils.logger import configure


def get_lifespan(fix_migration=False, socketio_server=None):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        nest_asyncio.apply()
        initialize_services(fix_migration=fix_migration, socketio_server=socketio_server)
        setup_llm_caching()
        LangfuseInstance.update()
        create_or_update_starter_projects()
        yield
        # Shutdown message
        rprint("[bold red]Shutting down insuant...[/bold red]")
        teardown_services()

    return lifespan


def create_app():
    """Create the FastAPI app and include the router."""

    configure()
    socketio_server = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*", logger=True)
    lifespan = get_lifespan(socketio_server=socketio_server)
    app = FastAPI(lifespan=lifespan)
    origins = ["*", "http://localhost:3000"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def flatten_query_string_lists(request: Request, call_next):
        flattened: list[tuple[str, str]] = []
        for key, value in request.query_params.multi_items():
            flattened.extend((key, entry) for entry in value.split(","))

        request.scope["query_string"] = urlencode(flattened, doseq=True).encode("utf-8")

        return await call_next(request)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(router)

    app = mount_socketio(app, socketio_server)

    return app


def mount_socketio(app: FastAPI, socketio_server: socketio.AsyncServer):
    app.mount("/sio", socketio.ASGIApp(socketio_server, socketio_path=""))
    return app


def setup_static_files(app: FastAPI, static_files_dir: Path):
    """
    Setup the static files directory.
    Args:
        app (FastAPI): FastAPI app.
        path (str): Path to the static files directory.
    """
    app.mount(
        "/",
        StaticFiles(directory=static_files_dir, html=True),
        name="static",
    )

    @app.exception_handler(404)
    async def custom_404_handler(request, __):
        path = static_files_dir / "index.html"

        if not path.exists():
            raise RuntimeError(f"File at path {path} does not exist.")
        return FileResponse(path)


def get_static_files_dir():
    """Get the static files directory relative to Langflow's main.py file."""
    frontend_path = Path(__file__).parent
    return frontend_path / "frontend"


def setup_app(static_files_dir: Optional[Path] = None, backend_only: bool = False) -> FastAPI:
    """Setup the FastAPI app."""
    # get the directory of the current file
    logger.info(f"Setting up app with static files directory {static_files_dir}")
    if not static_files_dir:
        static_files_dir = get_static_files_dir()

    if not backend_only and (not static_files_dir or not static_files_dir.exists()):
        raise RuntimeError(f"Static files directory {static_files_dir} does not exist.")
    app = create_app()
    if not backend_only and static_files_dir is not None:
        setup_static_files(app, static_files_dir)
    return app


if __name__ == "__main__":
    import uvicorn

    from insuant.__main__ import get_number_of_workers

    configure()
    uvicorn.run(
        "insuant.main:create_app",
        host="127.0.0.1",
        port=7860,
        workers=get_number_of_workers(),
        log_level="error",
        reload=True,
        loop="asyncio",
    )
