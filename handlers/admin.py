from aiogram import Router, F, types
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, FSInputFile
from workwithDB.connectDB import aplicat_admin, apl_cor, id_client, id_ap, tg
from workwithDB.adminworkDBpy import prosmotr, mark, photo, description
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
        keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Просмотр заявки')], 
                                                       [types.KeyboardButton(text='Информация о клиенте')]],
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
    cur.execute(f"SELECT idnum, name, email, phone, tgname FROM users WHERE idnum = {id_client}")
    info = cur.fetchall() 
    con.close()
    if info != []:
        tt = 'Информация о клиенте:\n' + "ФИО: " + info[0][1] + '\nПочта: ' + info[0][2] + '\nТелефон: ' + info[0][3] 
        tt = tt + '\nСсылка на чат с клиентом: ' + '@' + info[0][4]
    else:
        tt = 'Информациии о клиенте нет'
    await message.answer(text=tt)
    

@router.message(F.text.lower()=='просмотр заявки')
async def seeapl(message: Message):
    info = prosmotr(id_ap)
    for key in info:
        des = description(key)
        tt = 'Требование к фото: ' + des
        await message.answer(text=tt)
        await message.answer(text='Ниже будут выведены фото по этому требованию')
        for j in info[key]:
            ph = photo(j[1])
            image_from_pc = FSInputFile(ph)
            await message.answer_photo(image_from_pc)
    await message.answer(text='По команде /status <новый статус> вы можете назначить статус заявке')
    tt = 'Варианты статусов:\n одобрена, отклонена, на корректировке'


@router.message(Command("status"))
async def cmd_name(message: Message, command: CommandObject):
    stats = ['одобрена', 'отклонена', 'на корректировке']
    if command.args:
        if command.args in stats:
            con = psycopg2.connect(
            database="SovDB", user="postgres", password="password", 
            host="127.0.0.1", port="5432")
            cur = con.cursor()
            cur.execute(f"UPDATE application set status = '{command.args}' where ida = {id_ap}")
            con.commit()
            con.close()
            await message.answer(text='При необходимости отправки акта об осмотре или по вопросу корректировки вы можете связаться с пользователем во вкладке меню <информация о клиенте>')
        else:
            await message.answer("Этого варианта статуса нет. Попробуйте еще раз.")
    else:
        await message.answer("Пожалуйста, укажи статус заявки после команды /status !")
    