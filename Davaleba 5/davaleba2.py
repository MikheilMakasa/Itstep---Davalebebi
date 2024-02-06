import random


random_ricxvebi = []

for n in range(10):
    random_ricxvebi.append(random.randint(0,1000))


umciresi = min(random_ricxvebi)
udidesi = max(random_ricxvebi)


print(f'შემთხვევითი რიცხვების ლისტია: {random_ricxvebi}')
print(f'უმცირესი რიცხვია: {umciresi}')
print(f'უდიდესი რიცხვია: {udidesi}')