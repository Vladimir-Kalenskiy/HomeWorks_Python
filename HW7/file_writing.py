def writing_csv (info):
    file = 'HW/HW7/Phonebook.csv'
    with open (file, 'a') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt (info):
    file = 'HW/HW7/Phonebook.txt'
    with open (file, 'a') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n\n')