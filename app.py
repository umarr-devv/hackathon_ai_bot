import asyncio
import sys

import openai
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import load_config
from src.functions import set_commands
from src.handlers import router
from src.service.database import create_db_session
from src.service.logging import set_logging


async def main():
    config = load_config(config_file=sys.argv[1])
    set_logging(config=config)

    openai.api_key = config.open_ai.key

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=config.bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    db = await create_db_session(config)

    dp.include_router(router)
    await set_commands(bot)

    try:
        await dp.start_polling(bot, config=config, db=db)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
