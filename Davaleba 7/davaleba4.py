def factoriali(n):
    if n == 0 or n == 1:
        return 1
    else:
       
        return n * factoriali(n - 1)


ricxvi = 5
shedegi = factoriali(ricxvi)

print(f'რიცხვის "{ricxvi}" ფაქტორიალია: {shedegi}')