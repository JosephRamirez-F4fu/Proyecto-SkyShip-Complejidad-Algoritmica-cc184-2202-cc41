
import math as mt
import random

import numpy as np


def distance_per_aiports(punto_1,punto_2):
    """ Funcion que retorna la distancie entre dos puntos geografica en funcion de su latitud y longitud"""
    punto_1 = (np.radians(punto_1[0]), np.radians(punto_1[1]))
    punto_2 = (np.radians(punto_2[0]), np.radians(punto_2[1]))
    distancia = mt.acos(np.sin(punto_1[0])*np.sin(punto_2[0]) + np.cos(punto_1[0])*np.cos(punto_2[0])*np.cos(punto_1[1] - punto_2[1]))
    return distancia * 6371.0


def search_on_dict(mydict,code):
    aeropuertos=list(mydict.values())
    for i in aeropuertos:
        if i.pident==code:
            return i
    return False



def CreateRelation(data):
    relation=[]
    
    for i in range(len(data)):
        vedge=[]
        for j in range(2):
            redge=random.choice(list(data.keys()))
            if i!=redge:
                vedge.append(redge)
        vedge=set(vedge)
        vedge=list(vedge)
        relation.append(vedge)

    return relation

def Create_edges(mygraf,data,relation,adjac_lis):
    for i in range(len(relation)):
        l=[]
        for j in range(len(relation[i])):
            distance=round(distance_per_aiports(data[i].position(),data[relation[i][j]].position()),2)
            promdifij=1+(data[i].get_df()+data[relation[i][j]].get_df())/2
            mygraf.add_edge(i,relation[i][j],distance*promdifij)
            l.append((relation[i][j],distance*promdifij))
        adjac_lis[i]=l
            

adjac_lis = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}