import csv


with open('titanic.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    header = reader.fieldnames

    survived = [row for row in reader if row['Survived'] == '1']


with open('survived.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    
    writer.writeheader()
    writer.writerows(survived)


