monitor_price = float(input('შეიყვანეთ თქვენი მონიტორის ფასი(ლარი): '))
system_unit_price = float(input('შეიყვანეთ თქვენი სისტემური ბლოკის ფასი(ლარი): '))
keyboard_price = float(input('შეიყვანეთ თქვენი კლავიატურის ფასი(ლარი): '))
mouse_price = float(input('შეიყვანეთ თქვენი მაუსის ფასი(ლარი): '))

computer_price = monitor_price + system_unit_price + keyboard_price + mouse_price

print(f'თქვენი კომპიუტერის საერთო ფასი შეადგენს: {computer_price} ლარს.')