pirveli_ricxvi = float(input('შეიყვანეთ პირველი რიცხვი: '))
meore_ricxvi = float(input('შეიყვანეთ მეორე რიცხვი: '))
operatori = input('შეიყვანეთ მათემატიკური ოპერატორი(+, -, *, /): ')

if operatori == '+':
    print(pirveli_ricxvi + meore_ricxvi)
elif  operatori == '-':
    print(pirveli_ricxvi - meore_ricxvi)   
elif  operatori == '*':
    print(pirveli_ricxvi * meore_ricxvi)
elif  operatori == '/':
    if meore_ricxvi != 0:
        print(pirveli_ricxvi / meore_ricxvi) 
    else:
        print('ნულზე გაყოფა არ შეიძლება')
else:
    print ('შეიყვანეთ სწორი მათემატიკური ოპერატორი.')     