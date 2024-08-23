class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, genre: str):
        self.books.append({'Название книги': title, 'автор': author, 'жанр': genre})

    def remove_book(self, book_title: str):
        self.books = [book for book in self.books if book['Название книги'] != book_title]

    def find_book(self, search_parameter: str, search_value: str):
        match search_parameter:
            case 'Название книги': return [book for book in self.books if book['Название книги'] == search_value]
            case 'автор': return [book for book in self.books if book['автор'] == search_value]
            case 'жанр': return [book for book in self.books if book['жанр'] == search_value]
            case _: return []

    #def get_details(self):
    #    books = 'Список книг в библиотеке:\n'
    #    for item in self.books:
    #        books += f'{item['Название книги']}, {item['автор']}, {item['жанр']}\n'
    #    return books
    
    def get_details(self):
        books = []
        for item in self.books:
            books.append({'Название книги': item['Название книги'], 'автор': item['автор'], 'жанр': item['жанр']})
        return books
    

        
        