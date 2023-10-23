from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from workwithDB.connectDB import appl_num, req_tc, next_state, id_req, req_text, req_ne, flag_plan
from random import randrange
from keyboards.auto import builder
from handlers.workphoto import prov_photo
import texts
import psycopg2


router = Router()
class InputPhot(StatesGroup):
    texxt, textH = State(), State()
    photo = State()
    req1, req2, req3, req4 = State(), State(), State(), State()
    req5, req6, req7, req8 = State(), State(), State(), State()
    req9, req10, req11,req12 = State(), State(), State(), State()
    req13, req14, req15, req16 = State(), State(), State(), State()
    req17, req18, req19, req20 = State(), State(), State(), State()
    req21, req22 = State(), State()
    plan = State()

@router.message(F.text.lower() == "транспортное средство")
async def cmd_regis(message: Message):
    global appl_num
    appl_num = randrange(10000000)
    con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
     f"""INSERT INTO application (ida,cath,usid, status) 
            VALUES ({appl_num}, 'транспортное средство', '{message.from_user.id}', 'заполняется')""")
    con.commit()   
    con.close()
    await message.answer(text=texts.SEECAR, reply_markup=ReplyKeyboardRemove())
 

@router.message(F.text.lower() == "загородный дом")
async def cmd_regis(message: Message):
    global appl_num
    appl_num = randrange(10000000)
    con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
     f"""INSERT INTO application (ida,cath,usid, status) 
            VALUES ({appl_num}, 'недвижимость', '{message.from_user.id}', 'заполняется')""")
    con.commit()   
    con.close()
    await message.answer(text=texts.SEEHOUSE, reply_markup=ReplyKeyboardRemove())

    
@router.message(Command(commands=["textTC"]))
async def cmd_text(message: Message, state: FSMContext):
    await message.answer(text='Вы можете начать отправку текстового описания ТС')
    await state.set_state(InputPhot.texxt)
    
@router.message(Command(commands=["textH"]))
async def cmd_text(message: Message, state: FSMContext):
    await message.answer(text='Вы можете начать отправку текстового описания дома')
    await state.set_state(InputPhot.textH)

@router.message(Command(commands=["osmotrTC"]))
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = "После загрузки фото дождитесь сообщения <Фото принято на проверку>\n"
    tt = tt + "Вам нужно отправить " + req_tc[0][2] + '\n'
    tt = tt + 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[1][2]
    global next_state
    next_state = InputPhot.req1
    global id_req
    id_req = req_tc[0][0] 
    await state.set_state(InputPhot.photo)

@router.message(Command(commands=["osmotrH"]))
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = "После загрузки фото дождитесь сообщения <Фото принято на проверку>\n"
    tt = tt + "Вам нужно отправить " + req_ne[0][2] + '\n'
    tt = tt + 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[1][2]
    global next_state
    next_state = InputPhot.req10
    global id_req
    id_req = req_ne[0][0] 
    await state.set_state(InputPhot.photo)
    
@router.message(Command(commands=["plan"]))
async def plann(message: Message, state: FSMContext):
    await message.answer(text=texts.PLAN)
    tt = "Вы можете прикрепить план. После загрузки заявка будет отправлена на рассмотрение."
    await message.answer(text=tt)
    global flag_plan
    flag_plan = 1

@router.message(Command(commands=["example"]))
async def plann(message: Message, state: FSMContext):
    await message.answer(text="Пример схемы:")
    image_from_pc = FSInputFile("photoes/plan.jpg")
    await message.answer_photo(image_from_pc)
    
@router.message(InputPhot.req1)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[2][2]
    global next_state
    next_state = InputPhot.req2
    global id_req
    id_req = req_tc[1][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req2)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[3][2]
    global next_state
    next_state = InputPhot.req3
    global id_req
    id_req = req_tc[2][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req3)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[4][2]
    global next_state
    next_state = InputPhot.req4
    global id_req
    id_req = req_tc[3][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req4)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[5][2]
    global next_state
    next_state = InputPhot.req5
    global id_req
    id_req = req_tc[4][0] 
    await state.set_state(InputPhot.photo)
    
@router.message(InputPhot.req5)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[6][2]
    global next_state
    next_state = InputPhot.req6
    global id_req
    id_req = req_tc[5][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req6)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[7][2]
    global next_state
    next_state = InputPhot.req7
    global id_req
    id_req = req_tc[6][0] 
    await state.set_state(InputPhot.photo)


@router.message(InputPhot.req7)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_tc[8][2]
    global next_state
    next_state = InputPhot.req8
    global id_req
    id_req = req_tc[7][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req8)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text =  """Ваша заявке сформирована и отправлена на рассмотрение"""
    global next_state
    next_state = InputPhot.req9
    global id_req
    id_req = req_tc[8][0] 
    await state.set_state(InputPhot.photo)    
    
@router.message(InputPhot.req10)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[2][2]
    global next_state
    next_state = InputPhot.req11
    global id_req
    id_req = req_ne[1][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req11)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[3][2]
    global next_state
    next_state = InputPhot.req12
    global id_req
    id_req = req_ne[2][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req12)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[4][2]
    global next_state
    next_state = InputPhot.req13
    global id_req
    id_req = req_ne[3][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req13)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[5][2]
    global next_state
    next_state = InputPhot.req14
    global id_req
    id_req = req_ne[4][0] 
    await state.set_state(InputPhot.photo)
    
@router.message(InputPhot.req14)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[6][2]
    global next_state
    next_state = InputPhot.req15
    global id_req
    id_req = req_ne[5][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req15)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[7][2]
    global next_state
    next_state = InputPhot.req16
    global id_req
    id_req = req_ne[6][0] 
    await state.set_state(InputPhot.photo)


@router.message(InputPhot.req16)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[8][2]
    global next_state
    next_state = InputPhot.req17
    global id_req
    id_req = req_ne[7][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req17)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[9][2]
    global next_state
    next_state = InputPhot.req18
    global id_req
    id_req = req_ne[8][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req18)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[10][2]
    global next_state
    next_state = InputPhot.req19
    global id_req
    id_req = req_ne[9][0] 
    await state.set_state(InputPhot.photo)
    
@router.message(InputPhot.req19)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[11][2]
    global next_state
    next_state = InputPhot.req20
    global id_req
    id_req = req_ne[10][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req20)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text = req_ne[12][2]
    global next_state
    next_state = InputPhot.req21
    global id_req
    id_req = req_ne[11][0] 
    await state.set_state(InputPhot.photo)

@router.message(InputPhot.req21)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = 'После окончания загрузки фото по требованию, чтобы перейти к следующему введите /next'
    await message.answer(text=tt)
    global req_text
    req_text =  """plan"""
    global next_state
    next_state = InputPhot.req22
    global id_req
    id_req = req_ne[12][0] 
    await state.set_state(InputPhot.photo)
    
@router.message(InputPhot.req22)
async def plan(message: Message, state: FSMContext):
    tt = ('Если вам требуется прикрепить нарисованную план-схему загородного дома\n' +
          'Вы можете прикрепить ее по команде /plan и там же будут описаны подробные требования и пример схемы\n'+
          'Если план прикреплять не нужно введите любой текст для перехода на следующий этап')
    await message.answer(text=tt)
    global req_text
    req_text =  """Ваша заявке сформирована и отправлена на рассмотрение"""
    await state.set_state(InputPhot.plan)

@router.message(InputPhot.plan)
@router.message(InputPhot.req9)
async def cmd_osmotr(message: Message, state: FSMContext):
    tt = """Статус заявки вы можете посмотреть в меню на вкладке <Текущие заявки>"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=builder,
        resize_keyboard=True,
    )
    await message.answer(text=tt, reply_markup=keyboard)
    await state.clear()


@router.message(Command(commands=['next']))
async def cmd_next(message: Message, state: FSMContext):
    if req_text == """Ваша заявке сформирована и отправлена на рассмотрение""" :
        con = psycopg2.connect(
        database="SovDB", user="postgres", password="password", 
        host="127.0.0.1", port="5432")
        cur = con.cursor()
        cur.execute(f"UPDATE application set status = 'отправлена' where ida = {appl_num}")
        con.commit()
        con.close()
        tt = req_text + '\n'
    else:
        if req_text == 'plan':
            tt = 'Отправьте любой текст для перехода'
        else:
            tt = "Вам нужно отправить " + req_text + '\n'
    tt = tt + 'Отправьте любой текст для перехода на следующий этап'
    await message.answer(text=tt)
    await state.set_state(next_state)
    
@router.message(InputPhot.photo)
@router.message(F.document)
async def download_photo(message:Message, bot: Bot, state: FSMContext):
    if message.document:
        id_photo = message.document.file_id
        await bot.download(
            message.document,
            destination=f"photoes/{message.document.file_id}.jpg"
            )
        file_path = f"photoes/{message.document.file_id}.jpg"
        global flag_plan
        if flag_plan == 1:
            tt = 'Фото принято на проверку'
            global id_req
            id_req = 23
        else:
            tt = prov_photo(file_path)
        if tt == 'Фото принято на проверку':
            idph = randrange(100000)
            idd = randrange(100000)
            idae = randrange(100000)
            con = psycopg2.connect(database="SovDB", user="postgres", password="password", 
            host="127.0.0.1", port="5432")
            cur = con.cursor()
            cur.execute(
            f"""INSERT INTO photo (idph,photopath) 
                    VALUES ({idph}, '{file_path}')""")
            cur.execute(
            f"""INSERT INTO phreq (id, idre, idpho)
                  VALUES ({idd}, {id_req}, {idph})""")
            cur.execute(
            f"""INSERT INTO applel (idae, idap, pr, mark)
                VALUES ({idae}, {appl_num}, {idd}, 'На проверке')""")
            con.commit()   
            con.close()
            flag_plan = 0
        await message.answer(text=tt)
    else:
        await message.answer(text=tt)
        

@router.message(InputPhot.textH)
@router.message(InputPhot.texxt)
async def text(message: Message, state: FSMContext):
    await state.update_data(input_text=message.text)
    user_data = await state.get_data()
    con = psycopg2.connect(
    database="SovDB", user="postgres", password="password", 
    host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(
    f"""SELECT ida, text from application WHERE ida = '{appl_num}'"""
        )
    dat = cur.fetchall()
    if dat[0][1] is not None:
        tt = str(dat[0][1]) + ' ' + user_data['input_text']
    else:
        tt = user_data['input_text']
    cur.execute(f"UPDATE application set text = '{tt}' where ida = {appl_num}")
    con.commit()
    con.close()

