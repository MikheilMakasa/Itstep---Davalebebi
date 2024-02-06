import csv

with open('organizations-100.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    original_headers = reader.fieldnames

    ssl_companies = [
        {
            'Organization Id': row['Organization Id'],
            'Name': row['Name'],
            'Website': row['Website'],
            'Industry': row['Industry'],
            'Number of employees': row['Number of employees']
        }
        for row in reader if row['Website'].startswith('https://')
    ]

selected_headers = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']


with open('ssl_companies.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=selected_headers)
    
  
    writer.writeheader()
    writer.writerows(ssl_companies)
