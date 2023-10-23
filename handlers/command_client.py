from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboards.auto import kb_cat
import psycopg2

from aiogram.filters import CommandObject

router= Router()

@router.message(Command("applicat"))
async def cmd_name(message: Message, command: CommandObject):
    if command.args:
        await message.answer("Эта ветка с подробной выдачей еще не оформлена")
    else:
        await message.answer("Пожалуйста, укажи номер заявки после команды /applicat!")
