from tkinter import *
import random
import time
from random import randint

# Параметры для окна
tk = Tk()
tk.title('Pong')
tk.geometry('+300+100')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

# Поле
canvas = Canvas(tk, width=700, height=500, bd=0, highlightthickness=0)
canvas.config(bg='black')
canvas.pack()
tk.update()

# Центральная линия
canvas.create_line(350, 0, 350, 500, fill='#%06x' % randint(0, 0xFFFFFF))



# МЯЧ
class Ball:
    # конструктор
    def __init__(self, canvas, paddle_r, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle_r = paddle_r
        self.pS = 0
        self.p1S = 0
        self.drawP1 = None
        self.drawP = None
        self.id = self.canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 327, 220)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = random.choice([-2.5, 2.5])
        self.y = -2

    # Определение победителя
    def checkwin(self):
        winner = None
        if self.pS > self.p1S+1 and self.pS >= 11:
            self.winner_color = color_l
            winner = 'Left Player\n     WIN'

        if self.p1S > self.pS+1 and  self.p1S >= 11:
            self.winner_color = color_r
            winner = 'Right Player\n      WIN'

        return winner

    def drawwinner(self):
        self.canvas.create_text(344, 240, font=('', 70),text=self.checkwin(), fill=self.winner_color)

    def updatep(self, val):
        self.canvas.delete(self.drawP)
        self.drawP = self.canvas.create_text(170, 50,
                                             font=('', 40), text=str(val), fill=color_l)

    # Счет правого игрока
    def updatep_r(self, val):
        self.canvas.delete(self.drawP1)
        self.drawP1 = self.canvas.create_text(550, 50,
                                              font=('', 40), text=str(val), fill=color_r)

    # Отслеживание столкновния левой ракетки и мяча
    def hit_paddle(self, pos):

        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

            return False

    # Отслеживание столкновния правой ракетки и мяча
    def hit_paddle_r(self, pos):

        paddle_pos = self.canvas.coords(self.paddle_r.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

            return False

    # Отрисовка мяча и отслеживание столкновений
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.updatep_r(self.p1S)
            self.p1S += 1
            self.canvas.move(self.id, 327, 220)
            self.x = 4
            self.updatep_r(self.p1S)
        if pos[2] >= self.canvas_width:
            self.pS += 1
            self.canvas.move(self.id, -327, -220)
            self.x = -4
            self.updatep(self.pS)
        if self.hit_paddle(pos):
            self.x = 4
        if self.hit_paddle_r(pos):
            self.x = -4
        if self.checkwin() != None:
            self.canvas.move(self.id, 350, 350)




# Ракетка
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 200, 10, 310, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # Binding
        self.canvas.bind_all('w', self.up)
        self.canvas.bind_all('s', self.down)

    # движение ракетки вверх
    def up(self, e):
        self.y = -5
    # движение ракетки вних
    def down(self, e):
        self.y = 5

    # Отрисовка
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = -0



# Правая ракетка
class PaddleR:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680, 200, 690, 310, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.up)
        self.canvas.bind_all('<KeyPress-Down>', self.down)

    # движение ракетки вверх
    def up(self, e):
        self.y = -5
    # движение ракетки вних
    def down(self, e):
        self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = 0

color_l = '#%06x' % randint(0, 0xFFFFFF)
color_r = '#%06x' % randint(0, 0xFFFFFF)
paddle = Paddle(canvas, color_l)
paddle_r = PaddleR(canvas, color_r)
ball = Ball(canvas, paddle_r, paddle, '#%06x' % randint(0, 0xFFFFFF))
ball.updatep(0)
ball.updatep_r(0)


while ball.checkwin()==None:
    ball.draw()
    paddle.draw()
    paddle_r.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


ball.drawwinner()


tk.mainloop()
