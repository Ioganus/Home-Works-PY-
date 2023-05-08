#ОТЛОВ ОШИБКИ С НЕПРАВИЛЬНЫМ ЧИСЛОМ
# try:
#     i = int(input('Введите число:\n'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')

# # СИЛА ВЕТРА
# speed = int(input())
# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class()) #мы просим программу напечатать то, что в скобках

#Проверка логина и пароля
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5

# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)