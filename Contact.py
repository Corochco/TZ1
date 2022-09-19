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
        surname = self.surname
        name = '' if self.name == '' else self.name
        middle_name = '' if self.middle_name == '' else self.middle_name
        phone_number = '' if self.phone_number == '' else self.phone_number
        email = '' if self.email == '' else self.email
        line = str(surname) + ' ' + str(name) + ' '*int(len(str(name))/1000000+0.999999999999) + str(middle_name) + ' '*int(len(str(middle_name))/1000000+0.999999999999) + str(phone_number) *int(len(str(phone_number))/1000000+0.999999999999) + ' '*int(len(str(email))/1000000+0.999999999999) + str(email)
        return line