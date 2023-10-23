from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards.auto import builder
import texts
from hash_password import hashh, valid
from workwithDB.connectDB import user
import psycopg2

class InputInfom(StatesGroup):
    input_name = State()
    input_surname = State()
    input_surnameot = State()
    input_email = State()
    input_phone = State()
    input_login = State()
    input_password = State()
    input_validpassword = State()

router = Router()  
@router.message(F.text.lower() == "зарегистрироваться")
async def cmd_regis(message: Message, state: FSMContext):
    con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
    f"""SELECT idnum from users WHERE idnum = {message.from_user.id}"""
        )
    idd = cur.fetchall()   
    con.close()
    if idd != []:
        kb = types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text='Войти')]],
            resize_keyboard=True,
        )
        await message.answer(text='Вы уже зарегистрированы', reply_markup=kb)
        await state.clear()
    else:
        await message.answer(
            text="Введите вашу фамилию",
            reply_markup=ReplyKeyboardRemove()
        )
        user['idNum'] = message.from_user.id
        await state.set_state(InputInfom.input_surname)

@router.message(InputInfom.input_surname)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_surname=message.text)
    user_data = await state.get_data()
    await message.answer(
        text="Введите ваше имя"
    )
    user['Name'] = user_data['input_surname']
    await state.set_state(InputInfom.input_name)

@router.message(InputInfom.input_name)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_name=message.text)
    user_data = await state.get_data()
    await message.answer(
        text="Введите ваше отчество"
    )
    user['Name']=user['Name'] + ' ' + user_data['input_name']
    await state.set_state(InputInfom.input_surnameot)

@router.message(InputInfom.input_surnameot)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_surnameot=message.text)
    user_data = await state.get_data()
    
    await message.answer(text="Введите вашу почту")
    user['Name']=user['Name'] + ' ' + user_data['input_surnameot']
    await state.set_state(InputInfom.input_email)

@router.message(InputInfom.input_email)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    user_data = await state.get_data()
    await message.answer(text="Введите номер телефона")
    user['email']=user_data['email']
    await state.set_state(InputInfom.input_phone)

@router.message(InputInfom.input_phone)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()
    await message.answer(text="Введите логин")
    user['phone']=user_data['phone']
    await state.set_state(InputInfom.input_login)
    
@router.message(InputInfom.input_login)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_login=message.text)
    user_data = await state.get_data()
    await message.answer(
        text="Придумайте пароль"
    )
    user['login'] = str(user_data['input_login'])
    await state.set_state(InputInfom.input_password)

@router.message(InputInfom.input_password)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_password=message.text)
    user_data = await state.get_data()
    await message.answer(
        text="Повторите пароль"
    ) 
    user['Pass'] = hashh(user_data['input_password'])
    await state.set_state(InputInfom.input_validpassword)

@router.message(InputInfom.input_validpassword)
async def inputdatee(message: Message, state: FSMContext):
    await state.update_data(input_validpassword=message.text)
    user_data = await state.get_data()
    pas = valid(user_data['input_validpassword'], user['Pass'])
    if pas == False:
        await message.answer(text="Пароль неверный. Повторите пожалуйста")
    else:
        conn = psycopg2.connect(
        database="SovDB", 
        user="postgres", 
        password="password", 
        host="127.0.0.1", 
        port="5432"
        )
        cur = conn.cursor()
        cur.execute(
        f"""INSERT INTO users (idnum,role,login,name,pass,email,phone) 
            VALUES ({user['idNum']}, 'client', '{user['login']}', '{user['Name']}', '{user['Pass']}', '{user['email']}', '{user['phone']}')"""
        )
        conn.commit()   
        conn.close()
        await message.answer(text=texts.REFERENSE, reply_markup=builder.as_markup(resize_keyboard=True))
        await state.clear()

                