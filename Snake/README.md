# Snake Acitivity
## 1 Food verification & names addition
#### Alejandro García
``` python
#Función que mueve la comida y evalua que su posición sea correcta
def move_food():
    """Move food to a valid random position."""
    while True:# Generate random positions for food within the boundaries
        food.x = randrange(-19, 19) * 10
        food.y = randrange(-20, 20) * 10
        if food not in snake:
            break

#Función que pone nombres
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
```