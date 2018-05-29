import sys
import time

#Initial Data
import PiProtoSettings as s
"""
try:
	import picamera
except ImportError:
	print  "Error: PiCamera module needs to be installed"
	sys.exit()
"""

# ---------------------------------------------------------- #

def setup_camera(is_fullscreen = True):

	camera = picamera.PiCamera()
	camera.resolution = s.PICTURE_RESOLUTION
	camera.preview_fullscreen = is_fullscreen
	camera.awb_mode = "off"

	if not is_fullscreen: camera.preview_window = s.CAMERA_WINDOW_SIZE
	time.sleep(s.WAKEUP_DELAY) # wake-up time = 2 seconds

	return camera

def load_image(filename):

	print "INFO: Loading Image: " + str(filename)
	image = Image.open(filename)
	pixels = image.load()
	print "INFO: Image loaded"
	return (image, pixels)

def test(filename):

	image, pixels = load_image(str(filename))
	#Number values subject to change
	test_area = get_area_average(pixels, 50, 600, 620, 50)
	expected_area = get_area_average(pixels, 1500, 600, 300, 300)

	compare_area(test_area, expected_area)

def get_area_average(pixels, x, y, w, h):
	#Color scale here
	#x, y = starting coordinates
	#w, h = width/height

	#number of evaluation points
	numPoints = 5
	
	#setup
	totals = [0, 0, 0, 0]
	
	#RGB/color values
	for i in range(x, x + w):
		for j in range(y, y + h):
			for x in range(numPoints):
				totals[x] += pixels[i, j][x]


	#Calculate number of pixels in the area
	numPixels = w * h
	for i in range[numPoints]:
		totals[i] /= numPixels

	return totals


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
		