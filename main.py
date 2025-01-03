#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

from typing import cast
from telegram import User
async def new_start(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """This is my fun without trying any error msg"""
    user = cast(User, user)
    user = update.message.from_user

    text = "Hello Sir YOu have send me /start in ur message = /help"
    await context.bot.send_message(user.id, text.upper())


# This belwo fun will trigger on each message come to bot not for any other update
async def new_start(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """i remove those error sugession by this"""
    
    if update.message:
        user = update.message.from_user
    else:
        user = None

    if user:
        text = f"Hello {user.full_name} this is a Example Bot"
        await context.bot.send_message(user.id, text)




# This belwo fun will trigger on each message come to bot not for any other update
async def new_start(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """i remove those error sugession by this"""
    
    if not update.message:
        return None
    user = update.message.from_user
    text = f"Hello thanks"
    if user:
        await context.bot.send_message(user.id, text.upper())
    else:
        pass



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("TOKEN").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()