def custom_write(file_name: str, strings:list):
    file = open(file_name, 'w+', encoding='utf-8')
    counter = 0
    result = {}
    for i in strings:
        counter += 1
        b = file.tell()
        result[(counter, b)] = i
        file.write(f'{i}\n')

    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
