from turtle import *
import turtle
from freegames import vector
import math
t = turtle.Turtle()


# Función para dibujar una línea desde el punto de inicio hasta el punto final
def line(start, end):
    """ Draw line from start to end.
    start - vector (x,y)
    end - vector (x,y)
    up() - levanta la pluma
    down() - baja la pluma para dibujar
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado desde el punto de inicio hasta el punto final
def square(start, end):

    """ Draw square from start to end. """
    up()
    goto(start.x, start.y)
    down()
    # rellena el square
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
    begin_fill()
    circle(radius)
    end_fill()
    """ Draw circle from start to end. """

 

# Función para dibujar un rectángulo desde el punto de inicio hasta el punto final
def rectangle(start, end):
    """ Draw rectangle from start to end. """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):  # Repetir dos veces para completar el rectángulo
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


# Función para dibujar un triángulo desde el punto de inicio hasta el punto final
def triangle(start, end):
    """ Draw triangle from start to end. """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):  # Repetir tres veces para completar el triángulo
        forward(end.x - start.x)
        left(120)

    end_fill()

# Función que detecta un toque en la pantalla para dibujar una figura 
def tap(x, y):
    """ Store starting point or draw shape. """

    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

    
#Función que pine nombres
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

# Función que almacena un valor específico
def store(key, value):
    """ Store value in state at key.
    Solo se llama cuando se va a modificar el 'shape'    
    """
    state[key] = value


# Estado inicial del Paint - Diccionario - start - indica si el usuario dio un click mouse -
state = {'start': None, 'shape': square}
# setup(alto, ancho, x_esq. sup. izq_wind, y_esq. sup. izq_wind)
setup(420, 420, 0, 0)
# Registra la función que va a atender los eventos del mouse
onscreenclick(tap)
listen()
onkey(undo, 'u')
# Función Lambda (anónima)
onkey(lambda: color('red','black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

##ADDED COLORS
onkey(lambda: color('pink'), 'P')
onkey(lambda: color('violet'), 'V')
onkey(lambda: color("#33A2FF","#33FF4F"), 'Z')

#Shape
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
info_alumnos()
done()