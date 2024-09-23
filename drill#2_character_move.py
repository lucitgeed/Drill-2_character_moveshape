from pico2d import *

open_canvas()

grass = load_image('grass.png')
char = load_image('character.png')


grass.draw_now(400, 90)
char.draw_now(400, 90)


while(True):

    for i in range(0, 100):
        clear_canvas_now()
        char.draw_now(400 + i, 90)
        i = i + 2

    for i in range(0, 50):
        clear_canvas_now()
        char.draw_now(400 + 100, 90 + i)
        i = i+2

    for i in range(0,200):
        clear_canvas_now()
        char.draw_now(400 + 100 - i, 90 + 50)
        i = i+2

    for i in range(0, 50):
        clear_canvas_now()
        char.draw_now(400 + 100 - 200, 90 + 50 - i)
        i = i + 2

    for i in range(0, 100):
        clear_canvas_now()
        char.draw_now(400 + 100 - 200 + i, 90 + 50 - 50)
        i = i + 2


    delay(2)



    for x in range(0, 50):
        for y in range(0, 50):
            clear_canvas_now()
            char.draw_now(400 + x, 90 + y)
            x = x + 2
            y = y + 2


    for x in range(0, 50):
        for y in range(0, 50):
            clear_canvas_now()
            char.draw_now(400 + 50 - x, 90 + 50 + y)
            x = x + 2
            y = y + 2


    for x in range(0, 50):
        for y in range(0, 50):
            clear_canvas_now()
            char.draw_now(400 - x, 90 + 50 + 50 - y)
            x = x + 2
            y = y + 2


    for x in range(0, 50):
        for y in range(0, 50):
            clear_canvas_now()
            char.draw_now(400 - 50 + x, 90 + 50 - y)
            x = x + 2
            y = y + 2


    delay(2)
            
    


close_canvas()
