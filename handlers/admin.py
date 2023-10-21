from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()

@router.massage(Command(commands=["see"]))
@router.message(F.text.lower() == "начать просмотр заявок")
async def cmd_see(message: Message):
    await message.answer(text="You see")
