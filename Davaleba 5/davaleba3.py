import copy

my_list = [43, '22', 12, 66, 210, ["hi"]]

# a
index_of_210 = my_list.index(210)
print(f'210-ის ინდექსია: {index_of_210}')

# b
my_list[-1].append('hello')

# c
my_list.pop(2)
print(my_list)

# d
my_list_2= copy.deepcopy(my_list)
my_list_2.clear()

print(f'my_list:{my_list} \nmy_list_2: {my_list_2}')