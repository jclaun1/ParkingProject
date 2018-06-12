# test_mouse.py                                                                                                           
from tkinter import *
root=Tk()
root.title('test_mouse.py')
print ('test_mouse.py window gets mouse x,y')

def mouseMove(event):
  print ('mouse move x=')
  print (event.x)
  print (', y=')
  print (event.y)

def mouseB1press(event): # left                                                                                           
  print ('mouse B1 press x=')
  print (event.x)
  print (', y=')
  print (event.y)

def mouseB1up(event):
  print ('mouse B1 up x=')
  print (event.x)
  print (', y=')
  print (event.y)

def mouseB3press(event): # right                                                                                          
  print ('mouse B3 press x=')
  print (event.x)
  print (', y=')
  print (event.y)

def keyInput(event):
  print ("key input ", repr(event.char))

c=Canvas(root, width=400, height=400, bg='white')
c.create_rectangle(20,20,50,100,fill='blue')
c.bind('<B1-Motion>'      , mouseMove)
c.bind('<ButtonPress-1>'  , mouseB1press)
c.bind('<ButtonRelease-1>', mouseB1up)
c.bind('<ButtonPress-3>'  , mouseB3press)

c.pack()
root.mainloop()
=======
#File       
