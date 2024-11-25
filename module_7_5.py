import os
import time

dir_path = ''
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = time.strftime("%d.%m.%Y %H:%M",time.localtime(os.path.getmtime(filepath)))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, '
              f'Родительская директория: {parent_dir}')