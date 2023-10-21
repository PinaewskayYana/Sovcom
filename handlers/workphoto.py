from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, ContentType
from texts import WELCOME_MES, SPRAVKA, PHOTO, ANDROID, IPHONE
from keyboards.auto import kb_autor, builder, phone
from PIL import Image
import exifread


router=Router()

@router.message(F.document)
async def download_photo(message:Message, bot: Bot):
    id_photo = message.document.file_id
    await bot.download(
        message.document,
        destination=f"photoes/{message.document.file_id}.jpg"
    )
    file_path = f"photoes/{message.document.file_id}.jpg"
    image = Image.open(file_path)
    textt =''
    width, height = image.size
    if width <= 1600 or height <= 1200:
        textt = textt + "Размер фото слишком мал\n"
    
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
    
    if not tags:
        textt = textt + "Отсутствуют метаданные. Вы можете посмотреть, как их подключать по команде /data\n"
    
    software = tags.get('Software')
    if software is not None:
        textt = textt + "Фото было отредактировано\n"
    if textt != '':
        textt = 'Фото не принято\n' + textt
    else:
        textt = 'Фото принято на проверку'
    await message.answer(text=textt
                         )