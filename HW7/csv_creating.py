
def creating ():
    file = 'HW/HW7/Phonebook.csv'
    with open (file, 'w') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')