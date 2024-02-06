import random

def random_listi(size=100):
    return [random.randint(1, 1000) for _ in range(size)]

def bubble_sort(list):
    
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
        pivotze_naklebi = [x for x in list if x <= pivot]
        pivoteze_meti = [x for x in list if x > pivot]
        return quick_sort(pivoteze_meti) + [pivot] + quick_sort(pivotze_naklebi)


test_listi = random_listi()


zrdadobit = bubble_sort(test_listi.copy())
klebadobit = quick_sort(test_listi.copy())


print("საწყისი ლისტი:")
print(test_listi)
print("\nზრდადობით დალაგებული (Bubble Sort):")
print(zrdadobit)
print("\nკლებადობით დალაგებული  (Quick Sort):")
print(klebadobit)
