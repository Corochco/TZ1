#создаем класс 1 (1 пункт оценки - 1 балл)
class Contact(object):
    #конструктор класса
    def __init__(self, surname, name, middle_name, phone_number, email):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.email = email
        self.phone_number = phone_number
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_middle_name(self):
        return self.middle_name
    def get_email(self):
        return self.email
    def get_phone_number(self):
        return self.phone_number
    def pyout(self):
        if self.name == '':
            if self.phone_number == '':
                if self.email == '':
                    return str(self.surname)
                else:
                    return str(self.surname) + ' ' + str(self.email)
            else:
                if self.email == '':
                    return str(self.surname) + ' ' + str(self.phone_number)
                else:
                    return str(self.surname) + ' ' + str(self.phone_number) + ' ' + str(self.email)
        elif self.middle_name == '':
            if self.phone_number == '':
                if self.email == '':
                    return str(self.surname) + ' ' + str(self.name)
                else:
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.email)
            else:
                if self.email == '':
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.phone_number)
                else:
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.phone_number) + ' ' + str(self.email)
        else:
            if self.phone_number == '':
                if self.email == '':
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.middle_name)
                else:
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.middle_name) + ' ' + str(self.email)
            else:
                if self.email == '':
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.middle_name) + ' ' + str(self.phone_number)
                else:
                    return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.middle_name) + ' ' + str(self.phone_number) + ' ' + str(self.email)

#функция выгрузки контактов в класс и передача их в виде массива
def show_contacts():
    array = []
    with open('contacts.txt', 'r') as f:
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

def find_by_phone_number(contacts_array):
    b = False
    command = ' '.join(input().split())
    for i in contacts_array:
        if str(i.get_phone_number()) == str(command):
            print(i.pyout())
            b = True
            line = i
            break
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    return line

def find_by_email(contacts_array):
    b = False
    command = ' '.join(input().split())
    for i in contacts_array:
        if str(i.get_email()) == str(command):
            print(i.pyout())
            b = True
            line = i
            break
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    return line

def find_by_name(contacts_array):
    b = False
    command = ' '.join(input().split())
    for i in contacts_array:
        if str(i.get_name()) == str(command):
            print(i.pyout())
            b = True
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')

def find_by_surname(contacts_array):
    b = False
    command = ' '.join(input().split())
    for i in contacts_array:
        if str(i.get_surname()) == str(command):
            print(i.pyout())
            b = True
            line = i
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    return line

def find_by_middle_name(contacts_array):
    b = False
    command = ' '.join(input().split())
    for i in contacts_array:
        if str(i.get_middle_name()) == str(command):
            print(i.pyout())
            b = True
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')

def find_by_surname_and_name(contacts_array):
    b = False
    surname, name = map(str, input().split())
    for i in contacts_array:
        if str(i.get_surname()) == str(surname) and str(i.get_name()) == str(name):
            print(i.pyout())
            b = True
            line = i
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    return line

def find_by_all(contacts_array):
    b = False
    surname, name, middle_name = map(str, input().split())
    for i in contacts_array:
        if str(i.get_surname()) == str(surname) and str(i.get_name()) == str(name) and str(i.get_middle_name()) == str(middle_name):
            print(i.pyout())
            b = True
            line = i
    if not b:
        print('Извините, но по вашему запросу контактов не найдено')
        return 0
    return line

def find_empty_phone_number(contacts_array):
    b = False
    for i in contacts_array:
        if str(i.get_phone_number()) == '':
            print(i.pyout())
            b = True
    if not b:
        print('У всех контактов заполнены номера телефонов')

def find_empty_email(contacts_array):
    b = False
    for i in contacts_array:
        if str(i.get_email()) == '':
            print(i.pyout())
            b = True
    if not b:
        print('У всех контактов заполнены номера телефонов')

def find_empty_email_and_phone_number(contacts_array):
    b = False
    for i in contacts_array:
        if str(i.get_email()) == '' and str(i.get_phone_number()) == '':
            print(i.pyout())
            b = True
    if not b:
        print('У всех контактов заполнены номера телефонов')

def re_write(contacts_array):
    with open('contacts.txt', 'w') as f:
        for i in contacts_array:
            f.write(i.get_surname() + ' ' + i.get_name() + ' ' + i.get_middle_name() + ', ' + i.get_phone_number() + ', ' + i.get_email() + '\n')

#приветственное сообщение и первая команда(в приведственном сообщении распишем все команды
print('Введите команду (если хотите закрыть приложение, введите close. \nДля вывода всех контактов введите show contacts. \nДля поиска по номеру телефона введите find by phone number. \nДля поиска по электронной почте введите find by email. \nДля поиска по имени введите find by name. \nДля поиска по фамилии введите find by surname. \nДля поиска по отчеству введите find by middle name. \nДля поиска по фамилии, имени, отчеству введите find by all (пожалуйста пишите фамилию, имя и отчество в порядке, как в этой строке).\nДля поиска по фамилии и имени введите find by surname and name (пожалуйста пишите фамилию и имя в порядке, как в этой строке).  \nДля поиска контактов без номера телефона введите find empty phone number. \nДля поиска контактов без номера телефона введите find empty email. \nДля поиска контактов без номера телефона и почты введите find empty email and phone number. \nДля редактирования контакта введите change contact.')
command = ' '.join(input().split())

#"сердце" программы
while command != 'close':
    # считываем базу и передаем в массив contacts_array
    contacts_array = show_contacts()
    if command == 'show contacts':
        for i in contacts_array:
            print(i.pyout())
    elif command == 'find by phone number':
        find_by_phone_number(contacts_array)
    elif command == 'find by email':
        find_by_email(contacts_array)
    elif command == 'find by name':
        find_by_name(contacts_array)
    elif command == 'find by surname':
        find_by_surname(contacts_array)
    elif command == 'find by middle name':
        find_by_middle_name(contacts_array)
    elif command == 'find by surname and name':
        find_by_surname_and_name(contacts_array)
    elif command == 'find by all':
        find_by_all(contacts_array)
    elif command == 'find empty phone number':
        find_empty_phone_number(contacts_array)
    elif command == 'find empty email':
        find_empty_email(contacts_array)
    elif command == 'find empty email and phone number':
        find_empty_email_and_phone_number(contacts_array)
    elif command == 'change contact':
        print('Для изменения контакта выберите способ его нахождения \n(ниже выберете в зависимости от всех атрибутов контакта, то есть если есть только фамилия, то поиск по фамилии и тп)\nПоиск по фамилии find by surname \nПоиск по фамилии и имени find by surname and name \nПоиск по фамилии, имени и отчеству find by all \nПоиск по номеру телефона find by phone number\nПоиск по электронной почте find by email.')
        command = ' '.join(input().split())
        if command == 'find by phone number':
            line = find_by_phone_number(contacts_array)
        elif command == 'find by email':
            line = find_by_email(contacts_array)
        elif command == 'find by surname':
            line = find_by_surname(contacts_array)
        elif command == 'find by surname and name':
            line = find_by_surname_and_name(contacts_array)
        elif command == 'find by all':
            line = find_by_all(contacts_array)
        else:
            print('Я не понимаю вашу команду, начните с начала, пожалуйста')
        print('Как вы хотите изменить этот контакт?\nЕсли хотите изменить номер, напишите change number.\nЕсли хотите изменить почту, напишите change email.\nЕсли хотите изменить фамилию, напишите change surname.\nЕсли хотите изменить имя, напишите change name.\nЕсли хотите изменить отчество, напишите change middle name.')
        command = ' '.join(input().split())
        if str(command) == 'change number':
            print('Введите новый номер')
            command = ' '.join(input().split())
            line2 = Contact(line.surname, line.name, line.middle_name, command, line.email)
            contacts_array[contacts_array.index(line)] = line2
            re_write(contacts_array)
            print('Изменения успешно внесены!')
        elif str(command) == 'change email':
            print('Введите новую почту')
            command = ' '.join(input().split())
            line2 = Contact(line.surname, line.name, line.middle_name, line.phone_number, command)
            contacts_array[contacts_array.index(line)] = line2
            re_write(contacts_array)
            print('Изменения успешно внесены!')
        elif str(command) == 'change name':
            print('Введите новое имя')
            command = ' '.join(input().split())
            line2 = Contact(line.surname, command, line.middle_name, line.phone_number, line.email)
            contacts_array[contacts_array.index(line)] = line2
            re_write(contacts_array)
            print('Изменения успешно внесены!')
        elif str(command) == 'change surname':
            print('Введите новую фамилию')
            command = ' '.join(input().split())
            line2 = Contact(command, line.name, line.middle_name, line.phone_number, line.email)
            contacts_array[contacts_array.index(line)] = line2
            re_write(contacts_array)
            print('Изменения успешно внесены!')
        elif str(command) == 'change middle name':
            print('Введите новое отчество')
            command = ' '.join(input().split())
            line2 = Contact(line.surname, line.name, command, line.phone_number, line.email)
            contacts_array[contacts_array.index(line)] = line2
            re_write(contacts_array)
            print('Изменения успешно внесены!')
    else:
        print('Извините, но я Вас не понимаю :(')

    command = ' '.join(input().split())

