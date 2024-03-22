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

# Trae de libreria freegames el gif de nombre car
car = path('car.gif')
# Lista de emojis de temática "Tecnología"
emojis = ['👨‍💻', '📱', '💻', '🖥️', '📀', '🎧', '📷', '📡',
          '🛰️', '🚀', '👩‍🚀', '👾', '🕹️', '🎮', '🔌', '🧲',
          '⚡', '🤖', '💡', '📟', '🖨️', '🖲️', '📠', '☎️',
          '📞', '🌐', '📶‍', '🔬', '🧑‍🦼', '👽', '🦾', '🤖',]
print(len(emojis))
# Inicia las cartas del memorama
tiles = emojis * 2
# Indica si tengo una carta destapada
state = {'mark': None}
# Esconde las 64 barajas
hide = [True] * len(tiles)
# Pluma que dibuja los nombres
info = Turtle()
# Contador de taps
tap_count = 0
# Contador de parejas encontradas
pairs_found = 0

# Función para dibujar un cuadro con color de fondo diferente
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y - 30)  # Mueve el cuadrado por +30 en el eje Y
    down()
    color('blue', 'lightgreen')  # Cambiar color de fondo del cuadro
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Función que pone la información de los integrantes
def info_alumnos():
    info.up()
    info.goto(-65,250)
    info.color('gray')
    info.write('Cristian Alejandro Garcia Mendoza A01641920', align='left', font=('Arial', 10, 'normal'))
    info.goto(-19,230)
    info.color('red')
    info.write('Cesar Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    info.goto(53,210)
    info.color('green')
    info.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))

# Función para convertir coordenadas (x, y) a índice de tiles
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 170) // 50) * 8) # Ajusta coordenada en Y

# Función para convertir índice de tiles a coordenadas (x, y)
def xy(count):
    """Convert tiles count to (x, y) coordinates. Retorna la esq inf izq. de la carta"""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 170 # Ajusta coordenada en Y

# Función para manejar el tap/click del usuario
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count, pairs_found  # Acceder a las variables globales
    tap_count += 1  # Incrementar el contador de taps

    if x >=-200 and x<=200 and y>=-200 and y<200:
        # Posición de la última carta seleccionada
        spot = index(x + 5, y + 30)
    print(x)
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
        pairs_found += 1  # Incrementar contador de parejas encontradas

    
    # Verificar si todos los cuadros están destapados
    if all(not h for h in hide):
        messagebox.showinfo("¡Felicidades!", f"¡Ganaste un auto!!\nTaps: {tap_count}")

# Función para dibujar el juego
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
        goto(x + 5, y - 30)  # Centrar emoji en el cuadro
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # Mostrar el número de taps y parejas encontradas en la ventana
    goto(-200, 210)
    color('black')
    write(f"Found Pairs: {pairs_found}", font=('Arial', 16, 'normal'))
    goto(-200, 230)
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))
    # Desactiva los clicks
    # onscreenclick(None)
    update()
    ontimer(draw, 100)

# Revuelve las barajas
shuffle(tiles)
# Iniciar dimensiones de la ventana setup(alto, ancho, x_esq. sup. izq_wind, y_esq. sup. izq_wind)
setup(620, 620, 570, 0)
# Color del fondo
bgcolor("lightblue")
# Agrega el título a la ventana del juego
title("Cristian García, César Benavides, Rodrigo Ibarra")
addshape(car)
# Oculta el turtle
hideturtle()
# No se dibuja paso por paso el cuadrado
tracer(False)
# Espera eventos del mouse
onscreenclick(tap)
# Llamaa la función draw()
draw()
# Función que pone la información de los integrantes
info_alumnos()
# Agrega el título a la ventana del juego
title("Cristian García, César Benavides, Rodrigo Ibarra")
done()