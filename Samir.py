from tkinter import *

ventana = Tk()
ventana.minsize(800,600)
ventana.title("Proyecto Taller 2")


inicio = Canvas(ventana, width=800, height=600)
inicio.pack()
inicio.place(x=0,y=0)

def acercade(inicio2):
    inicio2.destroy()

    inicio = Canvas(ventana, width=800, height=600)
    inicio.pack()
    inicio.place(x=0,y=0)

    inicio.create_text(400,50, text="INSTITUTO TECNOLOGICO DE COSTA RICA, ESCUELA DE COMPUTADORES", font=("Helvetica",16),fill="black")
    inicio.create_text(400,120, text="TALLER DE PROGRMACION, PRIMER SEMESTRE DEL 2023", font=("Helvetica",12),fill="black")
    inicio.create_text(400,150, text="PRIMER PROYECTO DE TALLER DE PROGRAMACION, DESTROZA NAVES", font=("Helvetica",12),fill="black")
    inicio.create_text(400,180, text="PROFESOR: MILTON VILLEGAS LEMUS", font=("Helvetica",12),fill="black")
    inicio.create_text(400,210, text="ESTUDIANTES: ", font=("Helvetica",12),fill="black")
    inicio.create_text(400,240, text="ESTUDIANTES: -CABRERA TABASH SAMIR, 2022161229", font=("Helvetica",12),fill="black")
    inicio.create_text(400,270, text="ESTUDIANTES: -CAMPOS ABARCA ESTEBAN, 2022207705 ", font=("Helvetica",12),fill="black")
    inicio.create_text(400,300, text="PAIS DE PRODUCCION: COSTA RICA", font=("Helvetica",12),fill="black")
    inicio.create_text(400,330, text="PROGRAMA EJECUTADO EN PYTHON 3.11.2", font=("Helvetica",12),fill="black")

    volver = Button(inicio, text = "VOLVER", command=lambda:menu(inicio))
    volver.place(x = 600, y = 525, width= 50, height= 50)

def menu(inicio2):
    inicio2.destroy()

    inicio = Canvas(ventana, width=800, height=600)
    inicio.pack()
    inicio.place(x=0,y=0)

    BtnAcercade = Button(inicio, text="ACERCA DE", command=lambda: acercade(inicio))
    BtnAcercade.place(x =100, y = 100, width=100, height=100)

menu(inicio)
ventana.mainloop()