import tkinter as tk
from copy import deepcopy
from datetime import datetime

import airport as airport
import funciones as funciones
import grafo_class as grafo
import lecturaData as lectura

data_crude=lectura.lectura_data()

list_airport=[]

for airport_data in data_crude:
    created=airport.airport(airport_data[0],airport_data[1],airport_data[2],airport_data[3],airport_data[4],airport_data[5])
    list_airport.append(created)

data={}

h={}



for index in range(200):  #NUMERO DE NODOS A UTILIZAR
    data[index]=list_airport[index]

mygraf=grafo.G(data=data,dirigido=True)
mygraf_not=deepcopy(mygraf)
for index in range(len(data)):
    h[index]=1

adjlist={}
adjlist_2={}

relation=funciones.CreateRelation(data)
funciones.Create_edges(mygraf,mygraf_not,data,relation,adjlist,adjlist_2)


mygraf.set_h_adj_list(h,adjlist)
mygraf_not.set_h_adj_list(h,adjlist_2)

class Aplication():
    
    LetraH1=40
    LetraH2=36
    LetraH3=32
    LetraH4=28
    LetraP=14
    Data={}
    Recursos=[]
    colores=["#000004","#1b2141","#404884","#6e75d1","#a3a6ff"]
    sizeInicio="1600x900+140+60"
    Fuente="Cascadia Code"
    Airport=None
    now_3=datetime.now().hour
    now_8=datetime.now().hour
    ###########################################################
    ##recursos
    
    def LoadData(self):
        self.Data=data
    
    def LoadRecursos(self):
        self.logo=tk.PhotoImage(file="img/Recurso_1.png")
        

    
    def LoadGrafo(self):
        self.grafo=mygraf
        self.grafo_not=mygraf_not
        self.grafo.floyd_warshall()
        self.grafo_not.floyd_warshall()
        self.relation=relation

    def ReloadRelation(self):
        self.relation=funciones.CreateRelation(self.Data)

    def ReloadEdges(self):
        self.adjlist={}
        self.adjlist_2={}
        funciones.Create_edges(self.grafo,self.grafo_not,self.Data,self.relation,self.adjlist,self.adjlist_2)
    
    ###########################################################
    ## inicio aplicacion

    def __init__(self) -> None:
        self.root=tk.Tk()
        self.LoadData()
        self.LoadRecursos()
        self.LoadGrafo()
        #####INICIO######
        self.Inicio_script()
        actual=datetime.now().hour
        
        if abs(self.now_3-actual)>3:
            self.grafo.set_matrix()
            self.adjlist={}
            self.adjlist_2={}

            funciones.Create_edges(self.grafo,self.grafo_not,self.Data,self.relation,adjlist,self.adjlist_2)
            self.grafo.set_h_adj_list(h,self.adjlist)
            self.grafo_not.set_h_adj_list(h,self.adjlist_2)
            
            self.grafo_not.floyd_warshall()
            self.grafo.floyd_warshall()
            
            self.now_3=datetime.now().hour
        
        if abs(self.now_8-actual)>8:
            self.relation=funciones.CreateRelation(data)
           
            self.grafo.set_matrix()
            self.adjlist={}
            self.adjlist_2={}

            funciones.Create_edges(self.grafo,self.grafo_not,self.Data,self.relation,self.adjlist,self.adjlist_2)
            self.grafo.set_h_adj_list(h,self.adjlist)
            self.grafo_not.set_h_adj_list(h,self.adjlist_2)
            
            self.grafo.floyd_warshall()
            self.grafo_not.floyd_warshall()
            
            self.now_3=datetime.now().hour

        self.root.mainloop()
    ####################################################################
    def inicio_Properties(self):
        self.root.title("FlyShip")    
        self.root.option_add('*tearOff', False) 
        self.root.geometry(self.sizeInicio)
        self.root.resizable(False,False)

    def inicio_estilo(self):
        self.root.iconbitmap("img/Red_Hat_logo.ico")
        self.root.config(background=self.colores[1])

    def inicio_widgets(self):

        self.logo_lb=tk.Label(self.root,image=self.logo)
        self.entrada=tk.StringVar()
        self.entrada.set("00AA")
        self.buton_text=tk.StringVar()
        self.buton_text.set("Inciar Sesion")
        self.entrada_box=tk.Entry(self.root,textvariable=self.entrada)
        self.entrada_buton=tk.Button(self.root,textvariable=self.buton_text)
        self.label_ingreso=tk.Label(self.root,text="ingrese el codigo del aeropuerto")
        self.titulo_projecto=tk.Label(self.root,text="SkyShip")
        self.buton_creditos=tk.Button(self.root,text="Creditos")
    
     
    def inicio_grid(self):
        self.titulo_projecto.grid(row=1,column=0,sticky='')
        self.logo_lb.grid(row=2,column=0,sticky='')
        self.label_ingreso.grid(row=3,column=0,sticky='')
        self.entrada_box.grid(row=4,column=0,sticky='')
        self.entrada_buton.grid(row=5,column=0,sticky='')
        self.buton_creditos.grid(row=6,column=0,sticky='')

    def inicio_widgets_estilo(self):
        self.logo_lb.config(background=self.colores[1])
        self.titulo_projecto.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH1))
        self.label_ingreso.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH2))
        self.entrada_box.config(background=self.colores[2],foreground=self.colores[1],font=(self.Fuente,self.LetraH2),border=0)
        self.entrada_buton.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH2),border=0)
        self.buton_creditos.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH2),border=0)

    def inicio_Widgets_Funcionalities(self):
        self.entrada_buton.config(command=lambda:self.RunHome())
        self.buton_creditos.config(command=lambda:self.Creditos_script())


    def isCorrectCodeUser(self,code):
        resultado=False
        self.index=-1
        for i in range(len(self.Data)) :
            if code == self.Data[i].pident:
                self.index=i
                resultado=True

        return resultado

    def RunHome(self):

        if self.isCorrectCodeUser(self.entrada_box.get()):
            self.User=deepcopy(self.index)
            self.Airport=self.Data[self.User]
            self.Home_script()



    

    #######################################################################
    ##HOME###

    def HomeProperties(self):
        self.Home=tk.Toplevel()
        self.Home.geometry(self.sizeInicio)
        self.Home.resizable(0,0)
        self.Home.transient(master=self.root)
        self.Home.grab_set()
        self.Home.title("Home")

    def Home_estilo(self):
        self.Home.iconbitmap("img/Red_Hat_logo.ico")
        self.Home.config(background=self.colores[1])
    
    def Home_widegts(self):

        self.TitleHome=tk.Label(self.Home,text="INICIO")
        self.CodeUser=tk.Label(self.Home,text="CODIGO: "+str(self.Airport.pident))
        self.NameAirportUser=tk.Label(self.Home,text="NOMBRE DE AEROPUERTO: "+str(self.Airport.name))
        self.RegionUser=tk.Label(self.Home,text="REGION: "+str(self.Airport.municipality))
        self.UbicationAiportUser=tk.Label(self.Home,text="UBCACION")
        self.UbicactionLatitudAiportUser=tk.Label(self.Home,text="LATITUD: "+str(self.Airport.latitude))
        self.UbicactionLongitudAiportUser=tk.Label(self.Home,text="LONGITUD: "+str(self.Airport.longitude))
        self.UbicactionAlturaAiportUser=tk.Label(self.Home,text="ALTURA: "+str(self.Airport.elevation))

        self.Button_Algorithms=tk.Button(self.Home,text="Algoritmos")
        self.Button_Salir=tk.Button(self.Home,text="Salir")
    
    def Home_widgets_estilo(self):
        self.TitleHome.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH1))
        self.CodeUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.NameAirportUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.RegionUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.UbicationAiportUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.UbicactionLatitudAiportUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.UbicactionLongitudAiportUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
        self.UbicactionAlturaAiportUser.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))

        self.Button_Algorithms.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH3),border=0)
        self.Button_Salir.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH3),border=0)
        
    def Home_grid(self): 
        self.TitleHome.grid(row=0,column=0,sticky='w')
        self.CodeUser.grid(row=1,column=0,sticky='w')
        self.NameAirportUser.grid(row=2,column=0,sticky='w')
        self.RegionUser.grid(row=4,column=0,sticky='w')
        self.UbicationAiportUser.grid(row=3,column=0,sticky='w')
        self.UbicactionLatitudAiportUser.grid(row=5,column=0,sticky='w')
        self.UbicactionLongitudAiportUser.grid(row=6,column=0,sticky='w')
        self.UbicactionAlturaAiportUser.grid(row=7,column=0,sticky='w')

        self.Button_Algorithms.grid(row=8,column=0,sticky='')
        self.Button_Salir.grid(row=9,column=0,sticky='')
    
    def Home_Widgets_Funcionalities(self): 
        self.Button_Salir.config(command=self.Home.destroy)
        self.Button_Algorithms.config(command=lambda:self.Algorithms_script())

    def OpenHome(self):
        self.Home_script()
        self.root.wait_window(self.Home)
    
    
    #######################################################################
    
    
    ##Algorithms###
    
    def AlgorithmsProperties(self):
        self.Algorithms=tk.Toplevel()
        self.Algorithms.geometry(self.sizeInicio)
        self.Algorithms.resizable(0,0)
        self.Algorithms.transient(master=self.root)
        self.Algorithms.grab_set()
        self.Algorithms.title("Algorithms")

    def Algorithms_estilo(self):
        self.Algorithms.iconbitmap("img/Red_Hat_logo.ico")
        self.Algorithms.config(background=self.colores[1])

    def Algorithms_widegts(self):
        self.Rutas_label=tk.Label(self.Algorithms,text="Realizar mas corta ruta a: ")
        self.Ruta_entry=tk.Entry(self.Algorithms)
        self.Ruta_button=tk.Button(self.Algorithms,text="iniciar algoritmo")
        self.Rutas_Convexa_label=tk.Label(self.Algorithms,text="Dame la distancia hasta mi destino: ")
        self.Rutas_Convexa_buton=tk.Button(self.Algorithms,text="iniciar algoritmo")
        
        
         
        self.Resultado=tk.Frame(self.Algorithms)
        self.Button_Salir_algorithms=tk.Button(self.Algorithms,text="Salir")
    
 
    def Algorithms_grid(self):
        self.Rutas_label.grid(row=0,column=0,sticky='w')
        self.Ruta_entry.grid(row=1,column=0,sticky='w')
        self.Ruta_button.grid(row=2,column=0,sticky='w')

        self.Rutas_Convexa_label.grid(row=3,column=0,sticky='w')
        self.Rutas_Convexa_buton.grid(row=4,column=0,sticky='w')
        self.Resultado.grid(row=6,column=0)
        self.Button_Salir_algorithms.grid(row=1,column=2,sticky='w')
    
    def Algorithms_widgets_estilo(self):
        self.Rutas_label.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.Ruta_entry.config(background=self.colores[2],foreground=self.colores[4],font=(self.Fuente,self.LetraH4),border=0)
        self.Ruta_button.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH4,),border=0)
        self.Rutas_Convexa_label.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.Rutas_Convexa_buton.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH4),border=0)
        self.Button_Salir_algorithms.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH4),border=0)

    
    def Algorithms_Widgets_Funcionalities(self):
        self.Ruta_minima=tk.Label(self.Resultado)
        self.Ruta_minima_2=tk.Label(self.Resultado)
        self.Texto=tk.Label(self.Resultado)
        self.Texto_v2=tk.Label(self.Resultado)
        
        self.accident=tk.PhotoImage(file="img/accident.png")
        self.rain=tk.PhotoImage(file="img/rain.png")
        self.snow=tk.PhotoImage(file="img/snow.png")
        self.torment=tk.PhotoImage(file="img/torment.png")
        
        self.accident_img=tk.Label(self.Resultado)
        
        self.show=tk.Label(self.Resultado)
        
        self.Ruta_button.config(command=lambda:self.Algorithm_Ruta_Minima())
        self.Rutas_Convexa_buton.config(command=lambda:self.Algorihm_Distancia_Minima())
        self.Button_Salir_algorithms.config(command=self.Algorithms.destroy)        

    def OpenAlgorithms(self):
        self.Algorithms_script()
        self.Home.wait_window(self.Algorithms)

    def Algorithm_Ruta_Minima(self):
        if self.isCorrectCodeUser(self.Ruta_entry.get()):

            self.Ruta_minima.destroy()
            self.Texto.destroy()
            self.Texto_v2.destroy()
            self.show.destroy()
            self.Ruta_minima_2.destroy()
            self.accident_img.destroy()
            i=deepcopy(self.index)
            
            Ruta=self.grafo.a_star_algorithm(self.User,i)
            Ruta_2=self.grafo_not.a_star_algorithm(self.User,i)
            L=[]
            L_2=[]
            for i in Ruta:
                L.append(self.Data[i].pident)
            for i in Ruta_2:
                L_2.append(self.Data[i].pident)

            val=data[i].get_df()
            

            
            strL=" -> ".join(L)
            strL_2=" -> ".join(L_2)
        
            if Ruta!=False:
                
                self.Texto=tk.Label(self.Resultado,text="La ruta principal es ....")
                self.Texto=tk.Label(self.Resultado,text="La ruta alterna debido a los problemas es ....")
                self.Ruta_minima=tk.Label(self.Resultado,text=strL)
                self.Ruta_minima_2=tk.Label(self.Resultado,text=strL_2)
                if val < 0.25 :
                    self.accident_img=tk.Label(self.Resultado,self.rain)
                elif 0.25 <=val and val<0.50 :
                    self.accident_img=tk.Label(self.Resultado,self.torment)
                elif 0.50 <=val and val<0.75 :
                    self.accident_img=tk.Label(self.Resultado,self.snow)
                elif 0.75 <=val and val<1.00 :
                    self.accident_img=tk.Label(self.Resultado,self.accident)
            else:
                self.Ruta_minima=tk.Label(self.Resultado,text="No existe ruta!")
                self.Ruta_minima_2=tk.Label(self.Resultado,text="")
                
            self.logo_lb.config(background=self.colores[1])
            self.Ruta_minima.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
            self.Ruta_minima_2.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
            
            self.Texto.grid(row=0,column=0)
            self.Texto_v2.grid(row=2,column=0)
            self.Ruta_minima.grid(row=1,column=0)
            self.Ruta_minima_2.grid(row=3,column=0)
            self.accident_img.grid(row=4,column=0)


    def Algorihm_Distancia_Minima(self):
        
        if self.isCorrectCodeUser(self.Ruta_entry.get()):
            i=deepcopy(self.index)
            self.show.destroy()
            self.Ruta_minima.destroy()

            if  self.grafo.distance[self.User][i] != False:
                self.show=tk.Label(self.Resultado,text="El recorrido es de "+str(self.grafo.distance[self.User][i])+" Km")
                self.show.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraP))
                self.show.grid(column=0,row=0)


    ###################################################
    def Creditos_Properties(self):
        self.Creditos=tk.Toplevel()
        self.Creditos.geometry(self.sizeInicio)
        self.Creditos.resizable(0,0)
        self.Creditos.transient(master=self.root)
        self.Creditos.grab_set()
        self.Creditos.title("Creditos")

    def Creditos_estilo(self):
        self.Creditos.iconbitmap("img/Red_Hat_logo.ico")
        self.Creditos.config(background=self.colores[1])

    def Creditos_widgets(self):
        self.GrupoFrameIntegrantes=tk.Frame(self.Creditos)
        self.Integrantes1=tk.Label(self.GrupoFrameIntegrantes,text="Matthew David Tello Salas U202021443")
        self.Integrantes2=tk.Label(self.GrupoFrameIntegrantes,text="Joseph Ramirez Sarmiento U20211C828")
        self.Integrantes3=tk.Label(self.GrupoFrameIntegrantes,text="Luna Morales Gianfranco U201824343")
        self.Profesora=tk.Label(self.GrupoFrameIntegrantes,text="Ing. Patricia Reyes Silva")
        self.buton_close_creditos=tk.Button(self.Creditos,text="Salir")
        #----------------------------------
    
     
    def Creditos_grid(self):
        self.GrupoFrameIntegrantes.grid(row=0,column=0)
        self.Integrantes1.grid(row=0,column=0)
        self.Integrantes2.grid(row=1,column=0)
        self.Integrantes3.grid(row=2,column=0)
        self.Profesora.grid(row=3,column=0)
        self.buton_close_creditos.grid(row=1,column=0)
        
    def Creditos_widgets_estilo(self):
        self.GrupoFrameIntegrantes.config(background=self.colores[1])
        self.Integrantes1.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.Integrantes2.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.Integrantes3.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.Profesora.config(background=self.colores[1],foreground=self.colores[4],font=(self.Fuente,self.LetraH4))
        self.buton_close_creditos.config(background=self.colores[3],foreground=self.colores[4],font=(self.Fuente,self.LetraH4),border=0)

    def creditos_Widgets_Funcionalities(self):
        self.buton_close_creditos.config(command=self.Creditos.destroy)        


    ###################################################
    def Inicio_script(self):
        self.inicio_Properties()
        self.inicio_estilo()
        self.inicio_widgets()
        self.inicio_widgets_estilo()
        self.inicio_grid()
        self.inicio_Widgets_Funcionalities()
    
    def Home_script(self):
        self.HomeProperties()
        self.Home_estilo()
        self.Home_widegts()
        self.Home_widgets_estilo()
        self.Home_estilo()
        self.Home_grid()
        self.Home_Widgets_Funcionalities()

    def Algorithms_script(self):
        self.AlgorithmsProperties()
        self.Algorithms_estilo()
        self.Algorithms_widegts()
        self.Algorithms_widgets_estilo()
        self.Algorithms_grid()
        self.Algorithms_Widgets_Funcionalities()
    
    def Creditos_script(self):
        self.Creditos_Properties()
        self.Creditos_estilo()
        self.Creditos_widgets()
        self.Creditos_widgets_estilo()
        self.Creditos_grid()
        self.creditos_Widgets_Funcionalities()



if __name__=='__main__':
    Interfaz=Aplication()