from tkinter import *
import random
#import numpy as np
#import pygame

tk = Tk()
tk.title("Bola Hindar wkwk")
tk.resizable(0,0) 
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=1000, height=500, bd=0, highlightthickness=0) 
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id,500,0)

        startsx = [-4,-3,-2,-1,1,2,3,4]
        startsy = [-4,-3,-2,-1,1,2,3,4]
        
        random.shuffle(startsx)
        random.shuffle(startsy)
        self.x = startsx[0] #arah sumbu x bola
        self.y = startsy[0] #arah sumbu y bola
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False
        #bermain()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                #main_lagi()
                return True
        return False

    def draw(self):
        if self.hit_bottom == False: #Jika bola tidak kena bawah

            self.canvas.move(self.id, self.x, self.y)

            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 4   #mantul dari atas
            if pos[3] >= self.canvas_height:
                self.y = -4  #mantul dari bawah

            if pos[3] >= self.canvas_height:
                self.hit_bottom = False  #Buat berhenti

            if self.hit_paddle(pos) == True:
                self.hit_bottom =True
                #pygame.mixer.music.pause()
                stop_game()
                                
#                self.y = -3   #buat mantul di papannya

            if pos[0] <= 0:
                self.x = 4    #mantul tembok kiri
            if pos[2] >= self.canvas_width:
                self.x = -4     #mantul tembok kanan

            if self.hit_bottom == False:
                self.canvas.after(10, self.draw) # miliseconds, function

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 30, 30, fill=color)
        
        self.canvas.move(self.id,200, 300)
        
        self.x = 0
        self.y=0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Up>",self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>",self.turn_down)


    def draw(self):
        if ball_1.hit_bottom == False and ball_2.hit_bottom == False and ball_3.hit_bottom == False\
           and ball_4.hit_bottom == False and ball_5.hit_bottom == False:

            self.canvas.move(self.id, self.x, self.y)
            self.x=0 #buat jalannya patah2
            self.y=0

            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0 #stop jika sampe bates kiri
            if pos[2] >= self.canvas_width:
                self.x = 0 #stop jika sampe bates kanan

            self.canvas.after(10, self.draw)
        

    def turn_left(self, event):
        self.pos = self.canvas.coords(self.id)
        
        if self.pos[0] >= 1:
            self.x = -15 #Jalan ke kiri
    
    def turn_up(self, event):
        self.pos = self.canvas.coords(self.id)
        
        if self.pos[0] >= 1:
            self.y = -15 #Jalan ke atas 

    def turn_right(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[2] <= self.canvas_width-1:
            self.x = 15 #Jalan ke kanan
    
    def turn_down(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[2] <= self.canvas_width-1:
            self.y = 15 #Jalan ke bawah

#gambarbaru = PhotoImage(file='bus.png')
#image = canvas.create_image(100,100, anchor=NW, image=gambarbaru)
#def move(event):
#    if event.char=="a":
#        canvas.move(image,-10,0)
#    elif event.char=="d":
#        canvas.move(image,10,0)
#    elif event.char=="w":
#        canvas.move(image,0,-10)
#    elif event.char=="s":
#        canvas.move(image,0,10)

def bg():
    canvas.grid(row=0,column=0)
    gambarbaru = PhotoImage(file='download.png')
    canvas.create_image(500,250, image=gambarbaru)
    canvas.image=gambarbaru

#pygame.mixer.init(88200)
bg()
#def bermain():
    #pygame.mixer.music.load('main.wav')
    #pygame.mixer.music.play(2)

#def stop():
    #pygame.mixer.Channel(3).play(pygame.mixer.Sound('dead.wav'))
    
paddle = Paddle(canvas, "darkred")
ball_1 = Ball(canvas, paddle, "blue")
ball_2 = Ball(canvas, paddle, "green")
ball_3 = Ball(canvas, paddle, "yellow")
ball_4 = Ball(canvas, paddle, "orange")
ball_5 = Ball(canvas, paddle, "black")

def stop_game():
    ball_1.x,ball_1.y=0,0
    ball_2.x,ball_2.y=0,0
    ball_3.x,ball_3.y=0,0
    ball_4.x,ball_4.y=0,0
    ball_5.x,ball_5.y=0,0
    
#def main_lagi():
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('dead.wav'))

def start_game(event):
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    ball_4.draw()
    ball_5.draw()

#tk.bind("<Key>",move)
canvas.bind_all("<Button-1>", start_game)
paddle.draw()

tk.mainloop()