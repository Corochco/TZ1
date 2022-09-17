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

#приветственное сообщение и первая команда(в приведственном сообщении распишем все команды
print('Введите команду (если хотите закрыть приложение, введите close. \nДля вывода всех контактов введите show contacts. \nДля поиска по номеру телефона введите find by phone number. \nДля поиска по электронной почте введите find by email. \nДля поиска по имени введите find by name. \nДля поиска по фамилии введите find by surname. \nДля поиска по отчеству введите find by middle name. \nДля поиска по фамилии, имени, отчеству введите find by all (пожалуйста пишите фамилию, имя и отчество в порядке, как в этой строке). \nДля поиска контактов без номера телефона введите find empty phone number. \nДля поиска контактов без номера телефона введите find empty email. \nДля поиска контактов без номера телефона и почты введите find empty email and phone number.')
command = ' '.join(input().split())

#"сердце" программы
while command != 'close':
    # считываем базу и передаем в массив contacts_array
    contacts_array = show_contacts()
    if command == 'show contacts':
        for i in contacts_array:
            print(i.pyout())
    elif command == 'find by phone number':
        b = False
        command = ' '.join(input().split())
        for i in contacts_array:
            if str(i.get_phone_number()) == str(command):
                print(i.pyout())
                b = True
                break
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find by email':
        b = False
        command = ' '.join(input().split())
        for i in contacts_array:
            if str(i.get_email()) == str(command):
                print(i.pyout())
                b = True
                break
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find by name':
        b = False
        command = ' '.join(input().split())
        for i in contacts_array:
            if str(i.get_name()) == str(command):
                print(i.pyout())
                b = True
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find by surname':
        b = False
        command = ' '.join(input().split())
        for i in contacts_array:
            if str(i.get_surname()) == str(command):
                print(i.pyout())
                b = True
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find by middle name':
        b = False
        command = ' '.join(input().split())
        for i in contacts_array:
            if str(i.get_middle_name()) == str(command):
                print(i.pyout())
                b = True
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find by all':
        b = False
        surname, name, middle_name = map(str, input().split())
        for i in contacts_array:
            if str(i.get_surname()) == str(surname) and str(i.get_name()) == str(name) and str(i.get_middle_name()) == str(middle_name):
                print(i.pyout())
                b = True
        if not b:
            print('Извините, но по вашему запросу контактов не найдено')
    elif command == 'find empty phone number':
        b = False
        for i in contacts_array:
            if str(i.get_phone_number()) == '':
                print(i.pyout())
                b = True
        if not b:
            print('У всех контактов заполнены номера телефонов')
    elif command == 'find empty email':
        b = False
        for i in contacts_array:
            if str(i.get_email()) == '':
                print(i.pyout())
                b = True
        if not b:
            print('У всех контактов заполнены номера телефонов')
    elif command == 'find empty email and phone number':
        b = False
        for i in contacts_array:
            if str(i.get_email()) == '' and str(i.get_phone_number()) == '':
                print(i.pyout())
                b = True
        if not b:
            print('У всех контактов заполнены номера телефонов')
    else:
        print('Извините, но я Вас не понимаю7')

    command = ' '.join(input().split())

