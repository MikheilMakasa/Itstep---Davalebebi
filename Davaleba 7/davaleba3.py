def shebruneba(str):

    if len(str) <= 1:
        return str
    else:
        return str[-1] + shebruneba(str[:-1])


test= "Hello"
shedegi = shebruneba(test)

print(f'სტრიქონის "{test}" შებრუნებული სტრიქონია: {shedegi}')