"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end.
    start - vector (x,y)
    end - vector (x,y)
    up() - levanta la pluma
    down() - baja la pluma para dibujar
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    # rellena el square
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle2(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


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
    """Store value in state at key.
    Solo se llama cuando se va a modificar el 'shape'    
    """
    state[key] = value


# Estado inicial del Paint - Diccionario - start - indica si el usuario dio un click mouse -
state = {'start': None, 'shape': square}
# setup(alto, ancho, x_esq. sup. izq_wind, y_esq. sup. izq_wind)
setup(420, 420, 0, 0)
# registra la función que va a atender los eventos del mouse
onscreenclick(tap)
listen()
onkey(undo, 'u')
# lambda
onkey(lambda: color('red','black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('#33A2FF', '#33FF4F'), 'Z')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
