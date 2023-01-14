from csv import reader

with open('filereader.csv','r') as f:
    csv_reader = reader(f)
    #print(csv_reader)

    next(csv_reader)
    for row in list(csv_reader):
        print(row)