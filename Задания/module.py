import os
from PIL import Image
import datetime
import json

def get_image_info(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        resolution = image.resolution
        date_created = datetime.datetime.fromtimestamp(os.stat(image_path).st_ctime)
        return {
        'width': width,
        'height': height,
        'resolution': resolution,
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

def get_user_input():
    while True:
        try:
            image_path = input("Введите путь к изображению: ")
            if os.path.exists(image_path):
                return image_path
            else:
                print("Ошибка: файл не найден")
        except Exception as e:
            print(f"Ошибка при вводе: {e}")

def store_data(image_path, data):
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file)
        print("Данные успешно сохранены")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return {}

def main():
    image_path = get_user_input()
    image_info = get_image_info(image_path)
    if image_info:
        print(f"Информация об изображении:")
        print(f" Ширина: {image_info['width']}")
        print(f" Высота: {image_info['height']}")
        print(f" Разрешение: {image_info['resolution']}")
        print(f" Дата создания: {image_info['date_created']}")
        new_name = input("Введите новое имя для изображения (если нужно переименовать): ")
    if new_name:
        rename_image(image_path, new_name)
        print(f"Изображение переименовано в {new_name}")
    else:
        print("Изображение не переименовано")

if __name__ == "__main__":
    main()
