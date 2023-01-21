# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

list1 = [12,'sadf',5643]

# List comprehension
list_str = [el for el in list1 if type(el) == str]
list_num = [el for el in list1 if type(el) == int]

# Filter
# list_str = list(filter(lambda el: type(el) == str, list1))
# list_num = list(filter(lambda el: type(el) == int, list1))

print(list_str, list_num)