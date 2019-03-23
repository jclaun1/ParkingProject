import sys
import time

#Initial Data
import PiProtoSettings as s

try:
    import picamera
except ImportError:
    print  "Error: PiCamera module needs to be installed"
    sys.exit()

try:
    from PIL import Image
except ImportError:
    print "Error Importing PiCamera Module"
    sys.exit()
# ---------------------------------------------------------- #

def setup_camera(is_fullscreen = True):

    camera = picamera.PiCamera()
    camera.resolution = s.PICTURE_RESOLUTION
    camera.preview_fullscreen = is_fullscreen
    camera.awb_mode = "off"
    if not is_fullscreen: camera.preview_window = s.CAMERA_WINDOW_SIZE
    time.sleep(s.WAKEUP_DELAY) # wake-up time = 2 seconds
        
    return camera

# ---------------------------------------------------------- #

def load_image(filename):

    print "INFO: Loading Image: " + str(filename)
    image = Image.open(filename)
    pixels = image.load()
    print "INFO: Image loaded"
    return (image, pixels)

# ---------------------------------------------------------- #

def test(filename):

    image, pixels = load_image(str(filename))
    #Number values subject to change
    test_area = get_area_average(pixels, 50, 600, 620, 50)
    expected_area = get_area_average(pixels, 1500, 600, 300, 300)

    compare_area(test_area, expected_area)

# ---------------------------------------------------------- #

def get_area_average(pixels, spotPixels):
    print "Getting averages"
    #Number of colors to be tested
    numColors = s.NUM_COLORS
    #setup totals based on number of colors being used [1, 3]
    totals = [0]

    for i in range(numColors):
        totals.append(0)
    print "Initialized totals"

    #RBG/color values
    if numColors == 3:
	print "Num colors = 3"
        for currPixel in spotPixels:
	    print currPixel
            currX = currPixel[0]
            currY = currPixel[1]
            for i in range(numColors):
                totals[k] += pixels[currX, currY][k]
    elif numColors == 1:
	print "Num colors = 1"
        for currPixel in spotPixels:
            currX = currPixel[0]
            currY = currPixel[1]
            totals[0] += pixels[currX, currY]
    else:
        print "ERROR: Invalid number of colors in setup_data.py"

    #Calculate number of pixels in the area
    numPixels = len(spotPixels)
    for i in range(numColors):
        totals[i] /= numPixels
        totals[numColors] += totals[i]
                
    print totals[numColors]
    return totals

# ---------------------------------------------------------- #

def compare_area(test, expected):

    if not isinstance(test, list) or not isinstance(expected, list):
        raise ValueError("Arrays need to be lists.")
    if len(test) != len(expected):
        raise ValueError("Arrays need to be same length")
        
    different = False

    for test_value, expected_value in zip(test, expected):
        if abs(test_value - expected_value) > s.IMAGE_THRESHOLD:
            different = True
    return different
        
# ---------------------------------------------------------- #
 
def checkCriticalAreas(critPoints, pixels, previousVals):
    if previousVals[0] == -1:
        return true

    totalDiffCriticals = 0
    checkVals = [len(critPoints)]
    for i in range(0, len(critPoints)):
        currIndex = critPoints[i]
        currX = currIndex[0]
        currY = currIndex[1]
        if s.NUM_COLORS == 1:
            currRBG = pixels[currX, currY]
        else:
            currRBG = pixels[currX, currY][0] + pixels[currX, currY][1] +pixels[currX, currY][2]
        previousRBG = previousVals[i]

        if abs(previousRBG - currRBG) > 5:
            totalDiffCriticals += 1
    
    if totalDiffCriticals > (len(critPoints) + 1):
        return true

    return false            
# ---------------------------------------------------------- #
