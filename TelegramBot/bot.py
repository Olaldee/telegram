#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import subprocess

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
# Telegram available methods
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def batuketa(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Hau da zure batura: " + str(int(context.args[0]) + int(context.args[1])))

def kenketa(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Hau da zure kenketa: " + str(int(context.args[0]) - int(context.args[1])))

def biderketa(update, context):
       """Send a message when the command /help is issued."""
       update.message.reply_text("Hau da zure biderketa: " + str(int(context.args[0]) * int(context.args[1])))

def zatiketa(update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text("Hau da zure zatiketa: " + str(int(context.args[0]) / int(context.args[1])))

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def fitxategia(update, context):
    print_file = context.bot.get_file(update.message.document.file_id).download()
    subprocess.run(["lpr","-P","MP-C3004",print_file])


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1723998779:AAH_AX00ScSgTWj-JzHxQkS28tnT6-oFWyg", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("batuketa", batuketa))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("kenketa", kenketa))
    dp.add_handler(CommandHandler("biderketa", biderketa))
    dp.add_handler(CommandHandler("zatiketa", zatiketa))
    dp.add_handler(MessageHandler(Filters.document,fitxategia))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
