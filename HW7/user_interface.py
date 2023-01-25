from file_writing import writing_csv
from file_writing import writing_txt

def phone_book():
    choise_user = 0
    while choise_user == 0:

        print('Телефонный справочник.')
        choise_user = int(input('\nВыберите действие: \
                                \n1 - Добавить контакт.\
                                \n2 - Вывести в консоль весь список.\
                                \n3 - Закрыть справочник.\
                                \nВаш выбор: '))
        
        if choise_user == 1:
            get_info()
            choise_user = 0
            
        elif choise_user == 2:
            choise_user = int(input('\nВ каком виде вывести список: \
                                    \n1 - Имя, Фамилия, Номер телефона, Описание.\
                                    \n2 - Имя\n    Фамилия\n    Номер телефона\n    Описание\n    ----------\
                                    \nВаш выбор: \n'))
            if choise_user == 1:
                with open('HW/HW7/Phonebook.csv', 'r') as pb:
                    print(*pb)
            else:
                with open('HW/HW7/Phonebook.txt', 'r') as pb:
                    print(*pb)
            choise_user = 0
        else:
            break


def get_info ():
    info = []

    last_name = input('Введите фамилию: ')
    info.append(last_name)

    first_name = input('Введите имя: ')
    info.append(first_name)

    phone_number = input('Введите номер телефона: ')
    phone_number = int(phone_number)
    info.append(phone_number)

    description = input('Введите описание: ')
    info.append(description)
    writing_txt(info)
    writing_csv(info)

    return info
