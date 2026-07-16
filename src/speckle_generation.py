#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


#functions
def userinputs():
    imageheight = int(input("Enter height of image in pixels: "))
    imagewidth = int(input("Enter width of the image in pixels: "))

    specksize = True
    while specksize == True:
        speckle_width = int(input("Enter the desired speckle width in pixels: "))
        speckle_height = int(input("Enter the desired speckle height in pixels: "))
        if speckle_width < 3 or speckle_height < 3:
            print("Speckles must be at least 3 x 3 pixels. ")
            specksize = True
        else:
            specksize = False

    specklespacing = int(input("Enter how far apart you would like the speckles (between midpoints): "))

    bwbal = True
    while bwbal == True:
        blackwhite = float(input("Enter the black/white balance as a number between 0.0 and 1.0 (between black and white):  "))
        if blackwhite >= 0.0 and blackwhite <= 1.0:
            bwbal = False
        else:
            print("Please enter a number in the correct range.")
            bwbal = True

    return imagewidth, imageheight, speckle_height, speckle_width, specklespacing, blackwhite


#need to work out how many speckles i have so i know how many coordinates/points i need to generate
def speckle_num(imagewidth, specklespacing, imageheight):
    x_speckles = imagewidth /specklespacing
    y_speckles = imageheight / specklespacing
    speckle_number = x_speckles * y_speckles
    return speckle_number

#generate my grid now:
def coordinate_generation():
    x_coords = np.arange(0, imagewidth, specklespacing)
    y_coords = np.arange(0, imageheight, specklespacing)
    X, Y = np.meshgrid(x_coords, y_coords) #making my grid

    #generating random displacements
    x_disp = np.random.randint(
        (-1 * specklespacing // 2),
        (specklespacing //2) + 1,
        size = X.shape)

    y_disp = np.random.randint(
        (-1 * specklespacing // 2) + 1,
        (specklespacing // 2) + 1,
        size = Y.shape)

    #new points
    X_new = X + x_disp #adding my random displacements to each grid point
    Y_new = Y + y_disp
    return X_new, Y_new

def imagegeneration():
    #generating image with user inputted blackwhite balance
    image = np.full((imageheight, imagewidth), blackwhite)
    #drawing each speckle onto the image
    for x, y in zip(X_new.ravel(), Y_new.ravel()):
        x = max(0, min(x, imagewidth - speckle_width))
        y = max(0, min(y, imageheight - speckle_height))
        image[
            y:y+speckle_height,
            x:x+speckle_width] = 0 
    return image

def fftanalysis():
    fft = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft) # moves 0 frequency bit to the centre - easier to read
    magnitude = np.abs(fft_shifted)

    power = np.abs(fft_shifted)**2
    #next need to calculate the radial distance from the centre
    rows, cols = power.shape
    cy = rows // 2
    cx = cols // 2

    y, x = np.indices((rows, cols))

    r = np.sqrt((x-cx)**2 + (y-cy)**2) #equation for centre cx,cy
    r = r.astype(int)
    #now every FFT pixel has a radius from the centre
    counts = np.bincount(r.ravel())
    sums = np.bincount(r.ravel(), weights = power.ravel())
    radial_profile = sums / np.maximum (counts, 1)

    labels, num_features = ndimage.label(image == 0)
    areas = ndimage.sum(
        image == 0,
        labels,
        range(1, num_features + 1))
    print("Using FFT analysis, average speckle size is ",np.mean(areas))
    plt.show()


#main code
imagewidth, imageheight, speckle_height, speckle_width, specklespacing, blackwhite = userinputs()
speckle_size = speckle_height * speckle_width
imagesize = imagewidth * imageheight
number_of_speckles = speckle_num(imagewidth, specklespacing, imageheight)
X_new, Y_new = coordinate_generation()
image = imagegeneration()
plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
plt.savefig('new_speckle_pattern.tiff')
fftanalysis()
