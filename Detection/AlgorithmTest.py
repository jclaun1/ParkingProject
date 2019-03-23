import time
import math
import data_setup

def printPoints(allPixels, finalPixels, newLineSize):
    print("\n")
    counter = 0
    for point in allPixels:
        if point in finalPixels:
            print("O", end=" ")
        else:
            print("_", end=" ")
        if counter == newLineSize:
            counter = 0
            print("")
        else:
            counter+=1
    print("\n")

def removePixels(finalPixels, removalPixels):
    newPixels = []
    for point in finalPixels:
        if point not in removalPixels:
            newPixels.append(point)
    return newPixels

def main():
    
    box_data = data_setup.pixelBoundaries
    print(box_data)
    boundaries = data_setup.boxes
    spotIter = 0
    overallPixels = []
    for spot in box_data:
        boundary = boundaries[spotIter]
        xPixels = int(abs(boundary[2] - boundary[4]))
        yPixels = int(abs(boundary[3] - boundary[5])) 
        spotIter += 1
        #Populate these will all found pixels
        finalPixels = []
        allPixels = []
        for y in range(int(boundary[3]), int(boundary[5])):
            for x in range(int(boundary[2]), int(boundary[4])):
                finalPixels.append([x, y])
                allPixels.append([x, y])

        ##########################
        #Top Left
        pointOne = [spot[0], spot[1]]  
        #Bottom Left
        pointTwo = [spot[2], spot[3]]
        #Top Right
        pointThree = [spot[4], spot[5]]
        #Bottom Right
        pointFour = [spot[6], spot[7]]

        """
        print(pointOne)
        print(pointTwo)
        print(pointThree)
        print(pointFour)
        """

        ##########################

        if pointOne[0] == pointTwo[0]: slopeOneTwo = 0
        else:slopeOneTwo = (pointOne[1] - pointTwo[1])/(pointOne[0] - pointTwo[0])

        if pointOne[0] == pointThree[0]: slopeOneThree = 0
        else: slopeOneThree = (pointOne[1] - pointThree[1])/(pointOne[0] - pointThree[0])
        
        if pointFour[0] == pointTwo[0]: slopeTwoFour = 0
        else: slopeTwoFour = (pointFour[1] - pointTwo[1])/(pointFour[0] - pointTwo[0])

        if pointThree[0] == pointFour[0]: slopeThreeFour = 0
        else: slopeThreeFour = (pointFour[1] - pointThree[1])/(pointFour[0] - pointThree[0])

        lineOneTwo = [slopeOneTwo, (pointOne[1] - slopeOneTwo * pointOne[0])]
        lineOneThree = [slopeOneThree, (pointOne[1] - slopeOneThree * pointOne[0])]
        lineTwoFour = [slopeTwoFour, (pointFour[1] - slopeTwoFour * pointFour[0])]
        lineThreeFour = [slopeThreeFour, (pointFour[1] - slopeThreeFour * pointFour[0])]
        """
        print("lineOneTwo: ")
        print(lineOneTwo)
        print("lineOneThree: ")
        print(lineOneThree)
        print("lineTwoFour: ")
        print(lineTwoFour)
        print("lineThreeFour: ")
        print(lineThreeFour)
        """
        ##########################
        startTime = time.time()

        #Pixels accounted for by each line
        removalPixels = []
        pointIter = 0
        for point in finalPixels:
            yLineValueOne = lineOneThree[0] * point[0] + lineOneThree[1]
            yLineValueTwo = lineTwoFour[0] * point[0] + lineTwoFour[1]


            if slopeOneTwo == 0: xLineValueOne = pointOne[0]
            else: xLineValueOne = (point[1] - lineOneTwo[1])/lineOneTwo[0]
            
            if slopeThreeFour == 0: xLineValueTwo = pointThree[0]
            else: xLineValueTwo = (point[1] - lineThreeFour[1])/lineThreeFour[0]

            """
            if pointIter%15 == -50:
                print("yLineValueOne: {0}".format(yLineValueOne))
                print("yLineValueTwo: {0}".format(yLineValueTwo))
                print("xLineValueOne: {0}".format(xLineValueOne))
                print("xLineValueTwo: {0}".format(xLineValueTwo))
            """

            if point[1] < yLineValueOne or point[1] > yLineValueTwo or point[0] < xLineValueOne or point[0] > xLineValueTwo:
                removalPixels.append(point)

                #print("_", end=" ")
            """
            else:
                print("O", end = " ")
            pointIter += 1
            if pointIter % xPixels == 0:
                print()
            """

        finalPixels = removePixels(finalPixels, removalPixels)
        #printPoints(allPixels, finalPixels, xPixels)

        ##########################

        leftX = int((pointOne[0] + pointTwo[0])/2)
        rightX = int((pointThree[0] + pointFour[0])/2)
        topX = int((pointOne[0] + pointThree[0])/2)
        bottomX = int((pointFour[0] + pointTwo[0])/2)

        leftY = int((pointOne[1] + pointTwo[1])/2)
        rightY = int((pointThree[1] + pointFour[1])/2)
        topY = int((pointOne[1] + pointThree[1])/2)
        bottomY = int((pointFour[1] + pointTwo[1])/2)

        if slopeOneTwo == 0: horizontalSlope = 0
        else: horizontalSlope = (leftY - rightY)/(leftX - rightX)

        if slopeOneThree == 0: verticalSlope = 0
        else: verticalSlope = (topY - bottomY)/(topX - bottomX)

        horizontalLineMid = [horizontalSlope, (leftY - horizontalSlope * leftX)]
        verticalLineMid = [verticalSlope, (topY - verticalSlope * topX)]

        ##########################
        
        dYH = (abs(pointOne[1] - pointTwo[1]))

        horizontalLineTop = [horizontalSlope, horizontalLineMid[1] + dYH]
        horizontalLineBot = [horizontalSlope, horizontalLineMid[1] - dYH]

        dYV = (abs(pointOne[0] - pointThree[0]))

        verticalLineRight = [verticalSlope, verticalLineMid[1] + dYV]
        verticalLineLeft = [verticalSlope, verticalLineMid[1] - dYV]
        """
        print("dYH {0}".format(dYH))
        print("dYV {0}".format(dYV))
        print("HLT {0}".format(horizontalLineTop))
        print("HLB {0}".format(horizontalLineBot))
        print("VLR {0}".format(verticalLineRight))
        print("VLL {0}".format(verticalLineLeft))
        """
        ##########################

        for point in finalPixels:

            hLineB = horizontalLineBot[0] * point[0] + horizontalLineBot[1]
            hLineT = horizontalLineTop[0] * point[0] + horizontalLineTop[1]

            if verticalLineRight[0] == 0: vLineR = (leftY + rightY)/2 + dYV
            else: vLineR = (point[1] - verticalLineRight[1])/verticalLineRight[0]

            if verticalLineLeft[0] == 0: vLineL = (leftY + rightY)/2 - dYV
            else: vLineL = (point[1] - verticalLineLeft[1])/verticalLineLeft[0]

            #if point[1] < yLineValueOne or point[1] > yLineValueTwo or point[0] < xLineValueOne or point[0] > xLineValueTwo:
                #removalPixels.append(point)
            if point[1] > hLineT and (point[0] > vLineL or point[0] < vLineR):
                removalPixels.append(point)
            elif point[1] < hLineB and (point[0] > vLineL or point[0] < vLineR):
                removalPixels.append(point)

        finalPixels = removePixels(finalPixels, removalPixels)
        #print(finalPixels)
        ##########################

        finalTime = time.time()
        #printPoints(allPixels, finalPixels)
        print("\nTotal time is: {0}\n".format(finalTime - startTime))

        overallPixels.append(finalPixels)
        #print(len(finalPixels))
    newFile = open('setup_data.py', 'w')
    newFile.write("boxes = " + repr(boundaries) + "\n")
    newFile.write("pixelBoundaries = " + repr(overallPixels) + "\n")

    newFile.close()
main()
