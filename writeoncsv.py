from csv import DictWriter

with open('filereader.csv','w',newline='') as wf:
    csv_writer = DictWriter(wf, fieldnames = ['firstnames','lastnames','age'])
    csv_writer.writeheader()


    #writerows and populate fields
    csv_writer.writerow({
        'firstnames': 'PersonA',
        'lastnames': 'Person',
        'age' : 24
    })
    
    csv_writer.writerow({
        'firstnames': 'PersonA',
        'lastnames': 'Person',
        'age' : 24
    })
    
    csv_writer.writerow({
        'firstnames': 'PersonA',
        'lastnames': 'Person',
        'age' : 24
    })
    
    csv_writer.writerow({
        'firstnames': 'PersonA',
        'lastnames': 'Person',
        'age' : 24
    })
    
    csv_writer.writerow({
        'firstnames': 'PersonA',
        'lastnames': 'Person',
        'age' : 24
    })

