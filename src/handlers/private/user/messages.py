from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.utils.chat_action import ChatActionSender

from src.service.ai_client import get_completetions

router = Router()


@router.message(StateFilter(None))
async def on_message(message: types.Message, bot):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        text = await get_completetions(message.text)
        await message.answer(text)
