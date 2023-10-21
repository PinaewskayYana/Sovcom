from PIL import Image
import exifread
from PIL.ExifTags import TAGS
import datetime


def get_photo_created_date(file_path):
    try:
        with Image.open(file_path) as image:
            exif_data = image._getexif()
            if exif_data is not None:
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    if tag_name == "DateTimeOriginal":
                        return value
    except Exception as e:
        print(f"Error: {e}")
    
    return None

def check_photo_properties(file_path):
    # Проверяем размер фото
    image = Image.open(file_path)
    width, height = image.size
    
    if width <= 1600 or height <= 1200:
        print( "Размер фото слишком мал")
    
     #Проверяем наличие метаданных
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
    
    if not tags:
        print( "Отсутствуют метаданные")
    
     #Проверяем размытие/шумы
    sharpness = tags.get('Image Tag 0xA20E')
    if sharpness is None or sharpness.values[0] < 100:
        print( "Фото размыто или содержит шумы")
    
     #Проверяем количество света на фото
    exposure_program = tags.get('EXIF ExposureProgram')
    if exposure_program is None or exposure_program.values[0] != 0:
        print( "Фото сделано без достаточного количества света")
    
     #Проверяем, была ли фотография отредактирована
    software = tags.get('Software')
    if software is not None:
        print( "Фото было отредактировано")
    
    # Определение геолокации объекта
    gps_latitude = tags.get('GPS GPSLatitude')
    gps_longitude = tags.get('GPS GPSLongitude')
    if gps_latitude is None or gps_longitude is None:
        print( "Геолокация не найдена")
    
    latitude = gps_latitude.values
    longitude = gps_longitude.values
    return f"Геолокация: широта {latitude}, долгота {longitude}"

# Пример использования функции
photo_path = "photoes/BQACAgIAAxkBAAIBOmUyRD0-YCVDWcmRqavjM9pNPA8GAAIvOAACZLGQSZsUvJZNS8GuMAQ.jpg"
result = check_photo_properties(photo_path)
print(result)
# Получение текущей даты и времени
now = datetime.datetime.now()

# Форматирование даты и времени
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Вывод даты и времени
print("Текущая дата и время:", formatted_date)
created_date = get_photo_created_date(photo_path)
if created_date is not None:
    print(f"Дата создания фото: {created_date}")
else:
    print("Не удалось получить дату создания фото.")
if created_date <= formatted_date:
    print("Фото свежее")
else:
    print("Фото старое")
