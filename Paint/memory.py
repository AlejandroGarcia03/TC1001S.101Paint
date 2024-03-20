from random import shuffle
from turtle import *
from tkinter import messagebox  # Import messagebox from tkinter for showing message
import turtle
t=Turtle()

# Cambiar el color de fondo de la ventana
bgcolor('lightblue')

# Lista de emojis para los pares de tiles
emojis = ['🍎', '🍌', '🍉', '🍇', '🍓', '🍊', '🍋', '🍒',
          '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼']

#Función que pone nombres
def info_alumnos():
    t.up()
    t.goto(0,190)
    t.color('blue')
    t.write('Cristian Alejandro Garcia Mendoza A01641920', align='left', font=('Arial', 10, 'normal'))
    t.goto(0,170)
    t.color('black')
    t.write('Cesar Alejandro Benavides A01285056', align='left', font=('Arial', 10, 'normal'))
    t.goto(0,150)
    t.color('green')
    t.write('Rodrigo Ibarra A01625569', align='left', font=('Arial', 10, 'normal'))

def shuffle_tiles():
    """Shuffle the tiles to randomize emojis."""
    shuffle(tiles)  # Shuffle the tiles directly

# Asignar emojis aleatorios a los tiles
tiles = emojis * 2
shuffle_tiles()

# Estado del juego y lista de tiles ocultos
state = {'mark': None}
hide = [True] * len(tiles)
tap_count = 0  # Contador de taps

# Función para dibujar un cuadro con color de fondo diferente
def square(x, y):
    """Draw white square with blue outline at (x, y)."""
    up()
    goto(x, y + 30)  # Move square by +30 in Y-axis
    down()
    color('blue', 'white')  # Cambiar color de fondo del cuadro
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

# Función para convertir coordenadas (x, y) a índice de tiles
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 170) // 50) * 8)  # Adjust Y coordinate

# Función para convertir índice de tiles a coordenadas (x, y)
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 170  # Adjust Y coordinate

# Función para manejar el tap/click del usuario
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Acceder a la variable global tap_count
    tap_count += 1  # Incrementar el contador de taps
    spot = index(x, y - 30)  # Adjust Y coordinate for tap
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Verificar si todos los cuadros están destapados
    if all(not h for h in hide):
        messagebox.showinfo("¡Felicidades!", f"¡Ganaste un auto!\nTaps: {tap_count}")

# Función para dibujar el juego
def draw():
    """Draw tiles and emojis."""
    clear()

    for count in range(len(tiles)):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+5 , y+30 )  # Centrar emoji en el cuadro
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps en la ventana
    goto(-180, 180)
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

# Configuración de la ventana y dibujo inicial del juego
setup(620, 620, 570, 0)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
info_alumnos()
done()
