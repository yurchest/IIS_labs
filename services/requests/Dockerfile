FROM python:3.12-slim

COPY . /app
WORKDIR /app

RUN pip install requests

CMD ["python3", "req.py"]

# docker build . --tag request_service:1
# docker run request_service:1