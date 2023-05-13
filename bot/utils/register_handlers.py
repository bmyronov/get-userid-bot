from aiogram import Router

from handlers import command_get_id, command_start


async def register_handlers(router: Router) -> None:
    router.message.register(command_start)
    router.message.register(command_get_id)
