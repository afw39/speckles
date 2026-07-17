#gonna try make my speckles circular instead - then the fft might work better - can use most of the same code i think, will just ask for the speckle size not the speckle dimensions and then get the radius from that - but for circular speckles idk if i can use the image thing cause gotta change square pixels into circles

#imports
import numpy as np
import matplotlib.pyplot as plt
#from scipy import ndimage
#from scipy import fft
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

    specklespacing = int(input("Enter how far apart you would like the speckles (between centres): "))

    bwbal = True
    while bwbal == True:
        blackwhite = float(input("Enter the black/white balance as a number between 0.0 and 1.0 (between black and white):  "))
        if blackwhite >= 0.0 and blackwhite <= 1.0:
            bwbal = False
        else:
            print("Please enter a number in the correct range.")
            bwbal = True

    return imagewidth, imageheight, speckle_size, specklespacing, blackwhite

#generating the uniform grid
def coordinate_generation():
    x_coords = np.arange(0, imagewidth, specklespacing)
    y_coords = np.arange(0, imageheight, specklespacing)
    X, Y = np.meshgrid(x_coords, y_coords) #making my grid

    #generating random displacements
    x_disp = np.random.randint(
        (-1 * specklespacing // 2) + 1,
        (specklespacing //2) + 1,
        size = X.shape)

    y_disp = np.random.randint(
        (-1 * specklespacing // 2) + 1,
        (specklespacing // 2) + 1,
        size = Y.shape)
    
    #adding my random displacements to each grid point
    X_new = X + x_disp 
    Y_new = Y + y_disp
    return X_new, Y_new

#thats the same code as before but i think its fine, the X_new and Y_new are the new centres of the speckles. so when changing pixels, need to change the pixels of the centre and al pixels within the radius (but in a circular way? so cant make a square by accident)

#generating image with user inputted blackwhite balance
def imagegeneration():
    image = np.full((imageheight, imagewidth), blackwhite) #this is fine
    #drawing each speckle onto the image
    yy, xx = np.ogrid[:imageheight, :imagewidth]
    for x, y in zip(X_new.ravel(), Y_new.ravel()):
        mask = (xx - x)**2 + (yy-y)**2 <= speckle_radius**2 #making circles instead of squares/rectangles
        image[mask] = 0
    return image

#main code
imagewidth, imageheight, speckle_size, specklespacing, blackwhite = userinputs()
speckle_radius = np.sqrt( speckle_size / np.pi)
imagesize = imagewidth * imageheight
X_new, Y_new = coordinate_generation()
image = imagegeneration()
plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
plt.savefig('new_speckle_pattern.tiff')
plt.show()