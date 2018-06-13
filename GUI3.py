from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import os

def browse_button():
    global File
    File = filedialog.askopenfilename(parent=root, initialdir="M:/", title='Choose an image.')
    print("opening %s" % File)
    global w, img, imgWidth, imgHeight,original
    w = Canvas(root, width=1920, height=1200)
    w.pack()

    #Displays image on tkinter canvas                                                                                                                                                                           \
                                                                                                                                                                                                                 
    print("opening %s" % File)
    original = Image.open(File)
#    original = original.resize((1920,1600)) #resize image                                                                                                                                                      \
                                                                                                                                                                                                                 
    img = ImageTk.PhotoImage(original)
    w.image = img
    w.create_image(0, 0, image=img, anchor="nw")
    return

def crop_button():

    w.bind("<Button 1>", printcoords)
    return

def printcoords(event):

    global count,xVals, yVals, spotLabels, currentLabel
    #Mouse clicking event                                                                                                                                                                                       \
                                                                                                                                                                                                                 
    xVals.append(event.x)
    yVals.append(event.y)
    w.create_oval(xVals[count]-2,yVals[count]-2,xVals[count]+2,yVals[count]+2, fill='red')
    count = count + 1

    i = 0
    if (count % 2) == 0:

        if messagebox.askyesno("Title", "Is this a Parking Space?") == True:
            currentLabel = 1
            spotLabels.append(currentLabel)
        else:
            currentLabel = 0
            spotLabels.append(currentLabel)

        i = int(count/2)
        if i == 1:
            area = (xVals[i-1],yVals[i-1] , xVals[i], yVals[i])
        else:
            area = (xVals[i],yVals[i] , xVals[i+1], yVals[i+1])

        image = Image.open(File)
        cropped_img = image.crop(area)
        #filename, file_extension = os.path.splitext(File)                                                                                                                                                      \
                                                                                                                                                                                                                 
        cropped_img.show()
        saveimage = "test" + str(i) + '.JPG'
        cropped_img.save(saveimage)

def exit():
    w.unbind("<Button 1>")


    #Array of SPOTS (arrays)                                                                                                                                                                                    \
                                                                                                                                                                                                                 
    fileData = []

    #Original Spot Number = -1      --  Check nested for loop for explanation                                                                                                                                   \
                                                                                                                                                                                                                 
    spotIndex = -1

    numberLabel = -1
    #Writing to a python file now for easy data transfer to other files                                                                                                                                         \
                                                                                                                                                                                                                 
    newFile = open('data_setup.py', 'w')

    print (xVals)
    print (yVals)
    print (spotLabels)

    print(count)
    for i in range(count):

        #To each individual spot, will add x0 and y0, followed by xf and yf upon next loop iteration                                                                                                            \
                                                                                                                                                                                                                 
        if (i % 2) == 0:
            spotIndex += 1
            print ("spot index = ", spotIndex)
            print("fileData = ", fileData)
            #Create a new spot with no value                                                                                                                                                                    \
                                                                                                                                                                                                                 
            fileData.append([])
            if spotLabels[spotIndex] == 1:
                numberLabel += 1
                fileData[spotIndex].append(1)
                fileData[spotIndex].append(numberLabel+1)
            elif spotLabels[spotIndex] == 0:
                fileData[spotIndex].append(0)
                fileData[spotIndex].append(spotLabels[spotIndex])

        fileData[spotIndex].append(xVals[i])
        fileData[spotIndex].append(yVals[i])
        print("NEW fileData = ", fileData)
    #repr(fileData) takes the 2D array and converts it into string format to be written to the file                                                                                                             \
                                                                                                                                                                                                                 
    newFile.write("boxes = " + repr(fileData) + "\n")
    newFile.close()
    quit()


#Global variable 'spotLabel' == { 0 if control space | 1 if parking space}                                                                                                                                      \
                                                                                                                                                                                                                 
spotLabels = [] #Array of labels for each click                                                                                                                                                                 \
                                                                                                                                                                                                                 
count = 0
xVals = []
yVals = []

#Constructing tk() object                                                                                                                                                                                       \
                                                                                                                                                                                                                 
root = Tk()
root.geometry('1920x1600')
root.configure(background='pink')
root.title("Python GUI")
root.title("Python GUI")

#Adding Top level menu options                                                                                                                                                                                  \
                                                                                                                                                                                                                 
menu_bar = Menu(root)
root.configure(menu=menu_bar)

file_menu = Menu(menu_bar)
file_menu.add_command(label = "Browse", command=browse_button)
file_menu.add_separator()
file_menu.add_command(label = "Crop", command=crop_button)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.mainloop()
