from os.path import exists
from csv_creating import creating
from user_interface import phone_book

path = 'HW/HW7/Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

phone_book()