import time
import picamera
from PIL import Image

def BW(imagePath, imageDestination):
        color_image = Image.open(imagePath)
        bw = color_image.convert('1')
        bw.save(imageDestination)
        
if __name__ == '__main__':
        location = "/home/pi/BOX/BoxPic4.jpg"
        destination = "/home/pi/BOX/BoxPic5.jpg"
        #        BW(location, destination)
        camera = picamera.PiCamera()
        camera.resolution = (2592, 1944)
        camera.capture(location)
        img = Image.open(location)
        img = img.transpose( Image.FLIP_TOP_BOTTOM )
        img = img.transpose( Image.FLIP_LEFT_RIGHT )
        img.save(destination)


        """
        with picamera.PiCamera() as camera:
                for each in range(1):
                        camera.start_preview()
                        camera.capture(location)
                        time.sleep(5)
                        #BW(location)
                        camera.stop_preview"""
                        
		
