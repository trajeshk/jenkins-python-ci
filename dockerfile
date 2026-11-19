FROM python:3.13-slim

WORKDIR /app

COPY app.py .
COPY test_app.py .

RUN python -m unittest -v 

CMD ["python", "app.py"]
