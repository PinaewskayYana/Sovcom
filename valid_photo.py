from PIL import Image
import exifread

def check_photo_properties(file_path):
     #Проверяем размер фото
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
