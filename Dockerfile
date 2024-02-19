FROM tiangolo/uvicorn-gunicorn:python3.8-slim
#FROM mysql:latest

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV PORT=8000
CMD gunicorn main:app --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker


