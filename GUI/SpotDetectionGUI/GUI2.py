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
    return

def label_button():

    global currentLabel
    if messagebox.askyesno("Title", "Is this a Parking Space?") == True:
        currentLabel = 1
    else:
        currentLabel = 0
    print ("currentLabel ," ,currentLabel)
    spotLabels.append(currentLabel)

    print(spotLabels[0])

def printcoords(event):

    global count,xVals, yVals, currentLabel, spotLabels
    #Mouse clicking event                                                                                                          
    xVals.append(event.x)
    yVals.append(event.y)
    count = count + 1

def exit():
    w.unbind("<Button 1>")

    #Array of SPOTS (arrays)                                                                                                       
    fileData = []

    #Original Spot Number = -1      --  Check nested for loop for explanation                                                      
    spotIndex = -1
    global spotLabels
    numberLabel = -1
 #Writing to a python file now for easy data transfer to other files                                                            
    newFile = open('data_setup.py', 'w')

    print(count)
    for i in range(count):

        #Instance where i%2 -->                                                                                                    
        #>  Increase spot counter                                                                                                  
        #>  Add a new spot into array holding spots                                                                                
        #>  Append spot number and label to the new inner array                                                                    
        if (i % 2) == 0:
            spotIndex += 1
            #Create a new spot with no value                                                                                       
            fileData.append([])
            if spotLabels[i] == 1:
                numberLabel += 1
                fileData[spotIndex].append(numberLabel+1)
            elif spotLabels[i] == 0:
                fileData[spotIndex].append(0)
            fileData[spotIndex].append(spotLabels[i])

        #To each individual spot, will add x0 and y0, followed by xf and yf upon next loop iteration                               
        fileData[spotIndex].append(xVals[i])
        fileData[spotIndex].append(yVals[i])

    #repr(fileData) takes the 2D array and converts it into string format to be written to the file                                
    newFile.write("boxes = " + repr(fileData) + "\n")
    newFile.close()

    quit()

#Global variable 'spotLabel' == { 0 if control space | 1 if parking space}                                                         
spotLabels = [] #Array of labels for each click                                                                                    
count = 0
xVals = []
yVals = []

#Constructing tk() object                                                                                                          
root = Tk()
root.geometry('1000x1000')
root.configure(background='pink')
root.title("Python GUI")
root.title("Python GUI")

#Adding Top level menu options                                                                                                     
menu_bar = Menu(root)
root.configure(menu=menu_bar)

file_menu = Menu(menu_bar)
file_menu.add_command(label = "Browse", command=browse_button)
file_menu.add_separator()
file_menu.add_command(label = "Crop", command=crop_button)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

options_menu = Menu(menu_bar)
options_menu.add_command(label = "Change Label", command=label_button)
menu_bar.add_cascade(label="Options", menu=options_menu)


'''browsebutton = Button(root, text="Browse", command=browse_button).pack()                                                        
cropButton = Button(root, text="Crop", command=crop_button).pack()                                                                 
labelButton = Button(root, text="Change Label", command=label_button).pack()'''
#exitButton = Button(root, text = "Exit", command=exit).pack()                                                                     

root.mainloop()
