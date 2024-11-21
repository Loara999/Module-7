from pprint import pprint


class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        while True:
            content = file.readline()
            content = content.replace('\n', '')
            if not content:
                break
            print(content)
        file.close()

    def add(self, *products:Product):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        content = file.read()
        for i in products:
            if f'{i}\n' not in content:
                file.write(f'{i}\n')
            else:
                print(f'Продукт {i.name} уже есть в магазине.')
        file.close()

s1 = Shop()
b = Product('Banana', 0.3, 'Fruits')
m = Product('Milk', 1, 'Milk products')
a = Product('apple', 0.2, 'Fruits')
s1.add(b, m)
s1.get_products()
s1.add(b)
s1.add(a)
s1.get_products()