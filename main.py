import json
from datetime import datetime


# Сохранение заметки в JSON-файл
def save_note(note):
    filename = 'notes.json'
    with open(filename, 'w') as outfile:
        data = json.dumps(note)
        outfile.write(data)


# Загрузка заметки из JSON-файла
def load_note():
    filename = 'notes.json'
    data = None
    try:
        with open(filename) as infile:
            data = json.loads(infile.read())
    except IOError:
        raise ValueError('Ошибка при чтении файла')
    return data


def main():
    notes = [
        {
            'id': 1,
            'title': 'Заметка 1',
            'body': 'Это первая заметка',
            'created_at': '2023-01-01'
        },
        {
            'id': 2,
            'title': 'Заметка 2',
            'body': 'А это вторая заметка',
            'created_at': '2023-02-01'
        }
    ]

    while True:
        action = input('Выбор действия: ').strip().lower()

        if action == 'exit' or action == 'e' or action.startswith('ed'):
            break

        elif action == 's' and len(notes) > 0:
            id_ = input('ID заметки для создания: ')
            if id_ in notes:
                new_note = load_note()
                if new_note:
                    new_note['id'] = id_
                    notes.append(new_note)
                else:
                    raise ValueError('Заметка не найдена')
                    break
            else:
                note = load_note()
                note['created_at'] = datetime.now()
                notes.append(note)

        elif action == 'c':
            for note in notes:
                id_ = note['id']
                title = input(f'Редактирование заметки {id_}: ')
                body = input(f'Введите текст: ')
                created_at = input(f'Укажите дату создания (YYYY-MM-DD) или оставьте пустой для текущей даты: ')

                data = {
                    'id': id_,
                    'title': title,
                    'body': body,
                    'created_at': created_at
                }
                save_note(data)

        elif action.startswith('r'):
            id_ = int(input('Выберите заметку: '))
            if len(notes) and id_:
                note = notes[id_ - 1]
                if note:
                    print(f'Заметка {note["title"]} ({note["created_at"]})')
                else:
                    print(f'{action} Заметка не найдена.')
                    continue
            else:
                print(action + ' Заметка не создана или удалена.')

        elif action == 'u':
            del_note = input('Удаление заметки: ')
            id_ = del_note.strip()
            try:
                del notes[int(id_) - 1]
            except IndexError:
                raise ValueError(f'Заметка с ID {del_note} не найдена!')
        elif action in ('a', 'add'):
            title = input(f'Название заметки {id_}: ')
            body = input(f'Введите текст: ')
            created_at = input(f'Укажите дату создания (YYYY-MM-DD): ')

            data1 = {
                'id': id_,
                'title': title,
                'body': body,
                'created_at': created_at
            }
            save_note(data1)


if __name__ == "__main__":
    main()