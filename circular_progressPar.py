import tkinter as tk
root = tk.Tk()
backClr = "white"
frontClr = "black"
midClr = "EEEEEE"

cWidth = 100
cHeight = 100
x1 = 0
y1 = 0
x2 = cWidth
y2 = cHeight
bWidth = 25
ext = 28

canvas = tk.Canvas(root, width=cWidth, height= cHeight, background=backClr)
canvas.pack()

canvas.create_oval(x1, y1, x2, y2, fill=midClr , outline=midClr)
canvas.create_arc(x1, y1, x2, y2, fill=frontClr , extent=ext)
canvas.create_oval(x1 + bWidth, y1 + bWidth, x2 - bWidth ,y2 - bWidth, fill = backClr, outline = backClr)
canvas.create_text(cWidth / 2, cHeight/2,text=ext)
tk.mainloop()