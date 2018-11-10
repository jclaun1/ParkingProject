from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#Creating the display window
window = tk.Tk()
window.title("Camera 1")
window.geometry("1920x1080")

#Test Image
image = Image.open("testpic1.gif")
image = image.resize((1920, 750), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

photo1 = tk.Label(image=photo)
photo1.image= photo
photo1.grid(row=0, column=0, columnspan = 60, sticky=W)


#Camera indication label
label1 = tk.Label(text="Camera", borderwidth=2, relief="solid", width=16, height=4, bg="gray", fg="black")
label1.grid(row=1, rowspan = 2, column=0, sticky=W)

label2 = tk.Button(text="Center", borderwidth=2, relief="solid", width=15, height=4, bg="white", fg="black")
label2.grid(row=3, rowspan = 2, column=0, sticky=W)

label3 = tk.Button(text="Left", borderwidth=2, relief="solid", width=15, height=4, bg="white", fg="black")
label3.grid(row=5, rowspan = 2, column=0, sticky=W)

label4 = tk.Button(text="Right", borderwidth=2, relief="solid", width=15, height=4, bg="white", fg="black")
label4.grid(row=7, rowspan = 2, column=0, sticky=W)




#Centered control arrows
label5 = tk.Button(text="UP", borderwidth=2, relief="solid", width=7, height=2, activebackground="gray")
label5.grid(row=1, column=30,  pady=0)

label6 = tk.Button(text="DOWN", borderwidth=2, relief="solid", width=7, height=2, activebackground="gray")
label6.grid(row=4, column=30, sticky=S, pady=0)

label7 = tk.Button(text="LEFT", borderwidth=2, relief="solid", width=7, height=2, activebackground="gray")
label7.grid(row=2, rowspan = 2, column=29, sticky=W)

label8 = tk.Button(text="RIGHT", borderwidth=2, relief="solid", width=7, height=2, activebackground="gray")
label8.grid(row=2, rowspan = 2, column=31, sticky=E)

degree = StringVar()
xdegree = StringVar()
ydegree = StringVar()
entrybox = Entry(window, textvariable = degree, width = 5, bg = "lightblue")
entrybox.grid( row = 2, rowspan = 2, column = 30)

xbox = Entry(window, textvariable = xdegree, width = 5, bg = "lightblue")
xbox.grid( row = 3, column = 39, sticky = S)

ybox = Entry(window, textvariable = ydegree, width = 5, bg = "lightblue")
ybox.grid( row = 3, column = 41, sticky = E)


label9 = tk.Label(text = "Custom Position:")
label9.config(font =("Courier", 15))
label9.grid(row = 1, column = 37, columnspan = 6, sticky = N)

label10 = tk.Label(text = "X:")
label10.config(font = ("Courier", 12))
label10.grid(row = 3, column = 38, sticky = W)

label11 = tk.Label(text = "Y:")
label11.config(font = ("Courier", 12))
label11.grid(row = 3, column = 40)

updatebutton = tk.Button(text = "Update", borderwidth = 2, relief = "solid", width = 10, height = 2, activebackground = "gray")
updatebutton.grid(row = 5, column = 38, columnspan = 4)

currentposlabel = tk.Label(text="Current Posistion:\n X: (value) Y: (value)", borderwidth = 2, relief = "solid", width = 28, height = 7, bg = "white", fg = "black")
currentposlabel.config(font = ("Courier", 12))
currentposlabel.grid(row = 1, rowspan = 4, column = 57, columnspan = 4)

previousposlabel = tk.Label(text="Previous Posistion:\n X: (value) Y: (value)", borderwidth = 2, relief = "solid", width = 28, height = 7, bg = "white", fg = "black")
previousposlabel.config(font = ("Courier",12))
previousposlabel.grid(row = 5, rowspan = 4, column = 57, columnspan = 4)

window.mainloop()        

