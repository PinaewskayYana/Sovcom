#from aiogram import F, Router, Bot
#from aiogram.types import Message
from PIL import Image
import exifread
from PIL.ExifTags import TAGS
#from workwithDB.connectDB import id_photo, file_path


def prov_photo(file_path):
    textt = ''
    image = Image.open(file_path)
    width, height = image.size
    if width <= 1600 or height <= 1200:
        textt = textt + "Размер фото слишком мал\n"
    
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
    
    if not tags:
        textt = textt + "Отсутствуют метаданные. Вы можете посмотреть, как их подключать по команде /data\n"
    
    exposure_program = tags.get('EXIF ExposureProgram')
    
    if exposure_program is None or exposure_program.values[0] >= 2.5:
        textt = textt + "Фото сделано без достаточного количества света\n"
    
    software = tags.get('Software')
    if software is not None:
        textt = textt + "Фото было отредактировано\n"
    if textt != '':
        textt = 'Фото не принято\n' + textt
    else:
        textt = 'Фото принято на проверку'
    return textt