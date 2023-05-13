from aiogram.types import Message
from aiogram.filters import Command

from misc import router
from utils.logger import logger


@router.message(Command(commands=["get_id"]))
async def command_get_id(message: Message) -> None:
    """
    This handler receive messages with `/get_id` command
    Handler will forward user telegram id
    """
    await message.answer(
        f"Your telegram id: <strong><code>{message.from_user.id}</code></strong>\n"
        f"Chat id: <strong><code>{message.chat.id}</code></strong>",
    )
