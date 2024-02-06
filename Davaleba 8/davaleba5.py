from functools import reduce

def gadamravleba(input_list):
    try: 
        shedegi = reduce(lambda x, y: x * y, input_list)
        return shedegi
    except TypeError:
        print("შეცდომა: გთხოვთ შეიყვანოთ რიცხვების ლისტი.")


ricxvebi = [1, 2, 3, 4, 5]


shedegi = gadamravleba(ricxvebi)
print(shedegi)
