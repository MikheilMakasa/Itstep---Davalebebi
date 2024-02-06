filter_kenti = lambda x: x % 2 != 0


list1 = [1, 2, 3, 4, 5, 6, 7]


result = list(filter(filter_kenti, list1))

print(result)
