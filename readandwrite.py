from csv import DictReader, DictWriter

with open('filereader.csv', 'r') as rf:
    with open('filereader.csv','w') as wf:
        
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames = ['firstnames', 'lastnames','age'])
        csv_writer.writeheader()


        for row in csv_reader:
            fname, lname, age = row['firstnames'],row['lastnames'],row['age']

            csv_writer.writerow({
                'firstnames':fname.upper(),
                'lastnames' :lname.upper(),
                'age'       :age.upper()
            })