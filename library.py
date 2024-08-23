from library_manager import Library, generate_report
from library_manager.utils import validate_book_data, format_book_data

library = Library()

library.add_book('Пролетая над гнездом кукушки', 'Кен Кизи', 'трагедия')
library.add_book('Над пропастью во ржи', 'Джером Дэвид Сэлинджер', 'роман')
library.add_book('Сто лет одиночества', 'Габриэль Гарсиа Маркес', 'роман')
library.add_book('Чума', 'Альбер Камю', 'роман')
library.add_book('Камо грядеши', 'Генрик Сенкевич', 'роман')
library.add_book('Тихий Дон', 'Михаил Шолохов', 'роман')
library.add_book('Поднятая целина', 'Михаил Шолохов', 'роман')
library.add_book('Мастер и Маргарита', 'Михаил Булгаков', 'роман')
library.add_book('Тарас Бульба', 'Николай Гоголь', 'повесть')
library.add_book('Записки сумасшедшего', 'Николай Гоголь', 'повесть')
library.add_book('Шагреневая кожа', 'Оноре де Бальзак', 'роман')
library.add_book('Блеск и нищета куртизанок', 'Оноре де Бальзак', 'роман')
library.add_book('Жизнь холостяка', 'Оноре де Бальзак', 'роман')
library.add_book('Евгений Онегин', 'Александр Пушкин', 'роман')
library.add_book('Кавказский пленник', 'Александр Пушкин', 'поэма')
library.add_book('Кавказский пленник', 'Лев Толстой', 'рассказ')
library.add_book('Бедные люди', 'Лев Толстой', 1905)
library.add_book('Детство', 'Лев Толстой', 'повесть')
library.add_book('Детство', 'Максим Горький', 'повесть')
library.add_book('На дне', 'Максим Горький', 'драма')

print(library.get_details())
print(generate_report(library))

library.remove_book('Записки сумасшедшего')
print(generate_report(library))

print(library.find_book('Название книги', 'На дне'))
print('')
for i in library.find_book('Название книги', 'Детство'):
    print(i)
print('')
for i in library.find_book('автор', 'Оноре де Бальзак'):
    print(i)
print('')
for i in library.find_book('жанр', 'повесть'):
    print(i)

for i in library.get_details():
    validate_book_data(i)

for i in library.get_details():
    print(format_book_data(i))


