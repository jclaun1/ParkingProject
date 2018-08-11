from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter.font
from PIL import Image,ImageTk
from tkinter import filedialog
import os


FRAME_WIDTH = 1700
FRAME_HEIGHT = 980

def rbg_option():
    global appCanvas
    appCanvas = Canvas(mailbox_frame, bg="red", width=100, height=200)
    appCanvas.grid(row=10,column=1)

def ml_option():
    print("ml_option")


def browse_button():
    global File, w, img, imgWidth, imgHeight,original, rightCanvas

    #Chooses image file
    File = filedialog.askopenfilename(parent=root, initialdir="M:/", title='Choose an image.')
    original = Image.open(File)
    img = ImageTk.PhotoImage(original)
    imgWidth, imgHeight = original.size

    #Creates canvas that will display graphic
    rightCanvas=Canvas(rightFrame,bg="gray",width=imgWidth,height=imgHeight,scrollregion=(0,0,imgWidth,imgHeight)) 
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

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line')

def file_save():
    saveFile = filedialog.asksaveasfile(mode='w', defaultextension=".JPG")
    if saveFile is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(0.0, END)) # starts from `1.0`, not `0.0`
    saveFile.close()
    saveimage = text2save + '.JPG'
    cropped_img.save(saveimage)
    

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
    if (count % 2 == 0):
        print("count : ", count)
        w, h = original.size
        if messagebox.askyesno("Title", "Is this a Parking Space?") == True:
            currentLabel = 1
            spotLabels.append(currentLabel)
        else:
            currentLabel = 0
            spotLabels.append(currentLabel)

        

        area = (xVals[count-2],yVals[count-2] ,xVals[count-1] , yVals[count-1])
    
        cropped_img = original.crop(area) 
        print("area : ", area)                                                                                                                                                     
        cropped_img.show()
        saveimage = "test" + str(i) + '.JPG'
        cropped_img.save(saveimage)

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
root.geometry('1620x900')
root.configure(background='misty rose')
root.title("Parking Project")

############################# Creating Frame on the Left side of the GUI #############################
frame = Frame(root,width=100, height=100)
frame.pack(side = LEFT, fill = BOTH, expand = True) #padding provides a nice border between the root and the left frame  
'''leftCanvas = Canvas(frame, bg = 'white')
leftCanvas.pack(side = RIGHT, fill = BOTH, expand = True)
leftCanvas.create_text(155,10,fill="black",font="Times 20 italic bold",text="Add Notes")'''
mailbox_frame = Frame(frame, width = 10, height=10, bg = 'gray86')
mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

noteTab = ttk.Notebook(mailbox_frame)
tabFrame = Frame(noteTab, bg="gray86",width=200, height=200)
tabFrame2 = Frame(noteTab, bg="white",width = 200, height=200)
tabFrame3 = Frame(noteTab, width=200, height=200)
noteTab.add(tabFrame,text="Info")
noteTab.add(tabFrame2, text="RGB ")
noteTab.add(tabFrame3, text="ML")
NewTree= ttk.Treeview(tabFrame,height=20)
NewTree['show'] = 'headings'
NewTree["columns"]=("1","2","3")
NewTree.column("1", width=120)
NewTree.column("2", width=100)
NewTree.column("3", width=100)
NewTree.heading("1", text="Date")
NewTree.heading("2", text="(x,y)")
NewTree.heading("3", text="Parking Lot #")
NewTree.grid(row=2,column=0,pady=0,padx=0)

NewTree3= ttk.Treeview(tabFrame3,height=20)
NewTree3['show'] = 'headings'
NewTree3["columns"]=("1","2","3")
NewTree3.column("1", width=120)
NewTree3.column("2", width=100)
NewTree3.column("3", width=100)
NewTree3.heading("1", text="Date")
NewTree3.heading("2", text="(x,y)")
NewTree3.heading("3", text="File Saved")
NewTree3.grid(row=2,column=0,pady=0,padx=0)
noteTab.pack(fill=BOTH, expand=True)

lbl1 = Label(tabFrame,bg="gray86", fg="black",text="Section Number: ").grid(row=15,sticky=W,pady=5,padx=5)
e1 = Entry(tabFrame)

tools_canvas3 = Canvas(tabFrame3, width=330,height=50, bg="pink")
tools_canvas3.grid(row=1,column=0)
ml_crop = Button(tabFrame3, text='Crop', command=ml_option,pady=10, padx=10,)
ml_crop.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
mlcrop_window = tools_canvas3.create_window(10, 10, anchor=NW, window=ml_crop)

view_crops = Button(tabFrame3, text='View Images', command=ml_option,pady=10, padx=10,)
view_crops.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
viewcrops_window = tools_canvas3.create_window(200, 10, anchor=NW, window=view_crops)

############################# Adding text widget to mailbox_frame #############################
txt = Text(mailbox_frame, bg="white", width =50 ,height = 2, insertborderwidth=2, relief=SUNKEN, wrap = WORD,spacing1=2)
txt.insert(INSERT, "Click in this box to add notes!")
txt.pack(fill=BOTH, pady=5, padx=5, expand=True,) 



############################# New Frame #############################
'''optionFrame = Frame(mailbox_frame, bg="light grey", width=200, height=900)
optionFrame.pack(fill=BOTH, pady=5, padx=5, expand=True)
lbl1 = Label(optionFrame, bg="light grey",text="Section Number: ").grid(row=0,sticky=W)
lbl2= Label(optionFrame, bg="light grey",text="Spot Number : ").grid(row=2,sticky=W)
lbl3 = Label(optionFrame, bg="light grey",text = "Date :").grid(row = 4, sticky=W)
bttn1 = Button(optionFrame, )
e1 = Entry(optionFrame)
e2 = Entry(optionFrame)
e3 = Entry(optionFrame)
e1.grid(row=0, column=1)
e2.grid(row=2, column=1)
e3.grid(row=4, column =1)

RBG__button = Button(mailbox_frame, height=2, width=0, text="RBG Option", fg="black",command=rbg_option)
RBG__button.pack(side=LEFT, pady=5, padx=5)
ML_button = Button(mailbox_frame, height=2, width=0, text="ML Option", fg="black",command=ml_option)
ML_button.pack(side=LEFT, pady=5, padx=5)'''


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


'''shapes_menu = Menu(menu_bar)
shapes_menu.add_command(label="Rectangle", command = create_rectangle)
shapes_menu.add_separator()
#shapes_menu.add_command(label="Line", command = create_line)
menu_bar.add_cascade(label="Shapes", menu=shapes_menu)'''


search_menu = Menu(menu_bar)
search_menu.add_command(label="Search",command=find_text)
menu_bar.add_cascade(label="Search", menu=search_menu)
#Menu options to choose font
font_menu = Menu(menu_bar)
choose_fontMenu = Menu(menu_bar)
choose_size = Menu(menu_bar)
for name in sorted(tkinter.font.families()):
    fontChosen = choose_fontMenu.add_command(label=name)


for i in range(70):
    choose_size.add_command(label=i)

font_menu.add_cascade(label="Choose Font", menu=choose_fontMenu)
font_menu.add_cascade(label="Choose Size", menu=choose_size)
menu_bar.add_cascade(label="Fonts", menu=font_menu)

root.mainloop()
