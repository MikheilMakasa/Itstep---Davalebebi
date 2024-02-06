text = input('შეიყვანეთ თქვენი სიტყვა: ')

lower = text.lower()

gaertianebuli =''.join(lower.split())

shebrunebuli = gaertianebuli[::-1]


if gaertianebuli == shebrunebuli:
    print('შეყვანილი ტექსტი არის პალინდრომი')
else: 
    print('შეყვანილი ტექსტი არ არის პალინდრომი')


