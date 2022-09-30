from Contact import Contact
from functions_with_contacts import *
from prints import *
import time
print('Введите имя файла с базой контактов (без расширения)')
file_name = input() + '.txt'
print_hello()
command = ' '.join(input().split())
#"сердце" программы
while command != 'close':
    # считываем базу и передаем в массив contacts_array
    com = False
    contacts_array = show_contacts(file_name)
    while contacts_array == []:
        print('Введите имя файла с базой контактов (без расширения)')
        file_name = input() + '.txt'        
    if command == 'show contacts':
        for i in contacts_array:
            print(i.pyout())
    elif command == 'find by phone number':
        print('Введите номер телефона')
        find_by_phone_number(contacts_array)
    elif command == 'find by email':
        print('Введите электронную почту')
        find_by_email(contacts_array)
    elif command == 'find by name':
        print('Введите имя')
        find_by_name(contacts_array)
    elif command == 'find by surname':
        print('Введите фамилию')
        find_by_surname(contacts_array)
    elif command == 'find by middle name':
        print('Введите отчество')
        find_by_middle_name(contacts_array)
    elif command == 'find by surname and name':
        print('Введите имя и фамилию')
        find_by_surname_and_name(contacts_array)
    elif command == 'find by all':
        print('Введите ФИО')
        find_by_all(contacts_array)
    elif command == 'find empty phone number':
        find_empty_phone_number(contacts_array)
    elif command == 'find empty email':
        find_empty_email(contacts_array)
    elif command == 'find empty email and phone number':
        find_empty_email_and_phone_number(contacts_array)
    elif command == 'change contact':
        which_contact()
        command = ' '.join(input().split())
        if command == 'find by phone number':
            print('Введите номер телефона')
            array = find_by_phone_number(contacts_array)
        elif command == 'find by email':
            print('Введите электронную почту')
            array = find_by_email(contacts_array)
        elif command == 'find by surname':
            print('Введите фамилию')
            array = find_by_surname(contacts_array)
        elif command == 'find by surname and name':
            print('Введите имя и фамилию')
            array = find_by_surname_and_name(contacts_array)
        elif command == 'find by all':
            print('Введите ФИО')
            array = find_by_all(contacts_array)
        elif command == 'back':
            print('Вернул Вас назад')
            com = True
        else:
            com = True
            print('Я не понимаю вашу команду, начните с начала, пожалуйста')
        if not com:
            elem = 0
            if array == 0:
                print('ничего не найдено')
            else:
                if len(array) > 1:
                    print('Введите порядковый номер контакта из вышеперечисленных, которого вы хотите изменить.')
                    elem = int(input()) - 1
                    how_change()
                    command = ' '.join(input().split())
                    line = array[elem]
                    if str(command) == 'change number':
                        print('Введите новый номер')
                        command = ' '.join(input().split())
                        line2 = Contact(line.surname, line.name, line.middle_name, command, line.email)
                        contacts_array[contacts_array.index(line)] = line2
                        re_write(contacts_array, file_name)
                        print('Изменения успешно внесены!')
                    elif str(command) == 'change email':
                        print('Введите новую почту')
                        command = ' '.join(input().split())
                        line2 = Contact(line.surname, line.name, line.middle_name, line.phone_number, command)
                        contacts_array[contacts_array.index(line)] = line2
                        re_write(contacts_array, file_name)
                        print('Изменения успешно внесены!')
                    elif str(command) == 'change name':
                        print('Введите новое имя')
                        command = ' '.join(input().split())
                        line2 = Contact(line.surname, command, line.middle_name, line.phone_number, line.email)
                        contacts_array[contacts_array.index(line)] = line2
                        re_write(contacts_array, file_name)
                        print('Изменения успешно внесены!')
                    elif str(command) == 'change surname':
                        print('Введите новую фамилию')
                        command = ' '.join(input().split())
                        line2 = Contact(command, line.name, line.middle_name, line.phone_number, line.email)
                        contacts_array[contacts_array.index(line)] = line2
                        re_write(contacts_array, file_name)
                        print('Изменения успешно внесены!')
                    elif str(command) == 'change middle name':
                        print('Введите новое отчество')
                        command = ' '.join(input().split())
                        line2 = Contact(line.surname, line.name, command, line.phone_number, line.email)
                        contacts_array[contacts_array.index(line)] = line2
                        re_write(contacts_array, file_name)
                        print('Изменения успешно внесены!')
                    elif str(command) == 'back':
                        com = True
                    else:
                        print('Извините, но я Вас не понимаю :(')
    command = ' '.join(input().split())     

