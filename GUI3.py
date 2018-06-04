# w2tk.py   python using Tkinter, see web for documentation                                                                   
from Tkinter import *
root=Tk()
root.title('w2tk.py  connect points ')
width=400
height=300
npoint=0
x=[]
y=[]

c=Canvas(root, width=width, height=height, bg='white')
c.create_line(      20,        20, width-20,        20, fill='black')
c.create_line(      20,        20,       20, height-20, fill='black')
c.create_line(width-20,        20, width-20, height-20, fill='black')
c.create_line(      20, height-20, width-20, height-20, fill='black')
c.create_text(width/2, 10, text='press left button for point, press right button to connect', fill='black')
c.create_text(width/2, height-10, text='press to exit', fill='black')

def mouseB1press(event): # left                                                                                               
  global x, y, npoint, width, height
  if event.y>height-20:
    sys.exit()

  if npoint==0:
    c.delete(ALL)
    c.create_line(      20,        20, width-20,        20, fill='black')
    c.create_line(      20,        20,       20, height-20, fill='black')
    c.create_line(width-20,        20, width-20, height-20, fill='black')
    c.create_line(      20, height-20, width-20, height-20, fill='black')
    c.create_text(width/2, 10, text='press left button for point, press right button to connect', fill='black')
    c.create_text(width/2, height-10, text='press to exit', fill='black')


  x.append(event.x)
  y.append(event.y)
  c.create_oval(x[npoint]-2,y[npoint]-2,x[npoint]+2,y[npoint]+2, fill='red')
  npoint = npoint + 1

def mouseB3press(event): # right                                                                                              
  global x, y, npoint, width, height
  if event.y>height-20:
    sys.exit()

  for i in range(0,npoint-1):
    for j in range(i+1,npoint):
      c.create_line(x[i],y[i],x[j],y[j],fill='blue')

  npoint=0
  x=[]
  y=[]

c.bind('<ButtonPress-1>'  , mouseB1press)
c.bind('<ButtonPress-3>'  , mouseB3press)

c.pack()
root.mainloop()
