def cifrebis_jami(num):
    if num < 10:
        return num
    else:
       
        return num % 10 + cifrebis_jami(num // 10)

# Example usage:
ricxvi = 12345
shedegi = cifrebis_jami(ricxvi)

print(f"რიცხვის {ricxvi} ციფრების ჯამია: {shedegi}")