import time
import math

def printPoints(allPixels, finalPixels):
    print("\n")
    counter = 0
    for point in allPixels:
        if point in finalPixels:
            print("O", end=" ")
        else:
            print("_", end=" ")
        if counter == 99:
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
    xPixels = 100
    yPixels = 100

    #Populate these will all found pixels
    finalPixels = []
    allPixels = []
    for y in range(0, yPixels):
        for x in range(0, xPixels):
            finalPixels.append([x, y])
            allPixels.append([x, y])

    ##########################

    #Top Left
    pointOne = [5, 5]   
    #Bottom Left
    pointTwo = [5, 95]
    #Top Right
    pointThree = [95, 5]
    #Bottom Right
    pointFour = [95, 95]

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

    ##########################
    startTime = time.time()

    #Pixels accounted for by each line
    removalPixels = []
    for point in finalPixels:
        yLineValueOne = lineOneThree[0] * point[0] + lineOneThree[1]
        yLineValueTwo = lineTwoFour[0] * point[0] + lineTwoFour[1]

        if slopeOneTwo == 0: xLineValueOne = pointOne[0]
        else: xLineValueOne = (point[1] - lineOneTwo[1])/lineOneTwo[0]
        
        if slopeThreeFour == 0: xLineValueTwo = pointThree[0]
        else: xLineValueTwo = (point[1] - lineThreeFour[1])/lineThreeFour[0]

        if point[1] < yLineValueOne or point[1] > yLineValueTwo or point[0] < xLineValueOne or point[0] > xLineValueTwo:
            removalPixels.append(point)
    
    finalPixels = removePixels(finalPixels, removalPixels)
    printPoints(allPixels, finalPixels)

    ##########################

    leftX = int((pointOne[0] + pointTwo[0])/2)
    rightX = int((pointThree[0] + pointFour[0])/2)
    topX = int((pointOne[0] + pointThree[0])/2)
    bottomX = int((pointFour[0] + pointTwo[0])/2)

    """
    leftY = lineOneTwo[0] * leftX + lineOneTwo[1]
    rightY = lineThreeFour[0] * rightX + lineThreeFour[1]
    topY = lineOneThree[0] * topX + lineOneThree[1]
    bottomY = lineTwoFour[0] * bottomX + lineTwoFour[1]
    """

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
    
    dYH = .1 * (pointOne[1] + pointTwo[1])

    horizontalLineTop = [horizontalSlope, horizontalLineMid[1] + dYH]
    horizontalLineBot = [horizontalSlope, horizontalLineMid[1] - dYH]

    dYV = 1 * (pointOne[0] + pointThree[0])

    verticalLineRight = [verticalSlope, verticalLineMid[1] + dYV]
    verticalLineLeft = [verticalSlope, verticalLineMid[1] - dYV]

    print("dYH {0}".format(dYH))
    print("dYV {0}".format(dYV))
    print("HLT {0}".format(horizontalLineTop))
    print("HLB {0}".format(horizontalLineBot))
    print("VLR {0}".format(verticalLineRight))
    print("VLL {0}".format(verticalLineLeft))
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
    ##########################

    finalTime = time.time()
    printPoints(allPixels, finalPixels)
    print("\nTotal time is: {0}\n".format(finalTime - startTime))

    print(90*90)
    print(len(finalPixels))


main()
