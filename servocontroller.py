# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import sys
# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths

servo_min = 125  # Min pulse length out of 4096
servo_max = 675 # Max pulse length out of 4096
servo_mid = 300
servo_mid_2 = 400
servo_mid_3 = 500
servo_zero = 0

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
#print('Moving servo on channel 0, press Ctrl-C to quit...')

numCameras = 3
MAX_CHANNELS = 2
degreeMultiplier = 3
servo_positions = [0, 1]
degreeArray = [0,0]
currentDegree = []
inputDegree = servo_min

#Assigning position matrices for each camera (1 element for each servo)
for i in range(numCameras):
    currentDegree.append(degreeArray)

while(True):
    print(currentDegree)
    print("Which camera would you like to check? We have " + str(numCameras) + " cameras available. Select the corresponding number")
    print("Input '0' to exit the program.")
    cameraChoice = int(input())

    #Assuring accurate camera choice
    while(cameraChoice <= 0 or cameraChoice > numCameras):
        if(cameraChoice == 0): sys.exit()
        print("Enter a number in the range 0 - " + str(numCameras))
        cameraChoice = int(input())

    #Begin Camera index at 0 after receiving valid input
    cameraChoice -= 1

    #Took out a maximum number of loops. This will now continue indefinitely until break statement:
    #finishCamera = False
    while(True):
        print("Which servo would you like to control?")
        print("  1. Left - Right")
        print("  2. Up - Down")
        print("  3. Exit Current Camera")
        currentServo = int(input()) - 1

        #Assuring accurate channel choice
        if(currentServo == 2): break
        while(currentServo >= MAX_CHANNELS or currentServo < 0):
            print("Enter a number in the range 1 - 3")
            currentServo = int(input()) - 1
        if(currentServo == 2): break

        #Assigns what channel we will be working with
        currentChannel = (MAX_CHANNELS * cameraChoice) + currentServo

        inputDegree = currentDegree[cameraChoice][currentServo]
        option = 0
        while(True):
            print("\nChoose an option:")
            print("  1. Input new degree for the servo")
            print("  2. Check the servo's current degree")
            print("  Enter any other input to exit the Current Channel\n")
            option = int(input())

            if(option == 1):
                for i in range(1):
                    inputDegree = int(input("Enter the degree you want to turn to.\n"))
                    while(inputDegree < 0 or inputDegree > 180):
                        inputDegree = int(input("The input has to be within a 1-180 range\n"))
                        newPos = servo_min + (inputDegree * degreeMultiplier)
                        pwm.set_pwm(currentChannel, 0, newPos)
                        time.sleep(1)
                        pwm.set_pwm(currentChannel, 0, servo_zero)
                        time.sleep(1)

            elif(option == 2):
                print("Current degree is " + str(currentDegree[cameraChoice][currentServo]))
            else:
                break

            currentDegree[cameraChoice][currentServo] = inputDegree #(inputDegree - 125)/3













