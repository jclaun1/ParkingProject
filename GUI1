from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog


def browse_button():
    global File
    File = filedialog.askopenfilename(parent=root, initialdir="M:/", title='Choose an image.')
    print("opening %s" % File)
    return

def crop_button():

    global w
    w = Canvas(root, width=1000, height=1000)
    w.pack()

    #Displays image on tkinter canvas                                                                                       
    print("opening %s" % File)
    original = Image.open(File)
    original = original.resize((1000,1000)) #resize image                                                                   
    img = ImageTk.PhotoImage(original)
    w.image = img
    w.create_image(0, 0, image=img, anchor="nw")
    w.bind("<Button 1>", printcoords)
#    print("crop button")                                                                                                   
 #   print("count: ", count)                                                                                                
    return

def printcoords(event):

    global count,xVals, yVals
    #Mouse clicking event                                                                                                   
  #  print("Left Button")                                                                                                   
   # print (event.x,event.y)                                                                                                
    xVals.append(event.x)
    yVals.append(event.y)
    count = count + 1
#    print("count printcoords: ", count)                                                                                    
    #print("count: ", count)                                                                                                

#        print("(",xVals[0],yVals[0],") (",  xVals[1],yVals[1],")")                                                         
#        return                                                                                                             

def exit():
    w.unbind("<Button 1>")
    newFile = open("ParkProj.txt", "w")
    print(count)
    print("(",xVals[0],yVals[0],") (",  xVals[1],yVals[1],")")
    fileData = []
    for i in range(count):
        print("i", i)
        fileData.append([])
        fileData[i].append(i)

        print(xVals[i])
        fileData[i].append(xVals[i])
                print(yVals[i])
        fileData[i].append(yVals[i])

        print (fileData)
        newLine =''.join(str(fileData[i]))
        newFile.write(newLine + '\n')

    newFile.close
    quit()

#Constructing new tkinter object                                                                                            
count = 0
xVals = []
yVals = []
root = Tk()
root.geometry('1500x1500')
root.title("Python GUI")
browsebutton = Button(root, text="Browse", command=browse_button).pack()
cropButton = Button(root, text="Crop", command=crop_button).pack()
exitButton = Button(root, text = "Exit", command=exit).pack()
arrayCoords = []

root.mainloop()
