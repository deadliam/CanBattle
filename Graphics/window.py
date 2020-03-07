from tkinter import *
import math

root = Tk()
root.title("Can Battle")
root.geometry('1620x620')

canvas = Canvas(root, width=1315, height=615, bg='#789')
canvas.pack(side='right')

for y in range(27):
    k = 50 * y
    canvas.create_line(10 + k, 610, 10 + k, 10, width=1, fill='#191930')

for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10 + k, 1310, 10 + k, width=1, fill='#191938')

w_field = Label(root, text='Omega')
w_field.place(x=5, y=10)
phi_field = Label(root, text='Phi')
phi_field.place(x=5, y=50)
A_field = Label(root, text='A')
A_field.place(x=5, y=90)
dy_field = Label(root, text='Dy')
dy_field.place(x=5, y=130)

entry_w = Entry(root)
entry_w.place(x=70, y=10)
entry_phi = Entry(root)
entry_phi.place(x=70, y=50)
entry_A = Entry(root)
entry_A.place(x=70, y=90)
entry_dy = Entry(root)
entry_dy.place(x=70, y=130)

def sinus(w, phi, A, dy):
    global sin
    sin = 0
    xy = []
    for x in range(1300):
        y = math.sin(x * w)
        xy.append(x + phi)
        xy.append(y * A + dy)
    sin = canvas.create_line(xy, fill='red')
    print xy

def delete_sin_line():
    canvas.delete(sin)

attack_button = Button(root, text='Calc')
attack_button.bind('<Button-1>', lambda event: sinus(float(entry_w.get()),
                                                     float(entry_phi.get()),
                                                     float(entry_A.get()),
                                                     float(entry_dy.get())))
attack_button.place(x=5, y=170)

reset_button = Button(root, text='Reset')
reset_button.bind('<Button-1>', lambda event: delete_sin_line())
reset_button.place(x=70, y=170)

root.mainloop()
