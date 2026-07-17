#gonna try make my speckles circular instead - then the fft might work better - can use most of the same code i think, will just ask for the speckle size not the speckle dimensions and then get the radius from that - but for circular speckles idk if i can use the image thing cause gotta change square pixels into circles

#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import fft
from scipy.fft import fft2, fftshift, ifft2
from scipy.signal import peak_widths

#functions
def userinputs():
    imageheight = int(input("Enter height of image in pixels: "))
    imagewidth = int(input("Enter width of the image in pixels: "))

    specksize = True
    while specksize == True:
        speckle_size = int(input("Enter the desired speckle size in pixels: "))
        if speckle_size < 9:
            print("Speckles must be at least 9 pixels")
            specksize = True
        else:
            specksize = False


    bwbal = True
    while bwbal == True:
        blackwhite = float(input("Enter the black/white balance as a number between 0.0 and 1.0 (between white and black):  "))
        if blackwhite >= 0.0 and blackwhite <= 1.0:
            bwbal = False
        else:
            print("Please enter a number in the correct range.")
            bwbal = True

    return imagewidth, imageheight, speckle_size, blackwhite

#instead of getting user input for speckle spacing, see what 'density' of speckles is needed, and then using the image size/speckle siz in pixels can work out how much the speckle spacing is.  Going to write a separate function for this:

#lets work out what grid/speckle spacing is needed
def specklespacing():
    number_of_speckles = imagesize * blackwhite / speckle_size
    speckle_spacing = np.sqrt(imagesize / number_of_speckles)
    return speckle_spacing

#think that will be fine


#generating the uniform grid
def coordinate_generation():
    x_coords = np.arange(0, imagewidth, speckle_spacing)
    y_coords = np.arange(0, imageheight, speckle_spacing)
    X, Y = np.meshgrid(x_coords, y_coords) #making my grid

    #generating random displacements
    x_disp = np.random.randint(
        (-1 * speckle_spacing // 2) + 1,
        (speckle_spacing //2) + 1,
        size = X.shape)

    y_disp = np.random.randint(
        (-1 * speckle_spacing // 2) + 1,
        (speckle_spacing // 2) + 1,
        size = Y.shape)
    
    #adding my random displacements to each grid point
    X_new = X + x_disp 
    Y_new = Y + y_disp
    return X_new, Y_new

#making/plotting points onto my image
def imagegeneration():
    image = np.full((imageheight, imagewidth), 1) 
    #drawing each speckle onto the image
    yy, xx = np.ogrid[:imageheight, :imagewidth] #makes coordinates for each centre in a grid up to image dimensions - ogrid lets you do it at the same time. 
    for x, y in zip(X_new.ravel(), Y_new.ravel()): #loops through every speckle centre, the .ravel() changes them from a matrix and makes them into the corresponding array. 
        #this bacially colours in every pixel that is less than or equal distance away from the centre 
        mask = (xx - x)**2 + (yy-y)**2 <= speckle_radius**2 #making circles instead of squares/rectangles - will need to ammend this so that i can do like subset pixels. 
        image[mask] = 0
    return image

#main code
imagewidth, imageheight, speckle_size, blackwhite = userinputs()
imagesize = imagewidth * imageheight
speckle_radius = np.sqrt( speckle_size / np.pi)
speckle_spacing = specklespacing()
X_new, Y_new = coordinate_generation()
image = imagegeneration()
plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
plt.savefig('new_speckle_pattern.tiff')
plt.show()