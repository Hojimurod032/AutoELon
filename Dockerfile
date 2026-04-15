FROM python:3.12-slim
WORKDIR /app

COPY req.text .
RUN pip install req.text

COPY . .

CMD ["python", "main.py"]