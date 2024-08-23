def validate_book_data(data: dict) -> bool:
    try:
        if not all(item in data for item in ['Название книги', 'автор', 'жанр']):
            raise ValueError('Отсутствуют обязательные поля')
        for item in ['Название книги', 'автор', 'жанр']:
            if not isinstance(data[item], str):
                raise TypeError(f'Неподходящий тип данных для ключа {item}')
    except (ValueError, TypeError) as e:
        print(f'Ошибка: {e}, в данных книги {data}')
        return False
    else:
        return True

            

    