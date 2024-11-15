import json
import os
from module1 import get_image_info
from module1 import rename_image

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