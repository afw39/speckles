#okay so instead of randomnly changing pixels, i am going to generate a grid based off of the image size and speckle spacing and then randomnly displace each pixel. this might be a job for tomorrow tho. 

#start with imports again
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


#now user inputs - this time im going to ask for speckle separation instead of speckle size, to generate my grid (will be a theoretical point every spacing and that will be displaced.) so the spacing is how i know how many speckles to have

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

#running this first to get the inputs
imagewidth, imageheight, speckle_height, speckle_width, specklespacing, blackwhite = userinputs()

#apparently matplotlib doesnt like bitmaps so we'll see if we end up needing this at all
speckle_size = speckle_height * speckle_width
imagesize = imagewidth * imageheight

#lets calculate our grid size
def gridsize(imagewidth, specklespacing, imageheight):
    #so need to generate a point at regular intervals of x_diff and at y_diff
    x_coords = np.arange(0, imagewidth, specklespacing) # i think this is making an array between 0 and the width with intervals of specklespacing?
    y_coords = np.arange(0, imageheight, specklespacing) #same for y
    return x_coords, y_coords

x_coords, y_coords = gridsize(imagewidth, specklespacing, imageheight)

#need to work out how many speckles i have so i know how many coordinates/points i need to generate
def speckle_num(imagewidth, specklespacing, imageheight):
    x_speckles = imagewidth /specklespacing
    y_speckles = imageheight / specklespacing
    speckle_number = x_speckles * y_speckles
    return speckle_number

number_of_speckles = speckle_num(imagewidth, specklespacing, imageheight)

#i think i need to like use a for loop and iterate for each on of these x/y coords, i need to generate a random number between (-1 *speckle_spacing /2) and speckle_spacing / 2 and then add this number onto the x/y_coords and then plot those. 

#we gonna try do this random method but by generating an image instead:
image = np.full((imageheight, imagewidth), blackwhite) #making our image with a greyscale background
#generate my grid now:

x_coords = np.arange(0, imagewidth, specklespacing)
y_coords = np.arange(0, imageheight, specklespacing)
X, Y = np.meshgrid(x_coords, y_coords)

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
X_new = X + x_disp
Y_new = Y + y_disp

#instead of plotting them in a scatter graph, going to draw speckles onto the image - gonna use a for loop for this
for x, y in zip(X_new.ravel(), Y_new.ravel()):
    x = max(0, min(x, imagewidth - speckle_width))
    y = max(0, min(y, imageheight - speckle_height))
    image[
        y:y+speckle_height,
        x:x+speckle_width] = 0 #this is drawing each speckle in black, so to do the greyscale thing will change the np.zeroes thing.

#then display
plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
plt.savefig('new_speckle_pattern.tiff')

#okay now i need to do a fast fourier transform analysis for my average speckle size
fft = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft) # moves 0 frequency bit to the centre - easier to read
magnitude = np.abs(fft_shifted)

#display the fft
plt.figure()
plt.imshow(np.log(magnitude+1), cmap = 'gray')
plt.title("FFT Magnitude")
plt.savefig("fft.tiff")


power = np.abs(fft_shifted)**2
#next need to calculate the radial distance from the centre
rows, cols = power.shape
cy = rows // 2
cx = cols // 2

y, x = np.indices((rows, cols))

r = np.sqrt((x-cx)**2 + (y-cy)**2)
r = r.astype(int) #need to know what this FFT value is??
#now every FFT pixel has a radius from the centre
counts = np.bincount(r.ravel())
sums = np.bincount(r.ravel(), weights = power.ravel())
radial_profile = sums / np.maximum (counts, 1)
plt.figure()
plt.plot(radial_profile)
plt.xlim(0,50)
plt.xlabel("radius")
plt.ylabel("Average FFT power")


labels, num_features = ndimage.label(image == 0)


areas = ndimage.sum(
    image == 0,
    labels,
    range(1, num_features + 1)
)

print(np.mean(areas))
plt.show()