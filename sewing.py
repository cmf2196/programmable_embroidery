''' 
Author: Connor Finn, Drew DePerro

This scrypt generates a .jef file which is used to program a programmable embroidery machine. The file generates zig zag stitches, 
so that the quality of stitch is maintained. A Koch snowflake fractal is generated. 
'''

import numpy as np
zagHeight = 2  # make things even changes
zagWidth = 5


def zigZag(angle, length, outFile , forward):      # this will create a zig zag line
    
    numStitch = round(length / zagHeight)
    if forward:
    	outFile += [int(- 5 * zagWidth * np.cos(np.radians(angle))) , int(5 *  zagWidth * np.sin(np.radians(angle)) ), ] 
    else:
    	outFile += [int(5 * zagWidth * np.cos(np.radians(angle))) , int(-5 * zagWidth * np.sin(np.radians(angle)) ), ] 
    
    for i in range(numStitch):
        x = 10 * zagWidth 
        y = 10 * zagHeight
       
        x = int(x)
        y = int(y)
        if forward:
            forward = False
        else:
            x = -1 * x
            forward = True
        


        x1 = int(x * np.cos(np.radians(angle))  + y * np.sin(np.radians(angle)))
        y1 = int( y * np.cos(np.radians(angle)) - x * np.sin(np.radians(angle)) ) 


        outFile += [x1,y1,]

    if forward:
        outFile += [int(5 * zagWidth * np.cos(np.radians(angle))) , int(-5 * zagWidth * np.sin(np.radians(angle)) ), ] 
    else: 

        outFile += [int(-5 * zagWidth * np.cos(np.radians(angle))) , int(5 *  zagWidth * np.sin(np.radians(angle)) ), ] 


# this generates the Koch snowflake
def snowflake(startAngle, lengthSide, level, depth,  outFile, forward): 
    if level == depth:
	    zigZag(startAngle , lengthSide , outFile , forward) 
    else:
    	lengthSide = int(lengthSide / 3)
    	snowflake(startAngle , lengthSide , level + 1 , depth, outFile, forward)    	
    	startAngle -= 60
    	snowflake(startAngle , lengthSide , level + 1 , depth, outFile, forward)
    	startAngle += 120
    	snowflake(startAngle , lengthSide , level + 1 , depth, outFile, forward)    	
    	startAngle -= 60
    	snowflake(startAngle , lengthSide , level + 1 , depth, outFile, forward)    	

def noNeg(outFile):
    for i in range(len(outFile)):
        if outFile[i] < 0:
            outFile[i] += 256 




def hod(outFile):
    outFile +=  [128, 16]         # "Last stitch" command code

    jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
                10, 0, 0, 0,    # Unknown number
                ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
                ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
                ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
                ord("0"), ord("0"), 99, 0,  # SS00
                1, 0, 0, 0,     # Number of physical threads (1)
                (len(outFile)//2) & 0xff, (len(outFile)//2) >> 8 & 0xff, 0, 0,     # Number of stitches
                3, 0, 0, 0,     # Sewing machine hoop             
    			50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                2, 0, 0, 0,         # Thread color (white)
                13, 0, 0, 0,        # Unknown number
                ] + outFile
     

    jefBytes = bytes(jefBytes)
    with open("stitches.jef", "wb") as f:
        f.write(jefBytes)


def main():

    while True:
        try:
            numSides = int(input("How many sides would you like for your Koch snowflake: "))
            if numSides <= 7 and numSides >= 3:
                break
            else:
                print("Enter a number between 3 and 7  ")
                continue
        except ValueError:
            print("Enter a number! ")

    while True:
        try:
            sideLength = float(input("What is your desired side length? Enter a number of centemeters: "))
            if sideLength <= 12 and sideLength>= 3:
                break
            else:
                print("Enter a lenght between 1 and 12 centemeters. ")
                continue
        except ValueError:
            print("Enter a number! ")

    while True:
        try:
            numRecur = int(input("How many Recursions for your Koch Snowflake?: "))
            if numRecur <= 5 and numRecur >= 0 :
                break
            else:
                print("Enter a number of recursions between 0 and 5.  ")
                continue
        except ValueError:
            print("Enter a number! ")

    sideLength *= 100 # convert to cm
    stitches = [128, 2, 0, 0,]  # initialize stitches

## This makes first snowflake
    forward = True  # initialize bool

    for i in range(numSides):
        angle = i * 360 / numSides 
        snowflake(angle, sideLength , 0 , numRecur, stitches, forward)


    errorX= 0
    errorY = 0
    numError = int((len(stitches) - 4) / 2)
    for i in range(numError):
        errorX += stitches[i * 2 + 4]
        errorY += stitches[i*2 + 5]
	
    stitches +=[128 , 2 , 0 , 0 , 0 , 0 , 0 , 0]    
    stitches += [-1 * errorX ,  -1 *errorY , ]
    forward = False



	### Like to put the slowing down code here ###



# this makes second 
    forward = False
    for i in range(numSides):
        angle = i * 360 / numSides 
        snowflake(angle, sideLength , 0 , numRecur, stitches, forward)




    noNeg(stitches)
    print(errorX , errorY)
    hod(stitches)

main()
