import os
from PIL import Image
import datetime

def get_image_info(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        resolution = f"{width} x {height}"
        file_size = os.path.getsize(image_path)
        date_created = datetime.datetime.fromtimestamp(os.stat(image_path).st_ctime)
        return {
            'width': width,
            'height': height,
            'resolution': resolution,
            'file_size': file_size,
            'date_created': date_created
        }
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return None

def rename_image(image_path, new_name):
    try:
        os.rename(image_path, new_name)
        print(f"Изображение переименовано в {new_name}")
    except Exception as e:
        print(f"Ошибка при переименовании изображения: {e}")
