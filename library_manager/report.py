from library_manager import Library

def generate_report(library: Library):
    all_books = library.get_details()
    total_books = len(all_books)
    authors = set([item['автор'] for item in all_books])
    total_authors = len(authors)
    genres = set([item['жанр'] for item in all_books])
    total_genres = len(genres)
    return f'Всего книг в библиотеке: {total_books}, авторов: {total_authors}, жанров: {total_genres}'