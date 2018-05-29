import thread
import threading
import time
#import urllib

#import senddata
import imageread
import PiProtoSettings as s


try:
    import setup_data
except ImportError:
    print "ERROR: setup_data.py does not exist. Run ./pipark_setup.py first"
    sys.exit(1)


#globals
camera = None
has_quit = False
#app = None
occupancy = [None for i in range(12)]


def run():
    global camera
    global occupancy
    
    print "Run 1"
        
    image_location = "/home/pi/BOX/BoxPic1.jpg"        #"./images/parkingPal.jpeg"
    loop_delay = s.PICTURE_DELAY

    space_boxes, control_boxes = __setup_box_data()
    print "Finished Setup"
    num_spaces = len(space_boxes)
    num_controls = len(control_boxes)

    print "Num spaces = ", num_spaces, " , Num Controls = ", num_controls
        
    assert num_spaces > 0
    assert num_controls == 3

    last_status = [None for i in range(10)]
    last_ticks = [3 for i in range(10)]

    print "Run 2"
        
    while(True):
        space_averages = []
        control_averages = []
        #camera.capture(image_location)
#
        try:
            image = imageread.Image.open(image_location)
            pixels = image.load()
        except:
            print "Error while loading image"
            sys.exit(1)

            print "Run 3"

        for space in space_boxes:
            space_x = space[2]
            space_y = space[3]
            space_w = abs(space[4])
            space_h = abs(space[5])

            if s.IS_VERBOSE:
                print "Info: Space", space[0], "dimensions:"
                print "     x: " , space_x, " y: ", space_y, " w: ", space_w, " h: ", space_h

            space_average = imageread.get_area_average(
                    pixels, 
                    space_x, 
                    space_y, 
                    space_w, 
                    space_h
            )
            print space_average
            space_averages.append(space_average)

        print "Run 4"
                
#################################################################################

                 
        for control in control_boxes:
                control_x = control[2]
                control_y = control[3]
                control_w = abs(control[4])
                control_h = abs(control[5])

                print "INFO: CP", control[0], "dimensions:"
                print "      x:", control_x, "y:", control_y, "w:", control_w, "h:", control_h
            
                        # append control average pixel to list of averages
                control_average = imageread.get_area_average(
                        pixels, 
                        control_x, 
                        control_y, 
                        control_w, 
                        control_h
                )
                control_averages.append(control_average)
    
        print "Run 5"
        counter = 0
        numSpots = 12

        for i, space in zip(space_boxes, space_averages):
            
            # number of control points that conflict with parking space reading
            num_controls = 0
            for control in control_averages:
                

                if imageread.compare_area(space, control):
                    num_controls += 1
                                        #print "Y",
                                #else:
                                        #print "N",


                is_occupied = False
                if num_controls >= 2: is_occupied = True


#****Update 5/26
                if s.IS_VERBOSE and is_occupied:
                    print "x ",
            #    print "=> Space", i[0], "is filled.\n"
                elif s.IS_VERBOSE and not is_occupied:
                    print "o ",
            #    print "=> Space", i[0], "is empty.\n"
                couter = counter + 1
                if counter == numSpots/2 or counter == numSpots:
                    print "\n"
#****




#################################################################################

        #print "INFO: New image saved to: ", image_location

        imageread.time.sleep(loop_delay)

def main():
        global has_quit
        global camera
        #global occupancy
        print "Main 1"
        #camera = imageread.setup_camera(is_fullscreen = False)
        print "Main 2"
        try:
            run()
        except:
            print "ERROR: Failed to start new thread. =("



def __setup_box_data():
        print "Setup 1"
        try:
            box_data = setup_data.boxes
            print "box_data completed successfully"
        except:
            print "Issue in set_data.py for setting up box_data"
            sys.exit(0)

        print "Setup 2"
       


        if not box_data:
            print "ERROR: boxes in setup_data.py is empty!"
            sys.exit()
        else:
            print "INFO: box_data contains data!"


        print "Setup 3"
        
        space_boxes = []
        control_boxes = []
    
        for data_set in box_data:
            if data_set[1] == 1: space_boxes.append(data_set)
            elif data_set[1] == 0: control_boxes.append(data_set)
            else: print "ERROR: Box-type not set to either 0 or 1."

        print "space boxes:", space_boxes, "\ncontrol boxes:", control_boxes
        print "Setup 4"
        return space_boxes, control_boxes

if __name__ == "__main__":
        main()
