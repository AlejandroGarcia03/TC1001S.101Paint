'''
Equipo 2
Alejandro García - A01641920
César Benavides - A01285056
Rodrigo Ibarra - A01625569
'''

""" Snake, classic arcade game.
"""

from random import randrange
from turtle import *
from freegames import square, vector
import turtle

# Inicializar las variables del snanke
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
contador = 0
info = turtle.Turtle()
colors = ['blue', 'yellow', 'purple', 'orange', 'pink', 'black', 'brown', 'cyan']
color_index = 0

# Función que cambia la dirección del snake y checa
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    # Creación de variable global para contar la cantidad de movimientos del snake
    global contador
    contador += 1
    if contador % 5 == 0: # Si se cumple la condición, cambia la posición de la comida
        move_food()

# Función que checa si la cabeza del snake se encuentra dentro de los rangos permitidos
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Función que mueve al snake por segmentos
def move():
    """Move snake forward one segment."""        
    head = snake[-1].copy()
    head.move(aim)

    # Detecta si el snake no choca con el mismo o con los límites
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Agrega un nuevo segmento a la lista
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food() # Mover la comida a una posición válida
        writer.clear()
        writer.write(f'Snake:{len(snake)}', align='center', font=('chalkboard', 15, 'normal'))
    else:
        snake.pop(0)

    clear()

    # Se dibuja el snake
    for body in snake:
        square(body.x, body.y, 9, colors[color_index])

    # Se dibuja la comida
    square(food.x, food.y, 9, "white")
    center_x = food.x + 4.5  # Suma 4.5 para obtener el centro en el eje x
    center_y = food.y + 4.5  # Suma 4.5 para obtener el centro en el eje y
    goto(center_x, center_y)
    dot(10, colors[color_index-1])
    # Muestra en pantalla lo que tiene el buffer
    update()
    ontimer(move, 70)

#Función que mueve la comida y evalua que su posición sea correcta
def move_food():
    global cont
    cont = 0
    """Move food to a valid random position."""
    for _ in range(cont+1): # Genera posiciones random para la comida
        food.x = randrange(-18, 18) * 10
        food.y = randrange(-19, 19) * 10
        # Cambia el índice del color de la serpiente si come
        global color_index
        color_index = randrange(0, 8)
        if food not in snake:
            break

# Función que pone la información de los integrantes
def info_alumnos():
    info.up()
    info.goto(0,190)
    info.color('blue')
    info.write('Cristian Alejandro García Mendoza A01641920', align='left', font=('Arial', 10, 'normal'))
    info.goto(0,170)
    info.color('red')
    info.write('César Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    info.goto(0,150)
    info.color('green')
    info.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))
    info.hideturtle()
    

writer = Turtle(visible = False);
# Iniciar dimensiones de la ventana setup(alto, ancho, x_esq. sup. izq_wind, y_esq. sup. izq_wind)
setup(420, 420, 370, 0)
# Ocultar el turtle
hideturtle()
tracer(False)
# Guarda todos los eventos del teclado en una cola
listen()
# onkey(fx () - sin argumentos - lambda:)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Función que mueve la comida
move_food()
# Llamar a la función move()
move()
# Función que pone la información de los integrantes
info_alumnos()
# Agrega el título a la ventana del juego
title("Cristian García, César Benavides, Rodrigo Ibarra")
done()