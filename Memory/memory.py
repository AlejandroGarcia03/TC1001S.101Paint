'''
Equipo 2
Alejandro García - A01641920
César Benavides - A01285056
Rodrigo Ibarra - A01625569
'''

# Memory, puzzle game of number pairs.

from random import *
from turtle import *

from freegames import path
from tkinter import messagebox  # Import messagebox from tkinter for showing message
import turtle

#Trae de libreria freegames el gif de nombre car
car = path('car.gif')
# Inicia las cartas del memorama
tiles = list(range(32)) * 2
# Indica si tengo una carta destapada
state = {'mark': None}
# Esconde las 64 barajas
hide = [True] * 64
#pluma que dibuja los nombres
t=Turtle()
# Contador de taps
tap_count = 0  



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('white', 'gray')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Función que pone nombres
def info_alumnos():
    t.up()
    t.goto(-65,250)
    t.color('pink')
    t.write('Cristian Alejandro Garcia Mendoza A01641920', align='left', font=('Arial', 10, 'normal'))
    t.goto(-19,230)
    t.color('white')
    t.write('Cesar Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    t.goto(53,210)
    t.color('yellow')
    t.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates. Retorna la esq inf izq. de la carta"""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # Posición de la última carta seleccionada
    if x >=-200 and x<=200 and y>=-200 and y<200:
        spot = index(x + 5, y + 30)  # Adjust Y coordinate for tap

    # Posición de la carta anterior o si no había carta anterior tendrá un None
    mark = state['mark']
    
    # Checa si no hay carta previa, se dio click en la misma carta, no son par
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Si fue par, destapar las 2 cartas
        hide[spot] = False
        hide[mark] = False
        # Ya no existe carta destapada
        state['mark'] = None

     # Verificar si todos los cuadros están destapados
    if all(not h for h in hide):
        messagebox.showinfo("¡Felicidades!", f"¡Ganaste un auto!\nTaps: {tap_count}")

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    # Crea los cuadrados del memorama
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    # Posición de la carta anterior 
    mark = state['mark']

    
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Desactiva los clicks
    # onscreenclick(None)
    update()
    ontimer(draw, 100)

# Revuelve las barajas
shuffle(tiles)
# Iniciar dimensiones de la ventana setup(alto, ancho, x_esq. sup. izq_wind, y_esq. sup. izq_wind)
setup(620, 620, 570, 0)
# Color del fondo
bgcolor("Blue")
# Agrega el título a la ventana del juego
title("Cristian García, César Benavides, Rodrigo Ibarra")
addshape(car)
# Oculta el turtle
hideturtle()
# No se dibuja paso por paso el cuadrado
tracer(False)
# Espera eventos del mouse
onscreenclick(tap)
#Escribir nombre de equipo
info_alumnos()
draw()
done()
