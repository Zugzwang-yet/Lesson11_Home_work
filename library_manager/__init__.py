# Выполняется при первом импорте пакета
print('Инициализация пакета laybrary_manager')

# Определение списка экспортируемых модулей
__all__ = ['catalog', 'report', 'utils']

# Импортирование ключевых классов и функций для удобства
from .catalog import Library
from .report import generate_report