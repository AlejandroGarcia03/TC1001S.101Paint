"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector
import turtle

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

t = turtle.Turtle()

cont = 0

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    global cont 
    cont+=1
    if  cont == 10:
        move_food()


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()  # Mover la comida a una posición valida

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Función que mueve la comida y evalua que su posición sea correcta
def move_food():
    #counter of movemetns resets
    """Move food to a valid random position."""
    while True:# Generate random positions for food within the boundaries
        food.x = randrange(-19, 19) * 10
        food.y = randrange(-20, 20) * 10
        global cont
        cont = 0
        if food not in snake:
            break

#Función que pone nombres
def info_alumnos():
    t.up()
    t.goto(-22,190)
    t.color('blue')
    t.write('Cristian Alejandro Garcia Mendoza A01641920', align='left', font=('Arial',8, 'normal'))
    t.goto(-21,170)
    t.color('pink')
    t.write('Cesar Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    t.goto(55,150)
    t.color('green')
    t.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#En las siguientes funciones podemos cambiar el valor de los numeros en sus respectivas direcciones para modificar la velocidad.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move_food() #Función de la comida
move()
info_alumnos() #Función para nombres
done()