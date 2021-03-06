from tkinter import*
from tkinter import messagebox
import tkinter.font
from PIL import Image,ImageTk
from tkinter import filedialog
import os


FRAME_WIDTH = 1500
FRAME_HEIGHT = 980
def browse_button():
    global File, w, img, imgWidth, imgHeight,original, rightCanvas

    #Chooses image file
    File = filedialog.askopenfilename(parent=root, initialdir="M:/", title='Choose an image.')
    original = Image.open(File)
    img = ImageTk.PhotoImage(original)
    imgWidth, imgHeight = original.size

    #Creates canvas that will display graphic
    rightCanvas=Canvas(rightFrame,bg="white",width=FRAME_WIDTH,height=FRAME_HEIGHT,scrollregion=(0,0,imgWidth,imgHeight)) 
    rightCanvas.image = img
    rightCanvas.create_image(0,0, image=img, anchor="nw")  
    hbar=Scrollbar(rightFrame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=rightCanvas.xview)
    vbar=Scrollbar(rightFrame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=rightCanvas.yview)
    rightCanvas.config(width=FRAME_WIDTH,height=FRAME_HEIGHT)
    rightCanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    rightCanvas.pack(side=LEFT,expand=True,fill=BOTH) 
    
def file_save():
    saveFile = filedialog.asksaveasfile(mode='w', defaultextension=".JPG")
    if saveFile is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(0.0, END)) # starts from `1.0`, not `0.0`
    saveFile.close()
    saveimage = text2save + '.JPG'
    cropped_img.save(saveFile)
    

def crop_button():

    rightCanvas.bind("<Button 1>", printcoords)
    return

def printcoords(event):

    global count,xVals, yVals, spotLabels, currentLabel, cropped_img
    
    #Mouse clicking event     
    x = rightCanvas.canvasx(event.x)
    y = rightCanvas.canvasy(event.y)
    xVals.append(x)
    yVals.append(y)
    rightCanvas.create_oval(xVals[count]-2,yVals[count]-2,xVals[count]+2,yVals[count]+2, fill='red')
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

        fileImage = Image.open(File)
        cropped_img = original.crop(area)                                                                                                                                                      
        cropped_img.show()
        '''saveimage = "test" + str(i) + '.JPG'
        cropped_img.save(saveimage)'''

def cut_button():
    txt.event_generate("<<Cut>>")

def copy_button (evt=None):
    widget = root.focus_get()
    if isinstance(widget, Entry):
        if widget.selection_present():
            widget.clipboard_clear()
            widget.clipboard_append(widget.selection_get())
    else:
    # works for Text, not for Entry (why?); fails quietly
        widget.tk.call('tk_textCopy', widget._w)


def paste_button():
    txt.event_generate("<<Paste>>")
    return

def undo():
    txt.event_generate("<<Undo>>")
    return

def redo():
    txt.event_generate("<<Redo>>")
    return

def select_all(evt=None):
        widget = root.focus_get()
        if isinstance(widget, Text):
            # the following commented-out code fails on MacPython
            # because the tk commands themselves aren't recognized;
            # hence I am not sure if the code is correct
            print ("Cannot yet 'Select All' in Text widgets")
    #       widget.tk_textResetAnchor("1.0")
    #       widget.tk_textSelectTo(END)
        elif isinstance(widget, Entry):
            widget.selection_range(0, END)
            widget.icursor(0)


def find_text(event=None):
    print("find text")
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0,
           command=lambda: search_output(
               search_entry_widget.get(), ignore_case_value.get(),
               content_text, search_toplevel, search_entry_widget)
           ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)

def search_output(needle,if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove('match','1.0', END)
    matches_found=0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle,start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break

            end_pos = '{} + {}c'. format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found +=1
            start_pos = end_pos
        content_text.tag_config('match', background='yellow', foreground='blue')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))

def highlight_line(interval=100):
    textPad.tag_remove("active_line", 1.0, "end")
    textPad.tag_add("active_line", "insert linestart", "insert lineend+1c")
    textPad.after(interval, toggle_highlight)

def undo_highlight():
    textPad.tag_remove("active_line", 1.0, "end")

def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()


def create_rectangle():
    global object_id, rectangelCanvas
    rectangelCanvas = Canvas(rightCanvas,bg="white", height=300, width=300)
    rectangelCanvas.pack(side=RIGHT)
    rectangelCanvas.bind("<Button-1>",click)

    object_id = rectangelCanvas.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3)


def exit():
    rightCanvas.unbind("<Button 1>")

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

############################# Constructing tk() object ###################################                                                                                                                                                                                       \
root = Tk()
root.geometry('1280x900')
root.configure(background='misty rose')
root.title("Parking Project")


############################# Creating Frame on the Left side of the GUI #############################
frame = Frame(root, width=200, height=200)
frame.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)  
leftCanvas = Canvas(frame, bg = 'light grey')
leftCanvas.pack(side = RIGHT, fill = BOTH, expand = True)
leftCanvas.create_text(0,0,fill="darkblue",font="Times 20 italic bold",text="Add Notes")
mailbox_frame = Frame(leftCanvas, bg = 'white')

############################# Adding text widget to mailbox_frame #############################
txt = Text(mailbox_frame, bg="white", height = 25, insertborderwidth=2, relief=SUNKEN, wrap = WORD,spacing1=2)
txt.insert(INSERT, "Click in this box to add notes!")
txt.pack(fill=BOTH, pady=5, padx=5, expand=True,) 
canvas_frame = leftCanvas.create_window((0,0),window=mailbox_frame, anchor = NW)
var = StringVar(root)

############################# New Frame #############################
optionFrame = Frame(mailbox_frame, bg="light grey", width=200, height=900)
optionFrame.pack(fill=BOTH, pady=5, padx=5, expand=True)
lbl1 = Label(optionFrame, text="Section Number: ").grid(row=0,sticky=W)
lbl2= Label(optionFrame, text="Spot Number : ").grid(row=2,sticky=W)
lbl3 = Label(optionFrame, text = "Date :").grid(row = 4, sticky=W)
bttn1 = Button(optionFrame, )
e1 = Entry(optionFrame)
e2 = Entry(optionFrame)
e3 = Entry(optionFrame)
e1.grid(row=0, column=1)
e2.grid(row=2, column=1)
e3.grid(row=4, column =1)
'''lbl1.pack(side=LEFT, padx=5, pady=5)   
entry1 = Entry(optionFrame)
entry1.pack(fill=BOTH, padx=5, expand=True)   
frame2 = Frame(optionFrame)
frame2.pack(fill=X) '''
       
############################# Creating Frame Where Graphic is displayed #############################
rightFrame=Frame(root,width=FRAME_WIDTH,height=FRAME_HEIGHT)
rightFrame.config(bg="light grey")
rightFrame.pack()    

############################# Adding Top level menu option #############################
menu_bar = Menu(root)
root.configure(menu=menu_bar)
file_menu = Menu(menu_bar)
file_menu.add_command(label = "Browse", command=browse_button)
file_menu.add_separator()
file_menu.add_command(label="Save as...", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = Menu(menu_bar)
edit_menu.add_command(label = "Crop Image", command=crop_button)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command=cut_button)
edit_menu.add_separator()
edit_menu.add_command(label = "Copy", command=copy_button)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste_button)
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command=undo)
edit_menu.add_separator()
edit_menu.add_command(label = "Redo", command=redo)
hltln = IntVar()
edit_menu.add_command(label="Highlight Current Line",command=toggle_highlight)
menu_bar.add_cascade(label="Edit", menu=edit_menu)


shapes_menu = Menu(menu_bar)
shapes_menu.add_command(label="Rectangle", command = create_rectangle)
shapes_menu.add_separator()
#shapes_menu.add_command(label="Line", command = create_line)
menu_bar.add_cascade(label="Shapes", menu=shapes_menu)


search_menu = Menu(menu_bar)
search_menu.add_command(label="Search",command=find_text)
menu_bar.add_cascade(label="Search", menu=search_menu)
#Menu options to choose font
font_menu = Menu(menu_bar)
choose_fontMenu = Menu(menu_bar)
choose_size = Menu(menu_bar)
for name in sorted(tkinter.font.families()):
    choose_fontMenu.add_command(label=name)

txt.configure
for i in range(70):
    choose_size.add_command(label=i)

font_menu.add_cascade(label="Choose Font", menu=choose_fontMenu)
font_menu.add_cascade(label="Choose Size", menu=choose_size)
menu_bar.add_cascade(label="Fonts", menu=font_menu)

root.mainloop()
