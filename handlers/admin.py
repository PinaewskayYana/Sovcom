from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from workwithDB.connectDB import aplicat_admin, apl_cor, id_client, id_ap
from workwithDB.adminworkDBpy import prosmotr
from keyboards.auto import kb_apl
import psycopg2

router = Router()

@router.message(Command(commands=["see"]))
@router.message(F.text.lower() == "заявки, ожидающие рассмотрения")
async def cmd_see(message: Message):
    if aplicat_admin != []:
        now_apl = aplicat_admin[0]
        global id_ap
        id_ap = now_apl[0]
        con = psycopg2.connect(
        database="SovDB", user="postgres", password="password", 
        host="127.0.0.1", port="5432")
        cur = con.cursor()
        cur.execute(f"UPDATE application set status = 'на рассмотрении' where ida = {id_ap}")
        con.commit()
        con.close()
        tt = "Вы смотрите информацию по заявке\nНомер заявки" + str(id_ap) + '\nКатегория:' + now_apl[1]
        tt = tt + '\nОписание объекта недвижимости: ' + now_apl[3]
        global id_client
        id_client = now_apl[2]
        keyboard = ReplyKeyboardMarkup(keyboard=kb_apl,resize_keyboard=True,)
        await message.answer(text=tt, reply_markup=keyboard)
    else:
        await message.answer(text='Заявок, ожидающих рассмотрения нет')

@router.message(F.text.lower() == "заявки на корректировке")
async def cmd_see(message: Message):
    if apl_cor != []:
        now_apl = apl_cor[0]
        global id_ap
        id_ap = now_apl[0]
        global id_client
        id_client = now_apl[2]
        tt = "Вы смотрите информацию по заявке\nНомер заявки" + str(id_ap) + '\nКатегория:' + now_apl[1]
        tt = tt + '\nОписание объекта недвижимости: ' + now_apl[3]
        keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Связаться с клиентом')], 
                                                       [types.KeyboardButton(text='Изменить статус заявки')]],
                                                        resize_keyboard=True)
        await message.answer(text=tt, reply_markup=keyboard)
    else:
        await message.answer(text='Заявок, на корректировке нет')

@router.message(F.text.lower()=='информация о клиенте')
async def info(message: Message):
    con = psycopg2.connect(
    database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(f"SELECT idnum, name, email, phone FROM users WHERE idnum = {id_client}")
    info = cur.fetchall() 
    con.close()
    if info != []:
        tt = 'Информация о клиенте:\n' + "ФИО: " + info[0][1] + '\nПочта: ' + info[0][2] + '\nТелефон: ' + info[0][3]
    else:
        tt = 'Информациии о клиенте нет'
    await message.answer(text=tt)
    

@router.message(F.text.lower()=='просмотр заявки')
async def seeapl(message: Message):
    info = prosmotr(id_ap)