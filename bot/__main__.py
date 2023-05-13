import asyncio

from misc import dp, bot, router
from utils.logger import logger
from utils.register_handlers import register_handlers
from utils.set_commands import set_commands


async def main() -> None:
    # Sets commands in menu button
    await set_commands(bot)
    # Registeres all handlers instead of import without use
    await register_handlers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger()
    asyncio.run(main())
