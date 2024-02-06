import random

def random_listi():
    return [random.randint(1, 1000) for _ in range(100)]

def linear_search(list, element):
    for i in range (len(list)):
        if list[i] == element:
            return i
    return -1

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def binary_search(list, item):
    begin_index = 0
    end_index = len(list) - 1
   
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = list[midpoint]

        if midpoint_value == item:
            return midpoint
        elif midpoint_value < item:
            begin_index = midpoint + 1
        else:
            end_index = midpoint - 1

    return None


test_list = random_listi()


sadziebo_elementi = random.choice(test_list)


linear_search_shedegi = linear_search(test_list, sadziebo_elementi)


sortirebuli_listi = bubble_sort(test_list.copy())


binary_search_shedegi = binary_search(sortirebuli_listi, sadziebo_elementi)


print("საწყისი ლისტი: ", test_list)
print("\nსაძიებო ელემენტი:", sadziebo_elementi)
print("\nწრფივი ძიების შედეგი - საძიებო ელემენტის ინდექსია:", linear_search_shedegi) if linear_search_shedegi != -1 else print("ელემენტი ვერ იქნა ნაპოვნი.")
print("\nსორტირებული ლისტი (Bubble Sort): ", sortirebuli_listi)
print("\nბინარული ძიების შედეგი - საძიებო ელემენტის ინდექსია:", binary_search_shedegi) if binary_search_shedegi != -1 else print("ელემენტი ვერ იქნა ნაპოვნი.")


    