def mimateba(num1, num2):
    return num1 + num2

def gamokleba(num1, num2):
    return num1 - num2

def gamravleba(num1, num2):
    return num1 * num2

def gayofa(num1, num2):
    if num2 == 0:
        return "0-ზე გაყოფა არ შეიძლება."
    return num1 / num2

try:
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    operatori = input("შეიყვანეთ მათემატიკური ოპერატორი (+, -, *, /): ")

    operatorebi = {
        '+': mimateba,
        '-': gamokleba,
        '*': gamravleba,
        '/': gayofa
    }

    if operatori in operatorebi:
        operation = operatorebi[operatori]
        shedegi = operation(num1, num2)
        print(f"შედეგი: {shedegi}")
    else:
        print("შეიყვანეთ სწორი ოპერატორი")

except ValueError:
    print("შეიყვანეთ ვალიდური რიცხვი")
