from tkinter import *

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

strength_field = Label(root, text='Strength')
strength_field.place(x=5, y=10)

corner_field = Label(root, text='Corner')
corner_field.place(x=5, y=50)

entry_strength = Entry(root)
entry_strength.place(x=70, y=10)

entry_corner = Entry(root)
entry_corner.place(x=70, y=50)

attack_button = Button(root, text='Attack')
attack_button.bind('<Button-1>')
attack_button.place(x=5, y=90)

reset_button = Button(root, text='Reset')
reset_button.bind('<Button-1>')
reset_button.place(x=70, y=90)

root.mainloop()
