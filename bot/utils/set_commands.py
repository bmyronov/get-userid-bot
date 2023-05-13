from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(
            command="start", description="Press to start the conversation with the bot"
        ),
        BotCommand(command="get_id", description="Prints your telegram user id"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
