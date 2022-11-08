import random
from datetime import datetime


class airport: 
    def __init__(self,pname,pident,latitude_deg,longitude_deg,elevation_ft,municipality):
        """"nombre 3, codigo 1, latitud 4, longitud 5, elevation 6, region 7"""
        self.name= pname
        self.pident=pident
        self.latitude= round(latitude_deg,3)
        self.longitude= round(longitude_deg,3)
        self.elevation= round(elevation_ft/3.28084,3)
        self.municipality= municipality

        self.df={}
        for i in range(23):
            self.df[i]=(random.randint(1,12))/12
        

    def get_df(self):
        now=datetime.now()
        return self.df[now.hour]

    def position(self):
        return [self.latitude,self.longitude]
    
    def __repr__(self):
        return "Objeto " +self.name

def create_airports(Data):
    Airport_list=[]
    for i in Data:
        Airport_list.append(airport(i[0],i[1],i[2],i[3],i[4],i[5]))
    return Airport_list

def create_data_dict_key(Allairports):
    mydict={}
    for i in range(len(Allairports)):
        mydict[i]=Allairports[i]   
    return mydict

def create_data_dict_values(Allairports):
    mydict={}
    for i in range(len(Allairports)):
        mydict[Allairports[i]]=i

    return mydict 