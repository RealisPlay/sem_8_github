def print_contact(file_name): # функция для вывода всех контактов
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print('Список контактов пустой')



def connect_with_user(): # спрашивает у юзера информацию
    print('Введите имя, фамилию и телефон (например: Иванов Иван 89132456377): ')
    cont_info = input()
    return cont_info



def add_contact(file_name): # добавить контакт
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append(new_cont + '\n')
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)



def find_contact(file_name): # найти контакт

    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print('Выберите критерий для поиска: \
            \n1 - Имя \
            \n2 - Фамилия \
            \n3 - Телефон')

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)



def delite_contact(file_name): # удаление контакта
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            print('Все контакты: ')
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print('Список контактов пустой')
    print('Укажите, какой контакт вы бы хотели удалить: ')
    data = input()
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list:
            all_cont.remove(cont)
            print('Контакт удален')
            with open(file_name, 'w', encoding='utf8') as file:
                file.writelines(all_cont)



def update_contact(file_name): # изменение контакта
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    old_cont = input("Введите имя и фамилию контакта: ")

    print('Чтобы вы хотели изменить? \
              \n1 - Фамилию \
              \n2 - Имя \
              \n3 - Телефон')

    comm = int(input())

    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if old_cont in cont_as_list[comm - 1]:
            new_value = input('Введите измененные данные: ')
            cont_as_list[comm - 1] = new_value
            all_cont.remove(cont)
            all_cont.append('\n' + ' '.join(cont_as_list))
            print('Контакт изменен')
            with open(file_name, 'w', encoding='utf8') as file:
                file.writelines(all_cont)