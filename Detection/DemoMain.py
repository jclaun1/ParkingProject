import thread
import threading
import time
#import urllib

import imagereadOLD
import PiProtoSettings as s
#import AlgorithmTest as tester

try:
    import picamera
    print("Init pi camera successfully")
except ImportError:
    print "ERROR: PiCamera Module needs to be installed."
    sys.exit(1)

try:
    import data_setup
except ImportError:
    print "ERROR: setup_data.py does not exist. Run ./pipark_setup.py first"
    sys.exit(1)


#globals
camera = None
has_quit = False
occupancy = [None for i in range(12)]


def run():
    global camera
    global occupancy

    image_location = "/home/pi/BOX/ColorTest"
    loop_delay = s.PICTURE_DELAY

    space_boxes, control_boxes = __setup_box_data()
    num_spaces = len(space_boxes)
    num_controls = len(control_boxes)

    print("Num Spaces = ", len(space_boxes))
    #assert num_spaces > 0
    #assert num_controls == 5

    #Settings defaults to be used in the first run of the day/test set
    previousVals = []
    checkAvgs = []
    
    
    prevAvailability = []
    """
    for i in range(num_spaces):
        previousVals.append([])
        checkAvgs.append(false)
        prevAvailability.append(true)
        for j in range(0, 5):
            previousVals[i].append(-1)
    """
    #camera = picamera.PiCamera()
    print("Approaching climax")
    camera = picamera.PiCamera()
    print("Nut")
    camera.resolution = (2592, 1944)
    print "Initialized Camera"

    for locNum in range(s.MAX_LOOPS):
	print("the fuck is going on")
        outputFileLocation = "outputData" + str(locNum) + ".txt"
	print("outputFileLocation")
        locationNum = str(locNum)
	print("Oof")
        space_averages = []
        control_averages = []
	print("yeet")
        startTime = time.time()
	print("Fuck")        
        try:
            loc = image_location + str(locationNum) + ".jpg"
	    print("Skin a skinny nigga")
            camera.capture(loc)
            print "Camera Just Captured and Image! Analyzing now.."
            print ""
            image = imageread.Image.open(loc)
            #image = image.transpose(imageread.Image.FLIP_TOP_BOTTOM)
            #image = image.transpose(imageread.Image.FLIP_LEFT_RIGHT)
            if s.NUM_COLORS == 1:
                image = image.convert('L')
                #image = image.convert('1')
            pixels = image.load()
                        
        except:
            print "Error while loading image"
            sys.exit(1)

	print("If you do jumping jacks and your titties don't move you're a boy")            
#################################################################################
        
        spaceIndex = 0
        for space in space_boxes:
            checkAvgs[spaceIndex] = checkCriticalAreas(critPoints, pixels, previousVals[spaceIndex])
            if checkAvgs[spaceIndex]:
                space_average = imageread.get_area_average(pixels, space[2], space[3], abs(space[2] - space[4]), abs(space[3] - space[5]))
                space_averages.append(space_average)
            spaceIndex += 1

#################################################################################
        
        controlIndex = 0
        for control in control_boxes:
            if checkAvgs[controlIndex]:
                control_average = imageread.get_area_average(pixels, control[2], control[3], abs(control[2] - control[4]), abs(control[3] - control[5]))
                control_averages.append(control_average)
            controlIndex += 1
            
#################################################################################

        counter = 1
        numSpots = 45
        numRows = 4
        checkIndex = 0
        outputBoxes = []
	print("Round 2")
        for i, space in zip(space_boxes, space_averages):
            couter = counter + 1
            num_controls = 0
            is_occupied = False

            for control in control_averages:
                if imageread.compare_area(space, control):
                    num_controls += 1

            if num_controls >= 3: is_occupied = True
            if is_occupied:
                print "x "
                outputBoxes.append("" + counter + " " + " " + 1 + " " + space[2] + " " + space[3] + " " + space[4] + " " + space[5] + "\n")
            else:
                print "o "
                outputBoxes.append("" + counter + " " + " " + 0 + " " + space[2] + " " + space[3] + " " + space[4] + " " + space[5] + "\n")

            if counter%(numSpots/numRows) == 0:
                print "\n"
	"""
            if previousVals[0][0] != -1:
                prevAvailability[checkIndex] = is_occupied
            checkIndex += 1

        
	for i in range(len(previousVals)):
            previousVals[i] = space_averages[i]
	"""
        print "It took ", (time.time() - startTime), " time to complete this run."
        print "\n\n"

        fileOutput = open(outputFileLocation, "w")
        fileOutput.write("SpotData = ", outputBoxes)
        fileOutput.close()

        imageread.time.sleep(loop_delay)
        
#---------------------------------------------------------------------------------------------------------#

def main():
    global has_quit
    global camera

    #tester.main()

    try:
        run()
    except:
        print "ERROR: Failed to start new thread. =("

    camera = picamera.PiCamera()
    camera.capture("a.jpg")
#---------------------------------------------------------------------------------------------------------#

def __setup_box_data():
    try:
        box_data = data_setup.boxes
	#print(data_setup.boxes)
	print(box_data)
        #pixel_data = setup_data.pixelBoundaries
    except:
        print "Issue in set_data.py for setting up box_data"
        sys.exit(0)

    if not box_data:
        print "ERROR: boxes in setup_data.py is empty!"
        sys.exit()
    else:
        print "INFO: box_data contains data!"
    
    space_boxes = []
    control_boxes = []

    counter = 0
    for data_set in box_data:
        print(data_set)
        if data_set[0] == 1: space_boxes.append(data_set) #space_boxes.append(pixelBoundaries[counter])
        elif data_set[0] == 0: control_boxes.append(data_set) #control_boxes.append(pixelBoundaries[counter])
        else: print "ERROR: Box-type not set to either 0 or 1."
        counter += 1

    print(space_boxes)	
    return space_boxes, control_boxes
    
#---------------------------------------------------------------------------------------------------------#



if __name__ == "__main__":
    main()
