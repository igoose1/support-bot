# support-bot
Telegram bot that helps to admins to communicate with subscribers.
It forwards messages from subscribers to admin's chat and sends answers to user from admins.

User's chat:

![Users' view](img/user_view.png)

Admins' chat:

![Admins' view](img/admin_view.png)

## Usage

### Configuration

Edit `config.ini` file before running the bot.

Necessary:
  * `token` is your telegram bot's token.
  * `support-chat-id` is id of chat with admin(-s). If you want to use it in private chat write id of your account.

All messages are editable, you can find them in config file too.

#### Proxy

You can use https proxy for bot.

Change `proxy` to `yes` and write your address in `proxy-server`.
```
proxy-server: https://server_address:port
```

#### Receiving types

You can filter user's files types.
Write in `forward-types` necessary types from telegram bot API.

### Running

```
pip install -r requirements.txt  # installs deps

python main.py
```

# Usage of bot

Every message from users **forwards** to admin's chat.

Admin answers by **replying to the message with a question**.

User can be blocked by **`/block`** in reply. Unblocking is possible as well
with **`/unblock`**.
