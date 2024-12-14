# importing libraries
import pgzrun
from random import randint

# Screen size
WIDTH = 300
HEIGHT = 300

def draw():
    screen.clear()

    width = 300
    height = 100

    for i in range(15):
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)

        box = Rect((0,0),(width,height))
        box.center = (150,150)
        screen.draw.rect(box,(r,g,b))

        width -= 10
        height += 10
pgzrun.go()
