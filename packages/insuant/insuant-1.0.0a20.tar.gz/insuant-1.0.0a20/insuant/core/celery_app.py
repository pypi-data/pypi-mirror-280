from celery import Celery  # type: ignore


def make_celery(app_name: str, config: str) -> Celery:
    celery_app = Celery(app_name)
    celery_app.config_from_object(config)
    celery_app.conf.task_routes = {"insuant.worker.tasks.*": {"queue": "insuant"}}
    return celery_app


celery_app = make_celery("insaunt", "insuant.core.celeryconfig")
