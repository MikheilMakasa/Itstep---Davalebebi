
total_sum = 0

while True:
    user_inp = input("შეიყვანეთ რიცხვი ან 'sum' (რათა მიიღოთ რიცხვების ჯამი): ")

    if user_inp.lower() == 'sum':
        break

    try:
        ricxvi = float(user_inp)
        if ricxvi > 0:
            total_sum += ricxvi
        else:
            print('შეიყვანეთ დადებითი რიცხვი.')

    except ValueError:
        print('გთხოვთ შეიყვანეთ ვალიდური რიცხვი.')

print(f'თქვენი რიცხვების ჯამია: {total_sum}')