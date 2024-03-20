from turtle import *
import turtle
from freegames import vector
import math
t = turtle.Turtle()
# Función para dibujar una línea desde el punto de inicio hasta el punto final
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado desde el punto de inicio hasta el punto final
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un círculo desde el punto de inicio hasta el punto final
def circle2(start, end):
    up()
    goto(start.x, start.y)
    down()
    radius = (end.x - start.x) / 2  # Calcular el radio
    circle(radius)
# Función para dibujar un rectángulo desde el punto de inicio hasta el punto final
def rectangle(start, end):
    """Draw rectangle from start to end."""


# Función para dibujar un triángulo desde el punto de inicio hasta el punto final
def triangle(start, end):
    """Draw triangle from start to end."""


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value

def info_alumnos():
    t.up()
    t.goto(0,190)
    t.color('blue')
    t.write('Cristian Alejandro Garcia Mendoza A01641920', align='left', font=('Arial', 10, 'normal'))
    t.goto(0,170)
    t.color('pink')
    t.write('Cesar Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    t.goto(0,150)
    t.color('green')
    t.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))

# Inicializar el estado y configurar la ventana
#Variable sate es un Diccionario
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

##ADDED COLORS
onkey(lambda: color('pink'), 'P')
onkey(lambda: color('violet'), 'V')
onkey(lambda: color("#33A2FF","#33FF4F"), 'Z')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
info_alumnos()
done()
