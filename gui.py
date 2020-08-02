from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("The Deep Musicontia")
window.geometry('400x540')
window.resizable(0,0)

#Setting background image
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "bg-Image2.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = PhotoImage(file='output-onlinepngtools.png')

#adding a label
lbl = Label(window, image=img).pack(side="top")

frame = Frame(window)

tlbl = Label(window, text="Generate Music from given genre:", font = ('Verdana',15)).pack()

cimg = PhotoImage(file='images.png')
classicbutton = Button(frame,text="Classical", image=cimg , compound = BOTTOM, command= cgen)
classicbutton.pack()

jimg = PhotoImage(file='jazz (1).png')
jazzbutton = Button(frame, text="Jazz", image=jimg , compound = BOTTOM, command= jgen)
jazzbutton.pack()

himg = PhotoImage(file='hiphop.png')
hhbutton = Button(frame, text="Hip Hop", image=himg , compound = BOTTOM, hgen)
hhbutton.pack()

frame.pack(anchor='center')
C.pack()
window.mainloop()