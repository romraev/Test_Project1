import text as t
from datetime import datetime as dt

def menu() -> int:
    print(t.main_menu[0])
    for i in range(1, len(t.main_menu)):
        print(f'\t{i}. {t.main_menu[i]}')
    select = input(t.select_menu)
    if select.isdigit() and 0 < int(select) < (len(t.main_menu)):
        return int(select)
    print(t.input_error)

def add_note():
    new = {}
    for key, value in t.new_note.items():
        new[key] = input(value)
    new['date_time'] = dt.now().strftime("%d/%m/%y %I:%M")
    return new

def show_notes(book: dict[int: dict[str, str]], message):
    if book:
        max_name = []
        max_text = []
        for note in book.values():
            max_name.append(len(note.get('name')))
            max_text.append(len(note.get('text')))
        size_name = max(max_name)
        size_text = max(max_text)
        print('\n' + '=' * (size_name + size_text + 21))
        for index, note in book.items():
            print(f'{index:>3}. {note.get("name"):<{size_name}} {note.get("text"):<{size_text}} {note.get("date_time")}')
        print('=' * (size_name + size_text + 21) + '\n')
    else: 
        print(message)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def search_word() -> str:
    return input(t.search_word)

def select_id(text) -> int:
    id = input(text)
    return id