FROM python:3.10
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app
CMD ["uvicorn", "insuant.main:app", "--host", "127.0.0.1", "--port", "8000"]