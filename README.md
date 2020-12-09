# support-bot
Telegram bot that helps to admins to communicate with subscribers.
It forwards messages from subscribers to admin's chat and sends answers to user from admins.

Users' chat:

![Users' view](img/user_view.png)

Admins' chat:

![Admins' view](img/admin_view.png)

## Usage

### Configuration

Edit `config.ini` file to run the bot.

Necessary:
  * `token` is your telegram bot's token.
  * `support-chat-id` is id of chat with admin(-s). If you want to use it alone write id of your account.

All messages are editable.
You can find them in config file too.

#### Proxy

You can use https proxy for bot.

Change `proxy` to `yes` and write your address in `proxy-server`.
```
proxy-server: https://server_address:port
```

#### Receiving types

You can filter user's files types.
Write in `forward-types` variable all necessary types from telegram bot api.

### Running

```bash
pip install -r requirements.txt  # install packages
python main.py
```
Be sure that you are using python3.

# Usage of bot

Every messages from users **forward** to admin's chat.

To answer admin has to **answer by replying question message**.

To block user send **`/block` by replying** user's message you want to block.
To unblock use **`/unblock`**.
