# Telegram Bot for Image Crypto-Steganography

<b>Steganography</b> is the art and science of invisible communication. 
It is achieved by hiding the message information in some other carrier media.

<b>Image steganography</b> is a subset of steganography where messages are hidden in image files. 
The original image, before any message is hidden in it, is referred to as the <b>cover image</b>. 
After hiding the message in it, it is referred to as the <b>stego image</b>. 
For human eye, these two images must be identical (in appearance at least).

This bot provides <b>image steganography tools to hide secret text messages</b>, both for encryption and decryption.
Additionally, this implementation also enhance the security of the steganography through data encryption by using AES 256.

## Installation and Launch

### Using Docker

1. Clone the repository:

```
git clone https://github.com/tyranus-project/steganography-telegram-bot
cd steganography-telegram-bot
```

2. Rename environment file from example:

```
mv .env.dist .env
```

3. Personalize configuration by modifying ```.env```:

- Create a new Telegram bot by talking to [@BotFather](https://t.me/BotFather) and get its API token;

- Set `BOT_TOKEN` to the value obtained using the step described above.

4. Install [Docker Compose](https://docs.docker.com/compose/install/).

5. Build and run your container:

```
docker-compose up --build
```

### Manual

1. Clone the repository:

```
git clone https://github.com/tyranus-project/steganography-telegram-bot
cd steganography-telegram-bot
```

2. Install Python with [pip](https://pip.pypa.io/en/stable/installing/).

3. Install requirements:

```
pip install -r requirements.txt
```

4. Rename environment file from example:

```
mv .env.dist .env
```

5. Personalize configuration by modifying ```.env```:

- Create a new Telegram bot by talking to [@BotFather](https://t.me/BotFather) and get its API token;

- Set `BOT_TOKEN` to the value obtained using the step described above.

6. Launch bot:

```
python -m bot
```

## License

This project is released under the MIT License. See [LICENSE](https://github.com/neuromeow/ssh-telegram-bot/blob/master/LICENSE) for the full licensing condition.
