from sem_8_function import *

Contact = 'Contacts.txt'

def interface():
    while True:
        print('Выберете действие:\
            \n 1 - Добавить контакт \
            \n 2 - Вывести все контакты \
            \n 3 - Найти контакт \
            \n 4 - Удалить контакт \
            \n 5 - Изментить контакт \
            \n 0 - Выйти')

        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(Contact)
            case 2:
                print_contact(Contact)
            case 3:
                find_contact(Contact)
            case 4:
                delite_contact(Contact)
            case 5:
                update_contact(Contact)
            case _:
                print('Неверная команда')

if __name__ == '__main__':
    interface()