import time
import thread
import threading

import PiProtoSettings as s
from PIL, import Image


def main():

	#Subject to removal: 
	#Array that stores locations of ALL cropped images to be easily fed
	#	to kernel -- Purpose is to skip several lines of code in long run
	imageLocations = []

	try:
		#New data needs to be pulled from CROP_DATA, not setup_data!
		#Data will be as follows:
		#box_data = [   [spot#, label,x0,y0,w,h,   ]  ... ]
		box_data = crop_data.boxes
	except:
		print "Issue in setup_data.py for setting up boxes"
		sys.exit()

	if not box_data:
		print "ERROR: boxes in setup_data.py is empty"
		sys.exit()
	else:
		print "INFO: box_data contains data!"

	cropLocation = "C:\Users\clams\Desktop\BOX\Updates 5-31-18\crop"
	grabLocation = "C:\Users\clams\Desktop\BOX\Updates 5-31-18\LotPic"
	extension = ".jpg"
	#iterations = len(box_data)
	numSpots = 24
	#MAX_LOOPS will == the # of pictures taken since they overlap continuously
	availablePics = s.MAX_LOOPS + 1

	#Looking through 100 pictures
	for i in range(availablePics):
		lotLocation = grabLocation + str(i) + extension
		lotImage = Image.open(lotLocation)

		for j in range(numSpots):
			cropNum = (numSpots * i) + j
			currSpot = box_data[i]

			#setup coordinates for crop
			x0 = currSpot[2]
			y0 = currSpot[3]
			xf = x0 + currSpot[4]
			yf = y0 + currSpot[5]

			#Create save destination, crop image and save to destination
			croppedImgLoc = cropLocation + str(cropNum) + extension
			croppedImage = lotImage.crop(x0, y0, xf, yf)
			croppedImage.save(croppedImgLoc)

			imageLocations.append(croppedImgLoc)


main()
