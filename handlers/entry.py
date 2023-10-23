from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import texts
from keyboards.auto import builder, menu_admin
from hash_password import hashh, valid
import psycopg2
role = ''

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
    await message.answer('Введите логин',
                         reply_markup=ReplyKeyboardRemove()
                         )
    await state.set_state(Aytent.input_login)

@router.message(Aytent.input_login)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_login=message.text.lower())
    con = psycopg2.connect(
    database="SovDB", 
    user="postgres", 
    password="password", 
    host="127.0.0.1", 
    port="5432"
    )
    user_data = await state.get_data()
    cur = con.cursor()
    cur.execute(
    f"""SELECT login from users WHERE login = '{user_data['input_login']}'"""
        )
    dat = cur.fetchall()
    con.close()
    if dat != []:
        await message.answer(
            text="Введите пароль"
        )
        await state.set_state(Aytent.input_password)
    else:
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text='Зарегистрироваться')]],
            resize_keyboard=True,
        )
        await message.answer('Вы еще не зарегистрированы. Либо ваш логин не верен.',
                         reply_markup=keyboard
                         )
        await state.clear()
    
@router.message(Aytent.input_password)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_password=message.text.lower())
    user_data = await state.get_data()
    con = psycopg2.connect(
    database="SovDB", 
    user="postgres", 
    password="password", 
    host="127.0.0.1", 
    port="5432"
    )
    cur = con.cursor()
    cur.execute(
    f"""SELECT login, role, pass from users WHERE login = '{user_data['input_login']}'"""
        )
    dat = cur.fetchall()
    con.close()
    pas = valid(user_data['input_password'], dat[0][2])
    if pas == False:
        await message.answer(text="Пароль неверный. Повторите пожалуйста")
    else:
        if dat[0][1] == 'client': 
            keyboard = builder 
            await message.answer(text=texts.REFERENSE, reply_markup=keyboard.as_markup(resize_keyboard=True))
        if dat[0][1] == 'admin':
            keyboard = menu_admin
            await message.answer(text=texts.ADMIN, reply_markup=keyboard.as_markup(resize_keyboard=True))
        
        await state.clear()