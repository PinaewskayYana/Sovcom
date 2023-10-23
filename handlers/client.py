from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from keyboards.auto import kb_cat
import psycopg2

router = Router()

@router.message(F.text.lower() == "создать новую заявку")
async def new_app(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_cat,
        resize_keyboard=True,
    )
    await message.answer(text="Какой объект вы хотите осмотреть?", reply_markup=keyboard)
    
@router.message(F.text.lower() == 'посмотреть текущие заявки')
async def see_apl(message: Message):
    con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
    f"""SELECT ida, cath, usid, text, status from application WHERE usid = {message.from_user.id} AND
        (status = 'на рассмотрении' OR status = 'на корректировке' OR status = 'отправлена')"""
        )
    idd = cur.fetchall()   
    con.close()
    if idd == []:
        await message.answer(text='Текущих заявок на данный момент нет')
    else:
        tt = 'Ваши заявки\n'
        for apl in idd:
            st = 'Номер заявки: ' + str(apl[0]) + '\nКатегория: ' + apl[1] + '\nОписание объекта: ' + apl[3] + '\nСтатус: ' + apl[4]
            tt = tt + st + '\n'
        await message.answer(text=tt)
        await message.answer(text = 'По команде /applicat <номер, интересующей вас заявки>, вы сможете посмотреть заявку подробнее с фото')

@router.message(F.text.lower() == 'история заявок') 
async def history(message: Message):
    con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
    f"""SELECT ida, cath, usid, text, status from application WHERE usid = {message.from_user.id} AND
        (status = 'отклонена' OR status = 'одобрена')"""
        )
    idd = cur.fetchall()   
    con.close()
    if idd == []:
        await message.answer(text='В истории заявок на данный момент ничего нет')
    else:
        tt = 'Ваши заявки\n'
        for apl in idd:
            st = 'Номер заявки: ' + str(apl[0]) + '\nКатегория: ' + apl[1] + '\nОписание объекта: ' + apl[3] + '\nСтатус: ' + apl[4]
            tt = tt + st + '\n'
        await message.answer(text=tt)

@router.message(F.text.lower() == 'тех.поддержка')
async def support(message: Message):
    await message.answer(text='Тех.поддержка пока не активна.\n Скоро появится ссылка на нее или контакты поддержки')