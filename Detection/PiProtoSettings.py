from uuid import getnode as get_mac
PI_ID = get_mac()
CAMERA_WINDOW_SIZE = [0, 0, 0, 0]
PICTURE_RESOLUTION = [0, 0]
WAKEUP_DELAY = 5
PICTURE_DELAY = 5
PICTURE_RESOLUTION[0] = 960
PICTURE_RESOLUTION[1] = 540
CAMERA_WINDOW_SIZE[0] = 0
CAMERA_WINDOW_SIZE[1] = 0
CAMERA_WINDOW_SIZE[2] = 960
CAMERA_WINDOW_SIZE[3] = 540
MAX_PICTURES = 4
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
IS_VERBOSE = True
PARK_ID = 1
SERVER_PASS = "pi"
SERVER_URL = "http://10.173.33.129/pipark/server/"

NUM_COLORS = 3    #RBG=3 ; BW=1
MAX_LOOPS = 10
if NUM_COLORS == 1:    IMAGE_THRESHOLD = 13
elif NUM_COLORS == 3:  IMAGE_THRESHOLD = 40