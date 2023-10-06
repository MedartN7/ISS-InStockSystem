FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn pydantic

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
