FROM python:3.12-slim

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

WORKDIR /run

CMD ["python", "/app/main.py"]