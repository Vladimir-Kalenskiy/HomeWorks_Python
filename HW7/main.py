from os.path import exists
from csv_creating import creating
# from file_writing import writing_csv
# from file_writing import writing_txt
from user_interface import phone_book

path = 'HW/HW7/Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

phone_book()

# writing_csv()
# writing_txt()