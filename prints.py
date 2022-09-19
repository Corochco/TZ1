def print_hello():
    print('Введите команду (если хотите закрыть приложение, введите close.')
    print('Для вывода всех контактов введите show contacts.')
    print('Для поиска по номеру телефона введите find by phone number.')
    print('Для поиска по электронной почте введите find by email.')
    print('Для поиска по имени введите find by name.')
    print('Для поиска по фамилии введите find by surname. ')
    print('Для поиска по отчеству введите find by middle name.')
    print('Для поиска по фамилии, имени, отчеству введите find by all (пожалуйста пишите фамилию, имя и отчество в порядке, как в этой строке).')
    print('Для поиска по фамилии и имени введите find by surname and name (пожалуйста пишите фамилию и имя в порядке, как в этой строке). ')
    print('Для поиска контактов без номера телефона введите find empty phone number. ')
    print('Для поиска контактов без номера телефона введите find empty email. ')
    print('Для поиска контактов без номера телефона и почты введите find empty email and phone number. ')
    print('Для редактирования контакта введите change contact.')
def which_contact():
    print('Для изменения контакта выберите способ его нахождения. ')
    print('(ниже выберете в зависимости от всех атрибутов контакта, то есть если есть только фамилия, то поиск по фамилии и тп)')
    print('Поиск по фамилии find by surname.')
    print('Поиск по фамилии и имени find by surname and name.')
    print('Поиск по фамилии, имени и отчеству find by all.')
    print('Поиск по номеру телефона find by phone number.')
    print('Поиск по электронной почте find by email. ')
    print('Чтобы вернуться назад напишите back.')
def how_change():
    print('Как вы хотите изменить этот контакт?')
    print('Если хотите изменить номер, напишите change number.')
    print('Если хотите изменить почту, напишите change email.')
    print('Если хотите изменить фамилию, напишите change surname.')
    print('Если хотите изменить имя, напишите change name.')
    print('Если хотите изменить отчество, напишите change middle name.')
    print('Чтобы вернуться назад напишите back.')
