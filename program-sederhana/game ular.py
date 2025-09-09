
from tkinter import *
import random
import os
os.system('cls')


LEBARGAME = 1000
TINGGIGAME= 550
KECEPATAN = 115
UKURANSPASI = 50
BAGIANTUBUH = 3
WARNAULAR = "#09FF00"
WARNAMAKANAN = "#FF0000"
WARNABACKGROUND = "#000000"



class Snake:

    def __init__(self):
        self.body_size = BAGIANTUBUH
        self.coordinates = []
        self.squares = []

        for i in range(0, BAGIANTUBUH):
            self.coordinates.append([0, 0])

        for x, y, in self.coordinates:
            square = canvas.create_rectangle(x, y, x + UKURANSPASI, y + UKURANSPASI, fill=WARNAULAR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0, (LEBARGAME/UKURANSPASI)-1) * UKURANSPASI
        y = random.randint(0, (TINGGIGAME/UKURANSPASI)-1) * UKURANSPASI
         
        self.coordinates =  [x, y]

        canvas.create_oval(x, y, x + UKURANSPASI, y + UKURANSPASI, fill=WARNAMAKANAN, tag="food")


def next_turn(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= UKURANSPASI
    elif direction == "down":
        y += UKURANSPASI
    elif direction == "left": 
        x -= UKURANSPASI
    elif direction == "right":
        x += UKURANSPASI
    
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + UKURANSPASI, y + UKURANSPASI, fill=WARNAULAR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="score= {}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if cek_collision(snake):
        game_over()

    else:
        window.after(KECEPATAN, next_turn, snake, food)

def change_direction(arahbaru):
    
    global direction

    if arahbaru == 'left':
        if direction != 'right':
            direction = arahbaru

    elif arahbaru == 'right':
        if direction != 'left':
            direction = arahbaru

    elif arahbaru == 'up':
        if direction != 'down':
            direction = arahbaru

    elif arahbaru == 'down':
        if direction != 'up':
            direction = arahbaru


def cek_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= LEBARGAME:
        print("game over gi")
        return True
    elif y < 0 or y >= TINGGIGAME:
        print("game over gi")
        return True

    for bagian_tubuh in snake.coordinates[1:]:
        if x == bagian_tubuh[0] and y == bagian_tubuh[1]:
            print("game over gi")
            return True
        
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text((canvas.winfo_width()/2), canvas.winfo_height()/2, font=('consolas',70), text='"game over"\n by irgi', fill="red", tag="gameover")

window = Tk()
window.title("Permainan Ular")
window.resizable(False,False)

score = 0
direction = "down"

label = Label(window, text="score : {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, background=WARNABACKGROUND, height=TINGGIGAME, width=LEBARGAME)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()


