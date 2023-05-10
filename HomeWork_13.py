price_sum = 0
while True:
    try:
        tickets = int(input('При регистрации более 3-х человек, скидка на итоговую стоимость 10%\nСколько билетов вы желаете приобрести?\n:'))
        if type(tickets) == int:
            break
    except ValueError:
        print('Пожалуйста, укажите корректное число')
for i in range(tickets):
    i += 1
    while True:
        try:
            tickets_age = int(input(f'Возраст посетителя №{i}? '))
            if tickets_age < 18:
                print('Для лиц до 18 лет билет бесплатный')
            elif 25 > tickets_age >= 18:
                price_sum += 990
                print('От 18 до 25 лет стоимость билета: 990 руб.')
            else:
                price_sum += 1390
                print('От 25 лет стоимость билета: 1390 руб.')
            if type(tickets_age) == int:
                break
        except ValueError:
            print('Пожалуйста, укажите корректное число')
if tickets > 3:
    price_sum = price_sum - ((price_sum / 100) * 10)
    print(f'Итого к оплате {price_sum} руб. с учетом 10%-ой скидки')
else:
    print(f'Итого к оплате {price_sum} руб.')