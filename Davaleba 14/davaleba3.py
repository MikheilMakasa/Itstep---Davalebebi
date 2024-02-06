import csv


with open("organizations-100.csv", 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

sorted_data = sorted(data, key=lambda x: int(x['Number of employees']), reverse=False)


with open("sorted_csv.csv", 'w', newline='') as outfile:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_data)


