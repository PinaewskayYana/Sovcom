from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import texts
from keyboards.auto import builder, menu_admin
from hash_password import hashh, valid

class Aytent(StatesGroup):
    input_name = State()
    input_surname = State()
    input_surnameot = State()
    input_login = State()
    input_password = State()
    input_validpassword = State()

router = Router()  

@router.message(F.text.lower() == "войти")
async def ans_log(message: Message, state: FSMContext):
    users = ['1338974355']
    if str(message.from_user.id) in users:
        await message.answer('Введите логин',
                         reply_markup=ReplyKeyboardRemove()
                         )
        await state.set_state(Aytent.input_login)
    else:
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text='Зарегистрироваться')]],
            resize_keyboard=True,
        )
        await message.answer('Вы еще не зарегистрированы',
                         reply_markup=keyboard
                         )

@router.message(Aytent.input_login)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_login=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Введите пароль"
    )
    #mas['login']=user_data['input_login']
    await state.set_state(Aytent.input_password)
    
@router.message(Aytent.input_password)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_password=message.text.lower())
    user_data = await state.get_data()
    #mas['password']= hashh(user_data['input_password'])
    #pas = valid(user_data['input_password'], mas['password'])
    keyboard = builder #добавить развлетвление
    if pas == False:
        await message.answer(text="Пароль неверный. Повторите пожалуйста")
    else:
        await message.answer(text=texts.REFERENSE, reply_markup=keyboard.as_markup(resize_keyboard=True))
        await state.clear()