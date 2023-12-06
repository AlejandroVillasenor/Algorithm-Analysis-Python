# -*- coding: utf-8 -*-
"""
Tarea 7. Interfaz con tkinter
"""
from tkinter import * #Libreria para la interfaz grafica
import re #Libreria para expresiones regulares
class aplicacion():
    def __init__(self):
        #Ventana
        self.raiz = Tk()
        self.raiz.geometry('600x400')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Expresiones Regulares')
        label = Label(self.raiz, text="Validacion de expresiones regulares")
        label.pack(side=TOP)
        #Contenedores de texto
        self.textos=Frame(self.raiz)
        self.textos.pack(side=TOP)
        self.framDeAbajo=Frame(self.raiz)
        self.framDeAbajo.pack(side=BOTTOM)
        #Entradas de texto
        self.t1=Entry(self.textos,width=40)
        self.t1.grid(row=0,column=0,padx=10,pady=10)
        self.t2=Entry(self.textos,width=40)
        self.t2.grid(row=1,column=0,padx=10,pady=10)
        self.t3=Entry(self.textos,width=40)
        self.t3.grid(row=2,column=0,padx=10,pady=10)
        self.t4=Entry(self.textos,width=40)
        self.t4.grid(row=3,column=0,padx=10,pady=10)
        #Botones
        self.b1=Button(self.textos,text="Validar",command=lambda:self.validar(1))
        self.b1.grid(row=0,column=1,padx=10,pady=10)
        self.b2=Button(self.textos,text="Validar",command=lambda:self.validar(2))
        self.b2.grid(row=1,column=1,padx=10,pady=10)
        self.b3=Button(self.textos,text="Validar",command=lambda:self.validar(3))
        self.b3.grid(row=2,column=1,padx=10,pady=10)
        self.b4=Button(self.textos,text="Validar",command=lambda:self.validar(4))
        self.b4.grid(row=3,column=1,padx=10,pady=10)
        #Espacios para la validacion de los cuadros de texto
        self.l1=Label(self.textos,text="...")
        self.l1.grid(row=0,column=2)
        self.l2=Label(self.textos,text="...")
        self.l2.grid(row=1,column=2)
        self.l3=Label(self.textos,text="...")
        self.l3.grid(row=2,column=2)
        self.l4=Label(self.textos,text="...")
        self.l4.grid(row=3,column=2)
        #Espacios para la descripcion de los cuadros de texto
        self.d1=Label(self.textos,text="    ")
        self.d1.grid(row=0,column=3)
        self.d2=Label(self.textos,text="    ")
        self.d2.grid(row=1,column=3)
        self.d3=Label(self.textos,text="    ")
        self.d3.grid(row=2,column=3)
        self.d4=Label(self.textos,text="    ")
        self.d4.grid(row=3,column=3)
        #Destruccion de la ventana-.
        self.bsalir=Button(self.framDeAbajo,text="Salir",command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        #Limpiar
        self.blimpiar=Button(self.framDeAbajo,text="Limpiar",command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        #Mostrar descripcion
        self.bmostrar=Button(self.framDeAbajo,text="Descripcion",command=self.mostrarDescripcion)
        self.bmostrar.pack(side=LEFT)
        #Dark Mode
        self.bdark=Button(self.framDeAbajo,text="Modo Oscuro",command=self.darkMode)
        self.bdark.pack(side=LEFT)
        #Bucle de la aplicacion
        self.raiz.mainloop()
    
    def limpiar(self):
        self.t1.delete(first=0,last=END)
        self.l1.config(fg="black",text="...")
        self.t2.delete(first=0,last=END)
        self.l2.config(fg="black",text="...")
        self.t3.delete(first=0,last=END)
        self.l3.config(fg="black",text="...")
        self.t4.delete(first=0,last=END)
        self.l4.config(fg="black",text="...")
        self.d1.config(text="    ")
        self.d2.config(text="    ")
        self.d3.config(text="    ")
        self.d4.config(text="    ")

    def validar(self,numero):
        if numero==1:#Validar IPv4
            txtAValidar=self.t1.get()
            x=re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",txtAValidar)
            if (x):
                self.l1.config(fg="green",text="IPv4 Valida")
            else:
                self.l1.config(fg="red",text="IPv4 Invalida")
        elif numero==2:#Validar IPv6
            txtAValidar2=self.t2.get()
            x=re.search("^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$",txtAValidar2)
            if (x):
                self.l2.config(fg="green",text="IPv6 Valida")
            else:
                self.l2.config(fg="red",text="IPv6 Invalida")
        elif numero==3:#Validar URL
            txtAValidar3=self.t3.get()
            x = re.search("^(http|https)?://[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,4}(/\S*)?$", txtAValidar3)
            if (x):
                self.l3.config(fg="green",text="URL Valida")
            else:
                self.l3.config(fg="red",text="URL Invalida")
        elif numero==4:#Validar Correo
            txtAValidar4=self.t4.get()
            x=re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",txtAValidar4)
            if (x):
                self.l4.config(fg="green",text="Correo Valido")
            else:
                self.l4.config(fg="red",text="Correo Invalido")
    
    def mostrarDescripcion(self):
        self.d1.config(text="IPv4")
        self.d2.config(text="IPv6")
        self.d3.config(text="URL")
        self.d4.config(text="Correo")
    
    def darkMode(self):
        colorFondo="#1c1c1c"
        colorLetra="#ffffff"
        self.raiz.config(bg=colorFondo)
        self.textos.config(bg=colorFondo)
        self.framDeAbajo.config(bg=colorFondo)
        widgetList =[
            self.b1, self.b2, self.b3, self.b4,
            self.bsalir, self.blimpiar, self.bmostrar, self.bdark,
            self.l1, self.l2, self.l3, self.l4,
            self.d1, self.d2, self.d3, self.d4,
            self.t1, self.t2, self.t3, self.t4
        ]
        for widget in widgetList:
            widget.config(bg=colorFondo, fg=colorLetra)
        self.raiz.update()#Actualiza la ventana

app = aplicacion()
