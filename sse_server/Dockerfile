FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY sse_server.py sse_server.py

CMD ["python", "sse_server.py"]

