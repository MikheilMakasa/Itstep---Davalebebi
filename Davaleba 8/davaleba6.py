def daboloebit_gafiltvra(input_list, daboloeba):
    try:
        
        result = list(filter(lambda x: x.endswith(daboloeba), input_list))
        return result
    except TypeError:
        print("Error: Please provide a list of strings and a string for ending.")


testing_list = ['hello', 'world', 'coding', 'nod']
daboloeba = 'ing'


shedegi = daboloebit_gafiltvra(testing_list, daboloeba)
print(shedegi)
