# support-bot
Telegram bot that helps to admins to communicate with subscribers.
It forwards messages from subscribers to admin's chat and sends answers to user from admins.

## Usage

### Configurating

Edit `config.ini` file to run the bot.

Neccessary:
  * `token` is your telegram bot's token.
  * `support-chat-id` is id of chat with admin(-s).

All messages are editable.
You can find them in config file too.

### Run

There are many ways to run the bot.

It's running in docker and installing packages using pipenv or pip.

#### Docker

```bash
docker build -t support-bot .  # build
docker run --rm support-bot  # run
```
Dockerfile is existing in project folder.

#### Pipenv

```bash
pipenv install -r requirements.txt  # install packages
pipenv run python main.py  # run
```

#### Standart

```bash
pip install -r requirements.txt  # install packages
python main.py
```
Be sure that you are using python3
