import easy_tui as sTUI
from easy_tui import controls

hello = controls.Label(25, 3, "Hola, mundo")

nombre = controls.Entry(25, 4, "Nombre: ")
apellidos = controls.Entry(25, 5, "Apellidos: ")

def cambiaNombre():
    hello.text = f"Hola, {nombre.value} {apellidos.value}"

def limpiaTodo():
    nombre.value = ""
    apellidos.value = ""
    cambiaNombre()


f1 = controls.KeyButton(0, key=sTUI.F1, label="Reset", command=limpiaTodo)
f2 = controls.KeyButton(16,key=sTUI.F2, command=cambiaNombre, label="Saluda")


sTUI.loop()


