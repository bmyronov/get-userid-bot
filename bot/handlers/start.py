from aiogram.types import Message
from aiogram.filters import CommandStart

from misc import router


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    await message.answer(
        "Hello, this bot shows your telegram id.\n"
        "To get your telegram id write /get_id"
    )
