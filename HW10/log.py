id_user = None
input_data = None
result = None

def get_id_user(num_id):      # Получение ID пользователя.
    global id_user
    id_user = num_id

def get_input_data(data):     # Получение введеного пользователем примера
    global input_data
    input_data = data


def get_result(res):          # Получение результата примера от пользователя
    global result
    result = res

def save_log():               # Запись данных в log
    with open('HW/HW10/log_file.txt', 'a') as f:
        f.writelines(f'ID user: {id_user}, Input: {input_data}, Result: {result}\n')


