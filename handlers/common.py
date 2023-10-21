from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from texts import WELCOME_MES, SPRAVKA, PHOTO, ANDROID, IPHONE
from keyboards.auto import kb_autor, builder, phone

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_autor,
        resize_keyboard=True,
    )
    await message.answer(WELCOME_MES, reply_markup=keyboard)


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer(text=SPRAVKA)

@router.message(Command(commands=["menu"]))
async def cmd_menu(message: Message):
    await message.answer(text = 'Ваше меню',reply_markup=builder.as_markup(resize_keyboard=True))
    
@router.message(Command(commands=["photo"]))
async def cmd_photo(message: Message):
    await message.answer(text=PHOTO,
                         reply_markup=ReplyKeyboardRemove())
    
@router.message(Command(commands=["data"]))
async def cmd_data(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=phone,
        resize_keyboard=True,
    )
    await message.answer(text="В меню вы можете получить справку в зависимости от модели телефона", reply_markup=keyboard)

@router.message(F.text.lower() == "android")
async def cmd_phone(message: Message):
    await message.answer(text=ANDROID, reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower() == "iphone")
async def cmd_phone(message: Message):
    await message.answer(text=IPHONE, reply_markup=ReplyKeyboardRemove())