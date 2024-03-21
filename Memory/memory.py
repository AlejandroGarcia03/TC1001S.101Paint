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

car = path('car.gif')
# Inicia las cartas del memorama
tiles = list(range(32)) * 2
# Indica si tengo una carta destapada
state = {'mark': None}
# Esconde las 64 barajas
hide = [True] * 64


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


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates. Retorna la esq inf izq. de la carta"""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # Posición de la última carta seleccionada
    spot = index(x, y)
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
setup(620, 620, 370, 0)
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

draw()
done()
