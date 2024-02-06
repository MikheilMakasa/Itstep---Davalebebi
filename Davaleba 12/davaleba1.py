def dictatori(text):
    sityvebi = text.split()
    sityvis_dict = {}

    for sityva in sityvebi:
       
        sityva = sityva.strip('.,?!')
        sityva = sityva.lower()

        if sityva in sityvis_dict:
            sityvis_dict[sityva] += 1
        else:
            sityvis_dict[sityva] = 1

    return sityvis_dict


user_text = input("შეიყვანეთ წინადადება: ")
shedegi = dictatori(user_text)

print(shedegi)