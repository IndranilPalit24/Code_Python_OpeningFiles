from csv import DictReader
#orderedDict
with open('filereader.csv','r') as f:
    csv_reader = DictReader(f)

    #row order dict
    for row in list(csv_reader):
        print(row['Name'],row['Email'],row['PhoneNo'])