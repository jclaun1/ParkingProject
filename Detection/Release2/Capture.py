def main():
	global has_quit
	global camera

	try:
		pixels = captureImage()
		startTime = time.time()
		pixelFile = open("pixels.txt", "w")
		pixelFile.write(pixels)
		pixelFile.close()
		fileIOTime = time.time() - startTime
		print "The time it took to write the pixels to a file was: ", str(fileIOTime)

	except:
		print "ERROR: Failed to start new thread."


if __name__ == "__main__":
	main()
