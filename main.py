import telebot
import configparser
import logging

config = configparser.ConfigParser()
config.read('config.ini')
parsed_types = config.get(
    'Tech',
    'forward-types'
    ).split(';')
logging.basicConfig(
    format=config.get(
        'Tech',
        'logger-format'
        )
    )
bot = telebot.TeleBot(
          config.get(
              'Tech',
              'token'
              )
          )


class Filters:
    def is_user(message):
        return message.chat.id != config.get(
            'Tech',
            'support-chat-id'
            ) and message.chat.type == 'private'

    def is_admin(message):
        return message.chat.id == config.getint(
            'Tech',
            'support-chat-id'
            )

    def is_answer(message):
        return message.chat.id == config.getint(
            'Tech',
            'support-chat-id'
            ) and\
            message.reply_to_message is not None


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(
        message.chat.id,
        config.get(
            'Messages',
            'start'
            )
        )


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id,
        config.get(
            'Messages',
            'help'
            )
        )


@bot.message_handler(content_types=parsed_types, func=Filters.is_user)
def get_question(message):
    if config.getboolean(
        'Tech',
        'success-question-message'
       ):
        bot.send_message(
            message.chat.id,
            config.get(
                'Messages',
                'question-was-sent'
                )
            )
    bot.forward_message(
        config.get(
            'Tech',
            'support-chat-id'
            ),
        message.chat.id,
        message.message_id
        )


@bot.message_handler(func=Filters.is_user)
def get_error_question(message):
    bot.send_message(
        message.chat.id,
        config.get(
            'Messages',
            'question-wasnt-sent'
            )
        )


@bot.message_handler(content_types=['text', 'photo'], func=Filters.is_answer)
def answer_question(message):
    if message.photo is not None:
        bot.send_photo(
            message.reply_to_message.forward_from.id,
            message.photo[-1].file_id,
            message.caption,
            )
    else:
        bot.send_message(
            message.reply_to_message.forward_from.id,
            config.get(
                'Messages',
                'get-answer'
                ).format(
                message=message.text
                )
            )
    if config.getboolean(
        'Tech',
        'success-answer-message'
       ):
        bot.send_message(
            message.chat.id,
            config.get(
                'Messages',
                'answer-was-sent'
                ),
            reply_to_message_id=message.message_id
            )


def main():
    bot.infinity_polling(none_stop=True, timeout=60)


if __name__ == '__main__':
    main()
