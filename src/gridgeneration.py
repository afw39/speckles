#imports
import numpy as np #for number stuff
import matplotlib.pyplot as plt # for the plots/visualisation


#inputs
def inputvalues():
    #need to see that the image size is the right height, might do this as a function to see if their will be enough speckles in the image, run it first to get the measurements and if not, then will run it again to see if they will change it? for now will leave it and im just gonna enter allowed values.
    imagewidth = int(input("What is the width of the speckle image in pixels? "))
    imageheight = int(input("What is the height of the speckle image in pixels? "))
    area = imagewidth * imageheight

    #   asking for speckle dimensions and seeing if they are at least 3 x 3
    speckles = True
    while speckles == True:
        specklewidth= int(input("How many pixels wide would you like the speckles to be? "))
        speckleheight= int(input("How many pixels tall would you like the speckles to be?  "))
        speckle_area = specklewidth * speckleheight
        if specklewidth < 3 or speckleheight < 3:
            print("Speckles must be at least 3 pixels wide and 3 pixels tall. Please try again.")
            speckles = True
        elif speckle_area > 9 and (speckleheight and specklewidth) > 3:
            speckles = False
        else:
            speckles = False
    # maybe should also add that there needs to be a certain number of speckles per image (maybe put both the image questions and the speckle questions in the same loop)


    # asking for the black and white balance and making sure the value is between 0.0 and 1.0
    bw = True
    while bw == True:
        bwbalance = float(input("By entering a value between 0.0 and 1.0, enter the value of the black/white balance (0.0 is pure black, 1.0 is pure white). "))
        if bwbalance < 0.0 or bwbalance > 1.0:
            print("Incorrect value. Please enter a value between 0.0 and 1.0.")
            bw = True
        else:
            bw = False

    return imagewidth, imageheight, area, specklewidth, speckleheight, speckle_area, bwbalance

imagewidth, imageheight, area, specklewidth, speckleheight, speckle_area, bwbalance = inputvalues()

# try and generate a grid using matplotlib
def testgrid():
    # start with np.arange() which generates evenly spaced values within a given interval. 
    # so i can use this based off of the inputs the user gives, if they want the image to be 30 pixels wide and 30 pixels high, i can generate coordinates for x and y between 0 and 30.

    xcoords = np.arange(0, imagewidth, 10) 
    ycoords = np.arange(0, imageheight, 10) 

    #now from these sets of coordinates i gotta generate a grid of points, so i can use np.meshgrid() which takes two 1-D arrays and produces two 2-D matrices corresponding to all pairs of (x, y) in the two arrays.
    X, Y = np.meshgrid(xcoords, ycoords) 

    #plotting
    plt.scatter(X, Y, s = speckle_area) 
    plt.show()

testgrid()




#just used for generating random numbers
def randomgrid(): # this is better it doesnt use a mesh
    xcoordsrandom = np.random.randint(0, 30, size = 10)
    ycoordsrandom = np.random.randint(0, 30 ,size = 10)
    print(xcoordsrandom)
    plt.scatter(xcoordsrandom, ycoordsrandom)
    plt.show()
