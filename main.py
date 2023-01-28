from pprint import pprint
import os


class CookBook:
    def __init__(self):
        self.cook_book = {}
        self.dishes = []

    def open_book(self, file):
        folder_name = 'book'
        file_name = 'Cook_book.txt'
        path = os.path.join(os.getcwd(), folder_name, file_name)
        with open(path, 'r', encoding='utf-8') as file:
            cook_book = {}
            for line in file:
                dish_name = line.strip()
                dishes = []
                for i in range(int(file.readline())):
                    product = file.readline().strip()
                    ingredient_name, quantity, measure = product.split(' | ')
                    dishes.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                file.readline()
                self.cook_book[dish_name] = dishes
        return cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        lst = []
        for dish in dishes:
            if dish in self.cook_book:
                for i in self.cook_book[dish]:
                    lst.append(i['ingredient_name'])
                    i['quantity'] = int(i['quantity']) * person_count * lst.count(i['ingredient_name'])
                    shop_list[i['ingredient_name']] = {'measure': i['measure'], 'quantity': i['quantity']}
        return shop_list


book = CookBook()
book.open_book('Cook_book.txt')
pprint(book.cook_book)
print()
pprint(book.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10))