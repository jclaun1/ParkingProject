import thread
import threading
import time
import sys
#import urllib

import imageread
import PiProtoSettings as s


try:
        import picamera
except ImportError:
        print "ERROR: PiCamera Module needs to be installed."
        sys.exit(1)

try:
	import setup_data
except ImportError:
	print "ERROR: setup_data.py does not exist. Run ./pipark_setup.py first"
sys.exit(1)



def main():
	global has_quit
	global camera
	
	#Takes in current locNum as and argument from command line
	image_location = "/home/pi/BOX/ColorTest"
	loop_delay = s.PICTURE_DELAY
	
	camera = picamera.PiCamera()
        camera.resolution = (2592, 1944)
        print "Initialized Camera"
	
	try:
		pixels = captureImage()
		startTime = time.time()
		loc = image_location + locationNum + ".jpg"
		camera.capture(loc)
		print "Camera Just Captured and Image! Analyzing now.."
		print ""
		image = imageread.Image.open(loc)
		image = image.transpose(imageread.Image.FLIP_TOP_BOTTOM)
		image = image.transpose(imageread.Image.FLIP_LEFT_RIGHT)
		if s.NUM_COLORS == 1:
			image = image.convert('L')
			#image = image.convert('1')
		#pixels = image.load()
		picTime = time.time() - startTime
		print("Picture Capture took: ", str(picTime))
		
		#pixelFile = open("pixels.txt", "w")
		#pixelFile.write(pixels)
		#pixelFile.close()
		#fileIOTime = time.time() - startTime
		#print "The time it took to write the pixels to a file was: ", str(fileIOTime)

	except:
		print "ERROR: Failed to start new thread."


if __name__ == "__main__":
	main()
