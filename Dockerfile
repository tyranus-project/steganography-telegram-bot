FROM python:3.8-slim-buster

WORKDIR /steganography-telegram-bot

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY bot /steganography-telegram-bot/bot

CMD ["python", "-m", "bot"]
