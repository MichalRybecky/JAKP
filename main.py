"""
Hlavny file projektu,
sluzi na spustanie modulov a submodulov
"""

import tkinter

HEIGHT=900
WIDTH=500

canvas = tkinter.Canvas(height=HEIGHT, width=WIDTH)
canvas.pack()

x_spacing = 135
y_spacing = 160
size = 50
x, y = x_spacing // 1.5, y_spacing // 1.5
count = 0
for i in range(5):
    for j in range(3):
        canvas.create_rectangle(x, y, x + size, y + size)
        canvas.create_text(x + size // 2, y + size // 2, text=count)
        x += x_spacing
        count += 1
    y += y_spacing
    x = x_spacing // 1.5

canvas.mainloop()

