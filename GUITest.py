
import Tkinter as tk
import tkMessageBox
import thread
import time
import urllib

from PIL import Image, ImageTk

import senddata
import imageread
import data.settings as s

try:
    # check setup_data exists
    import setup_data
except ImportError:
    # oh noes, it doesn't =(
    print ("ERROR: setup_data.py does not exist. Run ./pipark_setup.py first.")
    sys.exit(1)

# global variables
app = None
camera = None
has_quit = False
occupancy = [None for i in range(10)]  # list of booleans. True for occupied, False for empty. None for no space.




def create_application():
	global app

	root = tk.Tk()
	#app = MainApplication(master = root)
    #app.master.title("Eskititttttt")
    #app.mainloop()



def main():


	create_application()


if __name__ == "__main__":
        main()
