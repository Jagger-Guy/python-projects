import tkinter as tk

window = tk.Tk()
WINDOW_WIDTH = window.winfo_screenwidth()
WINDOW_HEIGHT = window.winfo_screenheight()
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0')
window.title("UwU")
window.resizable(False,False)
window.bind("<Escape>", lambda event: window.destroy())

canvas = tk.Canvas(window, bg = 'white', height = WINDOW_HEIGHT, width = WINDOW_WIDTH)
canvas.pack()
floor = canvas.create_rectangle((0, WINDOW_HEIGHT-100, WINDOW_WIDTH, WINDOW_HEIGHT), fill = 'black')

label0 = tk.Label(window, bg = "white", text = "Controls:").place(relx = 0.01, rely = 0.01)
label1 = tk.Label(window, bg = "white", text = "w a s d - move").place(relx = 0.01, rely = 0.03)
label2 = tk.Label(window, bg = "white", text = "q - stop square").place(relx = 0.01, rely = 0.05)
label3 = tk.Label(window, bg = "white", text = "esc - exit program").place(relx = 0.01, rely = 0.07)
label4 = tk.Label(window, bg = "white", text = "")
label4.place(relx = 0.93, rely = 0.03)

canvas.create_rectangle((100,100,150,50), fill = "black")

class Square:

    def __init__(self,canvas,x1,y1,x2,y2,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x1,y1,x2,y2,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.coordinates = self.canvas.coords(self.rect)

        window.bind('<KeyPress>', self.keypress)

    def keypress(self,event):
        global timer
        key = event.char
        if key == "w":
            self.keypress_w(event)
        elif key == "a":
            self.keypress_a(event)
        elif key == "s":
            self.keypress_s(event)
        elif key == "d":
            self.keypress_d(event)
        self.coordinates = self.canvas.coords(self.rect)
        print(self.coordinates)
        self.collision(event)
        window.update()


    def collision(self,event):
        if self.coordinates[0] <= 155 and self.coordinates[0] >= 150 and self.coordinates[1] >= 10 and self.coordinates[1] <= 90:
            self.coordinates = [(WINDOW_WIDTH/2),100,((WINDOW_WIDTH/2)+50)]
            self.canvas.moveto(self.rect,(WINDOW_WIDTH/2),100)


    def keypress_w(self,event):
        self.xVelocity = 0
        self.yVelocity = -10
        if self.coordinates[1] <= 0:
            self.yVelocity = 0
        self.canvas.move(self.rect,self.xVelocity,self.yVelocity)


    def keypress_a(self,event):
        self.yVelocity = 0
        self.xVelocity = -10
        if self.coordinates[0] <= 0:
            self.xVelocity = 0
        self.canvas.move(self.rect,self.xVelocity,self.yVelocity)


    def keypress_s(self,event):
        self.xVelocity = 0
        self.yVelocity = 10
        if self.coordinates[3] >= WINDOW_HEIGHT-100:
            self.yVelocity = 0
        self.canvas.move(self.rect,self.xVelocity,self.yVelocity)


    def keypress_d(self,event):
        self.yVelocity = 0
        self.xVelocity = 10
        if self.coordinates[2] >= WINDOW_WIDTH:
            self.xVelocity = 0
        self.canvas.move(self.rect,self.xVelocity,self.yVelocity)



rect = Square(canvas,(WINDOW_WIDTH/2),100,((WINDOW_WIDTH/2)+50),150,0,0,'black')


window.mainloop()