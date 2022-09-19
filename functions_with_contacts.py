from Contact import Contact
import time
import sys
#функция выгрузки контактов в класс и передача их в виде массива
def show_contacts(file_name):
    array = []
    try:
        with open(file_name, 'r') as f:
            line = f.readline()
            while line != '':
                line1 = ' '.join(line[:line.find(',')].split())
                line2 = line[line.find(',') + 2:line.rfind(',')]
                line3 = line[line.rfind(',') + 2:len(line) - 1]
                if line1.count(' ') == 0:
                    if line2 != '':
                        if line3 != '':
                            contact = Contact(line1, '', '', line2, line3)
                        else:
                            contact = Contact(line1, '', '', line2, '')
                    else:
                        if line3 != '':
                            contact = Contact(line1, '', '', '', line3)
                        else:
                            contact = Contact(line1, '', '', '', '')
                elif line1.count(' ') == 1:
                    surname, name = map(str, line1.split())
                    if line2 != '':
                        if line3 != '':
                            contact = Contact(surname, name, '', line2, line3)
                        else:
                            contact = Contact(surname, name, '', line2, '')
                    else:
                        if line3 != '':
                            contact = Contact(surname, name, '', '', line3)
                        else:
                            contact = Contact(surname, name, '', '', '')
                else:
                    surname, name, middle_name = map(str, line1.split())
                    if line2 != '':
                        if line3 != '':
                            contact = Contact(surname, name, middle_name, line2, line3)
                        else:
                            contact = Contact(surname, name, middle_name, line2, '')
                    else:
                        if line3 != '':
                            contact = Contact(surname, name, middle_name, '', line3)
                        else:
                            contact = Contact(surname, name, middle_name, '', '')

                array.append(contact)
                line = f.readline()
            return array
    except FileNotFoundError:
        print('Вы все испортили!!!!!!')
        time.sleep(1.5)
        sys.exit()

def find_by_phone_number(contacts_array):
    command = ' '.join(input().split())
    array = []
    for i in contacts_array:
        if str(i.get_phone_number()) == str(command):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_email(contacts_array):
    command = ' '.join(input().split())
    array = []
    for i in contacts_array:
        if str(i.get_email()) == str(command):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_name(contacts_array):
    command = ' '.join(input().split())
    array = []
    for i in contacts_array:
        if str(i.get_name()) == str(command):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_surname(contacts_array):
    command = ' '.join(input().split())
    array = []
    for i in contacts_array:
        if str(i.get_surname()) == str(command):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_middle_name(contacts_array):
    command = ' '.join(input().split())
    array = []
    for i in contacts_array:
        if str(i.get_middle_name()) == str(command):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_surname_and_name(contacts_array):
    surname, name = map(str, input().split())
    array = []
    for i in contacts_array:
        if str(i.get_surname()) == str(surname) and str(i.get_name()) == str(name):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_by_all(contacts_array):
    surname, name, middle_name = map(str, input().split())
    array = []
    for i in contacts_array:
        if str(i.get_surname()) == str(surname) and str(i.get_name()) == str(name)and str(i.get_middle_name()) == str(middle_name):
            array.append(i)
    if len(array) == 0:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    print('Было найдено', len(array), 'совпадений:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')
    return array

def find_empty_phone_number(contacts_array):
    array = []
    for i in contacts_array:
        if str(i.get_phone_number()) == '':
            array.append(i)
    if len(array) == 0:
        print('У всех контактов заполнены номера телефонов')
    print('Было найдено', len(array), 'контактов без номера телефона:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')

def find_empty_email(contacts_array):
    array = []
    for i in contacts_array:
        if str(i.get_email()) == '':
            array.append(i)
    if len(array) == 0:
        print('У всех контактов заполнена электронная почта')
    print('Было найдено', len(array), 'контактов без электронной почты:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')

def find_empty_email_and_phone_number(contacts_array):
    array = []
    for i in contacts_array:
        if str(i.get_phone_number()) == '' or str(i.get_email()) == '':
            array.append(i)
    if len(array) == 0:
        print('У всех контактов заполнены номера телефонов и электронная почта')
    print('Было найдено', len(array), 'контактов без номера телефона или электронной почты:')
    for i in range(len(array)):
        print(i + 1, ': ', array[i].pyout(), sep='')

def re_write(contacts_array):
    with open('contacts.txt', 'w') as f:
        for i in contacts_array:
            f.write(i.get_surname() + ' ' + i.get_name() + ' ' + i.get_middle_name() + ', ' + i.get_phone_number() + ', ' + i.get_email() + '\n')
