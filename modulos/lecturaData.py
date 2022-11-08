import csv


def lectura_data():
    with open('airports_formated.csv') as f:
        reader = csv.reader(f)
        all_airport=[]
        for row in reader:
            data=row[0].split(";")
            data_airport=[data[3],data[1],round(float(data[4]),3),round(float(data[5]),3),round(float(data[6]),3),data[7]]
            all_airport.append(data_airport)
    return all_airport
