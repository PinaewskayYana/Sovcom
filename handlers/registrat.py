from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards.auto import builder
import texts
from hash_password import hashh, valid
from workwithDB.connectDB import user

DB_url = "postgresql+psycopg2://postgres:password@localhost:5432/SovDB" 

class InputInfom(StatesGroup):
    input_name = State()
    input_surname = State()
    input_surnameot = State()
    input_login = State()
    input_password = State()
    input_validpassword = State()

router = Router()  
@router.message(F.text.lower() == "зарегистрироваться")
async def cmd_regis(message: Message, state: FSMContext):
    await message.answer(
        text="Введите вашу фамилию",
        reply_markup=ReplyKeyboardRemove()
    )
    user['idNum'] = message.from_user.id
    await state.set_state(InputInfom.input_surname)

@router.message(InputInfom.input_surname)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_surname=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Введите ваше имя"
    )
    user['Name'] = user_data['input_surname']
    await state.set_state(InputInfom.input_name)

@router.message(InputInfom.input_name)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_name=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Введите ваше отчество"
    )
    user['Name']=user['Name'] + ' ' + user_data['input_name']
    await state.set_state(InputInfom.input_surnameot)

@router.message(InputInfom.input_surnameot)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_surnameot=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Введите логин. \n Номер телефона или почту"
    )
    user['Name']=user['Name'] + ' ' + user_data['input_surnameot']
    await state.set_state(InputInfom.input_login)

@router.message(InputInfom.input_login)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_login=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Придумайте пароль"
    )
    user['login'] = user_data['input_login']
    await state.set_state(InputInfom.input_password)

@router.message(InputInfom.input_password)
async def inputdate(message: Message, state: FSMContext):
    await state.update_data(input_password=message.text.lower())
    user_data = await state.get_data()
    await message.answer(
        text="Повторите пароль"
    ) 
    user['Pass'] = hashh(user_data['input_password'])
    await state.set_state(InputInfom.input_validpassword)

@router.message(InputInfom.input_validpassword)
async def inputdatee(message: Message, state: FSMContext):
    await state.update_data(input_validpassword=message.text.lower())
    user_data = await state.get_data()
    pas = valid(user_data['input_validpassword'], user['Pass'])
    if pas == False:
        await message.answer(text="Пароль неверный. Повторите пожалуйста")
    else:
        await message.answer(text=texts.REFERENSE, reply_markup=builder.as_markup(resize_keyboard=True))
        await state.clear()
        user = Users(idNum= user['idNum'],Role="client",login=user['login'],Name=user['Name'],
                   Pass=user['Pass'],Email="zasada1926@gmail.com",phone="8912786341")
        