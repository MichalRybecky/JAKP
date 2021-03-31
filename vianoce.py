from random import *
import tkinter
import math

c = tkinter.Canvas(width = 1000, height = 1000)
c.pack()

x = 500
y = 10


c.create_polygon(x - 100, y + 250, x + 100, y + 250, x, y, fill = 'darkgreen')
c.create_polygon(x - 250, y + 550, x + 250, y + 550, x, y + 250, fill = 'darkgreen')
c.create_polygon(x - 450, y + 900, x + 450, y + 900, x, y + 550, fill = 'darkgreen')


def gula(sur):
    x = sur.x
    y = sur.y
    d = 10
    b = 5
    for i in range(2):
        c.create_oval(x - d, y - d, x + d, y + d, fill = choice(("red", "white", "silver", "grey")), outline = '') 
        d = b
        
        
r = 10 
def girlanda(event):
    global r
    x, y = event.x, event.y
    c.create_oval(x-r, y-r, x+r, y+r, fill='gold', outline = '')
   

def hviezda(event):
    center_x=500
    center_y=80
    r=80 # The distance from the center point to each angle, called the radius

 # Place the five points of the five-pointed star in turn
    points=[
         # 
        center_x-int(r*math.sin(2*math.pi/5)),
        center_y-int(r*math.cos(2*math.pi/5)),

         # 
        center_x+int(r*math.sin(2*math.pi/5)),
        center_y-int(r*math.cos(2*math.pi/5)),

         # 
        center_x-int(r*math.sin(math.pi/5)),
        center_y+int(r*math.cos(math.pi/5)),

         # vertex
        center_x,
        center_y-r,

         # 
        center_x+int(r*math.sin(math.pi/5)),
        center_y+int(r*math.cos(math.pi/5)),
]
 # Create a polygon based on ten vertices
    c.create_polygon(points,outline='',fill='gold')
 # 's five-pointed star ‘three words at the center
    c.create_text(500,450,text='Merry Christmas', font='arial 75 bold', fill = 'red')


def vlocky(event):
    while True:
        for i in range(50):
            x = randint(1, 1001)
            y = randint(1, 1001)
            c.create_text(x, y, text = '*', font = 'arial 30 bold', fill = 'lightblue', tag = 't')
        c.update()
        c.after(1000)
        c.delete('t')
    
    
print("pre spustenie snehu click 's'")   
print("Pre stastne sviatky click 'm'!")

c.delete('t')
c.bind('<Button-1>', gula)
c.bind('<B3-Motion>', girlanda)
c.bind_all('<m>', hviezda)
c.bind_all('<s>', vlocky)