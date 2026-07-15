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


    # making sure the format is correct
    format = True
    while format == True:
        format_lossless = input("What format would you like the file to be saved as? Enter 't' for tiff and 'b' for bitmap. ")
        if format_lossless == 't':
            format = False
            #save as a tiff
        elif format_lossless == 'b':
            format = False
            #save as a bitmap
        else:
            print("incorrect format. try again ")
            format = True



# okay now im just going to try and generate a grid using matplotlib. 
def testgrid():
    # start with np.arange() which generates evenly spaced values within a given interval. 
    # so i can use this based off of the inputs the user gives, if they want the image to be 30 pixels wide and 30 pixels high, i can generate coordinates for x and y between 0 and 30.


    #need to run the function now, cant be bothered to do all the questions so just retyping the inputs here, will remove after

    imagewidth = 7
    imageheight = 7
    xcoords = np.arange(0, imagewidth, 1) #just using a spacing of 1 as that should be the like smallest resolution I guess?
    ycoords = np.arange(0, imageheight, 1) #same for the height(y coordinates) - also this is 0-29 inclusive so 30 pixels/points
    #these should have now generated an array of 0-30 with a step of 1?

    #now from these sets of coordinates i gotta generate a grid of points, so i can use np.meshgrid() which takes two 1-D arrays and produces two 2-D matrices corresponding to all pairs of (x, y) in the two arrays.
    X, Y = np.meshgrid(xcoords, ycoords) #this should generate a grid
    #print(X,Y) # to check if my coordinate grid is good and correct, if it is then i'll plot it in matplotlib. 
    #acc dont know if that worked, but i installed numpy and matplotlib so i should be able to plot it now.
    #print(X.shape)
    #print(Y.shape)

    #lets try plot this
    plt.scatter(X, Y, s =10) #scatter plot of the grid, the s = 10 controls the dot size, i can change this when i have my speckle dimensions? 
    plt.show()

#OKAYYYY so i have a uniform grid - things i need to do now is basically generate the x and y coordinates to be random and then make them the size that the user inputs.  
def randomgrid(): # this is better it doesnt use a mesh
    #okay gonna stick with the same size of all the speckles, just going to try and make them random coordinates - think that acc shouldnt be too hard? 
    #imagewidth = 7
    #imageheight = 7 #leaving these at 7 for now
    xcoordsrandom = np.random.randint(0, 30, size = 10) #right now, this size thing is the number of speckles/points i am making, has to be the same for the x and y coordinates i think. will calculate how many speckles i want to generate based off of the speckle size and the image size, but am gonna do that later. this code will generate 3 random x coordinates between 0 and 30 (not including 30) or just the middle value
    ycoordsrandom = np.random.randint(0, 30 ,size = 10) # we get 3 y coordinates, so should make 9 points?? idk
    print(xcoordsrandom)
    #X,Y = np.meshgrid(xcoordsrandom, ycoordsrandom) #this should generate a grid of the random coordinates, but not sure if it will be a uniform grid or not?
    plt.scatter(xcoordsrandom, ycoordsrandom)
    plt.show()

#now im going to make the speckles the right size?
