from ursina import *
from random import randint


def update():
    global x_direction, y_direction, z_direction

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    # time.dt is a global function

    cube.x = cube.x + 0.5 * time.dt * x_direction
    cube.y = cube.y + 0.5 * time.dt * y_direction
    cube.z = cube.z - 1.0 * time.dt * z_direction

    cube.rotation_x = cube.rotation_x + 50 * time.dt
    cube.rotation_y = cube.rotation_y + 50 * time.dt
    cube.rotation_z = cube.rotation_z + 50 * time.dt

    cube.color = color.rgb(red, green, blue)

    if abs(cube.x) > 3:
        x_direction = x_direction * (-1)

    if abs(cube.y) > 3:
        y_direction = y_direction * (-1)

    if abs(cube.z) > 6:
        z_direction = z_direction * (-1)


app = Ursina()

# rotation = (x,y,z), scale = (x,y,z), position = (x,y,z)
# The position (0,0,0) is dead center
# model includes quad (2D square), circle (2D circle), sphere (3D)
# color can also be RBG, color=color.rgb(45,45,255)

x_direction = 1
y_direction = 1
z_direction = 1

cube = Entity(model="cube", rotation=(45, 45, 0), scale=(1, 1, 2), position=(1, 1, 0), color=color.red)

txt = Text(text="Hello. Welcome to Python programming.", position=(-0.3, -0.3, 0), scale=(1, 1, 1), color=color.blue)

app.run()
