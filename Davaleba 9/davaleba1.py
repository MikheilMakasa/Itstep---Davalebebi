import random

def random_listi():
   
    random_listi = [random.randint(1, 1000) for _ in range(100)]

    zrdadobit = sorted(random_listi)

    klebadobit = sorted(random_listi, reverse=True)

    return zrdadobit, klebadobit


zrdadobit, klebadobit = random_listi()

print("ზრდადობით დალაგებული:", zrdadobit)
print("კლებადობით დალაგებული:", klebadobit)
