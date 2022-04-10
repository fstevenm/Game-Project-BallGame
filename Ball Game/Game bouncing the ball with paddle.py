from tkinter import *
import random
#import pygame

tk = Tk()
tk.title("Bola bounce")
tk.resizable(0,0) # tk window cannot be resized in x or y
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=1000, height=400, bd=0, highlightthickness=0) #no borders around the canvas
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0] #arah sumbu x bola
        self.y = -3 #arah sumbu y bola
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False
        bermain()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                main_lagi()
                return True
        return False

    def draw(self):
        if self.hit_bottom == False: #Jika bola tidak kena bawah

            self.canvas.move(self.id, self.x, self.y)

            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 3   #mantul dari atas
            if pos[3] >= self.canvas_height:
                self.y = -3   #mantul dari bawah

            if pos[3] >= self.canvas_height:
                self.hit_bottom = True  #Buat berhenti

            if self.hit_paddle(pos) == True:
                self.y = -3   #buat mantul di papannya

            if pos[0] <= 0:
                self.x = 3    #mantul tembok kiri
            if pos[2] >= self.canvas_width:
                self.x = -3     #mantul tembok kanan

            if ball.hit_bottom == False:
                self.canvas.after(10, self.draw) # miliseconds, function

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id,200, 300)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)



    def draw(self):
        if ball.hit_bottom == False:

            self.canvas.move(self.id, self.x, 0)
#            self.x=0 #buat jalannya patah2

            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0 #stop jika sampe bates kiri
            if pos[2] >= self.canvas_width:
                self.x = 0 #stop jika sampe bates kanan

            self.canvas.after(10, self.draw)

    def turn_left(self, event):
        self.pos = self.canvas.coords(self.id)
        
        if self.pos[0] >= 1:
            self.x = -3 #Jalan ke kiri

    def turn_right(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[2] <= self.canvas_width-1:
            self.x = 3 #Jalan ke kanan
            
def bg():
    canvas.grid(row=0,column=0,columnspan=2,rowspan=3)
    gambarbaru = PhotoImage(file='download.png')
    canvas.create_image(400,200, image=gambarbaru)
    canvas.image=gambarbaru

#pygame.mixer.init(88200)
bg()
def bermain():
    pygame.mixer.music.load('main.wav')
    pygame.mixer.music.play(2)

def stop():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('dead.wav'))
    
paddle = Paddle(canvas, "red")
ball = Ball(canvas, paddle, "blue")

    
def main_lagi():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('lompat.wav'))

def start_game(event):
    ball.draw()

canvas.bind_all("<Button-1>", start_game)
paddle.draw()

tk.mainloop()