import random, os
import string


from aiogram import Bot, Router, F, BaseMiddleware
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, KeyboardButton, InlineKeyboardButton, )
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


from BOT.utils.coze_bot import LLM

router = Router()




@router.message(Command(commands=["start"]))
async def get_start(message: Message, bot: Bot, state: FSMContext):

    await message.answer(text='Привет, <b>Solstice</b>! Напиши мне что-нибудь и я помогу.')

    await state.clear()


@router.message(F.text)
async def get_all_text_msgs(message: Message, bot: Bot):
    USER_ID: int = message.from_user.id

    TEXT = message.text

    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Да", callback_data="to_bot"))

    ANSWER = LLM.get_chat(QUERY=TEXT)

    await bot.send_message(
        chat_id=USER_ID,
        text=str(ANSWER)
    )


