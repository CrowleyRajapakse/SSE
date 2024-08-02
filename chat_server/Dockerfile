FROM python:3.9-slim

WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY chat_server.py chat_server.py

CMD ["python", "chat_server.py"]
