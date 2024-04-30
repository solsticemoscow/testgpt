from typing import NoReturn
from aiogram.types import BotCommandScopeDefault, BotCommand, FSInputFile
import asyncio


from BOT.config import TOKEN_SERVICE
from aiogram import Bot, Dispatcher

from BOT.handlers.router_first import router as router_first

BOT = Bot(token=TOKEN_SERVICE, parse_mode="HTML")
DP = Dispatcher()
DP.include_router(router_first)



async def main() -> NoReturn:
    print('Bot start!')

    await BOT.delete_webhook()

    await BOT.set_my_commands([
        BotCommand(command='start', description='✅ Начальное меню, сброс диалога'),
        BotCommand(command='test', description='Тест')
    ],
        scope=BotCommandScopeDefault()
    )

    await DP.start_polling(BOT)


if __name__ == "__main__":
    asyncio.run(main())


