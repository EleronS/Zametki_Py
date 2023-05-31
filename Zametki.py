import os
import sys
import time
import datetime
import json, string

notes = {}

def create_notes_file(filename, lang, title):
    if os.path.isfile(filename):                      #проверка на наличие файла 
        os.remove(filename)                           #удаляем его
    
    with open(filename, 'w') as f:                    #создаем новый файл
        f.write(f'Title:{title}')
        if lang == 'ru':
            f.write('Заметка на русском языке')       #проверяем язык ввода
            f.write(notes[title] + '')
        elif lang == 'en':
            f.write('Note in English')
            f.write(notes[title].encode('utf-8') + '')

def edit_note(title, lang):                          #редактирование заметок
    global notes
    with open('notes.json','r+') as f:
        current_note = f.read
        del notes[title]
        notes[title] = current_note

def main():
    title = input("Введите название заметки: ")
    lang = input("Выберите язык: ru/en (ru по умолчанию)")
    if lang == '':
        lang = 'ru'
        create_notes_file('notes.json', lang, title)
        print('Заметка успешно создана')
        for title in notes:
            print(f'Заметка"{title}":')
        edit_note(title)
        
if __name__ =='__main__':
    main()


