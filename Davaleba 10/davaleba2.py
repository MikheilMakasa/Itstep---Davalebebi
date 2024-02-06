
def linear_search(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

def samis_jeradebis_indeqsebi(list, lambda_fun):
    indeqsebis_listi = []

    for element in list:
        if lambda_fun(element):
            index = linear_search(list, element)
            indeqsebis_listi.append(index)

    return indeqsebis_listi



test_list = [1, 3, 12, 5, 9, 8, 15, 18, 23, 28]


samis_jeradi = lambda x: x % 3 == 0


shedegi = samis_jeradebis_indeqsebi(test_list, samis_jeradi)

print("საწყისი ლისტი:", test_list)
print("სამის ჯერადი ელემენტების ინდექსების ლისტი:", shedegi)
