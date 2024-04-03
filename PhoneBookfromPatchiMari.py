import sys
from easygui import*

PachiBook = {}
def load_book_from_file(filemane='Phonebook.txt'):
    with open(filemane, 'r', encoding='utf-8') as file:
        for line in file:
            poe3d = line.split(' ')
            id= poe3d[0]
            PiplInfo={'surname': poe3d[1], 'name' : poe3d[2], 'patronymic': poe3d[3], 'phone' : poe3d[4], 'dr' : poe3d[5], 'visable' : poe3d[6].strip()}
            PachiBook.update({id: PiplInfo})

def show_book():
    result=[]
    for key in PachiBook.keys():
        if 'en' in PachiBook[key]['visable']:
            result.append(f"ID {key}, ФИО: {PachiBook[key]['surname']} {PachiBook[key]['name']} {PachiBook[key]['patronymic']}, Номер телефона: {PachiBook[key]['phone']}, День рождения: {PachiBook[key]['dr']}\n")
    return(result)
def not_in_book():
    result=[]
    for key in PachiBook.keys():
        if 'dis' in PachiBook[key]['visable']:
            result.append(f"ID {key}, ФИО: {PachiBook[key]['surname']} {PachiBook[key]['name']} {PachiBook[key]['patronymic']}, Номер телефона: {PachiBook[key]['phone']}, День рождения: {PachiBook[key]['dr']}\n")
    return(result)
def show_not_in_book():
    content = not_in_book()
    codebox('Список контактов', 'Телефонный справочник', content)

def add_contact(surname, name, patronymic, number, dr):
    PiplInfo = {'surname' : surname, 'name' : name, 'patronymic' : patronymic, 'phone' : number, 'dr' : dr, 'visable' : 'en'}
    new_id= str(len(PachiBook.keys()) + 1)
    PachiBook.update({new_id : PiplInfo})
    save_book_to_file()

def save_book_to_file(filemane='Phonebook.txt'):
    with open(filemane, 'w', encoding='utf-8') as file:
        for key in PachiBook.keys():
            file.write(f"{key} {PachiBook[key]['surname']} {PachiBook[key]['name']} {PachiBook[key]['patronymic']} {PachiBook[key]['phone']} {PachiBook[key]['dr']} {PachiBook[key]['visable']}\n")

def update_contact(id, surname, name, patronymic, number, dr):
    PiplInfo = {'surname' : surname, 'name' : name, 'patronymic' : patronymic, 'phone' : number, 'dr' : dr, 'visable' : 'en'}
    PachiBook.update({id : PiplInfo})
    save_book_to_file()

def delite_contact(id):
    if id in PachiBook.keys():
        PachiBook[id]['visable'] = 'dis'
        save_book_to_file()
    else:
        msgbox('Неверно введён ID, либо контакт не найден', 'Ошибка')

def find_contacts(name):
    result = []
    for key in PachiBook.keys():
        if name.lower() in PachiBook[key]['name'].lower():
            result.append(f"ID {key}, ФИО: {PachiBook[key]['surname']} {PachiBook[key]['name']} {PachiBook[key]['patronymic']}, Номер телефона: {PachiBook[key]['phone']}, День рождения: {PachiBook[key]['dr']}\n")
    if result:
        codebox('Результаты поиска', 'Поиск контакта', result)
    else:
        msgbox('Контакт не найден', 'Поиск контакта')

def change_contacts():
    content = show_book()
    codebox('Запомните ID контакта, который хотите изменить', 'Изменение контакта', content)

def show_contacts():
    content = show_book()
    codebox('Список контактов', 'Телефонный справочник', content)

def recover_contact():
    show_not_in_book()
    id = enterbox("Введите ID контакта для восстановления:")
    if id in PachiBook.keys():
        PachiBook[id]['visable'] = 'en'
        save_book_to_file()
    else:
        msgbox('Неверно введён ID, либо контакт не найден', 'Ошибка')

pachimari = '111555.jpg'
msg = 'Ваш телефонный справочник от PatchiMari'
choices = ['Приступить']
reply = buttonbox(msg, image=pachimari, choices=choices)

load_book_from_file()

def main():
    while True:
        msg ="Какое действие желаете совершить?"
        title = "Телефонный справочник"
        choices = ["Добавить контакт", "Изменить контакт", "Удалить контакт" ,"Поиск контакта","Просмотр телефонного справочника", "Восстановить контакт", "Выйти"]
        choice = choicebox(msg, title, choices)
        
        if choice == "Добавить контакт":
            fieldValues = multenterbox("Введите данные контакта", "Добавить контакт", ["Фамилия", "Имя", "Отчество", "Номер телефона", "День рождения"])
            if fieldValues:
                surname, name, patronymic, number, dr = fieldValues
                add_contact(surname, name, patronymic, number, dr)


        elif choice == "Изменить контакт":
            change_contacts()
            id = enterbox("Введите ID контакта, который хотите изменить:")
            contact = PachiBook.get(id)
            if contact:
                fields = ["Фамилия", "Имя", "Отчество", "Номер телефона", "День рождения"]
                values = list(contact.values())
                new_values = multenterbox(msg="Введите новые данные", title="Изменение контакта", fields=fields, values=values)
            if new_values:
                update_contact(id, *new_values)
            else:
                msgbox("Контакт с данным ID не найден.", "Ошибка")


        elif choice == "Удалить контакт":
            change_contacts()
            id = enterbox("Введите ID контакта, который хотите удалить:")
            delite_contact(id)

        elif choice == "Поиск контакта":
            name = enterbox("Введите имя контакта для поиска:")
            if name:
                find_contacts(name)

        elif choice == "Просмотр телефонного справочника":
            show_contacts()
        
        elif choice == "Восстановить контакт":
            recover_contact()

        elif choice == "Выйти":
            sys.exit(0)
if __name__ == '__main__':
    main()