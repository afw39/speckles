#okay so instead of randomnly changing pixels, i am going to generate a grid based off of the image size and speckle spacing and then randomnly displace each pixel. this might be a job for tomorrow tho. 

#start with imports again
import numpy as np
import matplotlib.pyplot as plt

#now user inputs - this time im going to ask for speckle separation instead of speckle size, to generate my grid (will be a theoretical point every spacing and that will be displaced.) so the spacing is how i know how many speckles to have

def userinputs():
    imageheight = int(input("Enter height of image in pixels: "))
    imagewidth = int(input("Enter width of the image in pixels: "))

    specklespacing = int(input("Enter how far apart you would like the speckles (between midpoints): "))

    bwbal = True
    while bwbal == True:
        blackwhite = float(input("Enter the black/white balance as a number between 0.0 and 1.0 (between black and white):  "))
        if blackwhite >= 0.0 and blackwhite <= 1.0:
            bwbal = False
        else:
            print("Please enter a number in the correct range.")
            bwbal = True
    
    specksize = True
    while specksize == True:
        speckle_size = int(input("Enter the desired speckle size in pixels: "))
        if speckle_size < 9:
            print("Speckles must be at least 9 pixels. ")
            specksize = True
        else:
            specksize = False

    lossless_format = True
    while lossless_format == True:
        format = input("Enter the format the image will be stored in: 't' for `.tiff` and 'b' for `bitmap`: ")
        if format != 't' and format != 'b':
            print("Please enter a valid format. ")
            lossless_format = True
        else:
            lossless_format = False

    return imagewidth, imageheight, specklespacing, blackwhite, speckle_size, format

#running this first to get the inputs
imagewidth, imageheight, specklespacing, blackwhite, speckle_size, format = userinputs()

#gonna quick make an if statment to deal with the format variable, then will move on to calculating the grid size:
if format == 't':
    saving = '.tiff'
else:
    saving = '.bmp'

#apparently matplotlib doesnt like bitmaps so we'll see if we end up needing this at all
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

X, Y = np.meshgrid(x_coords, y_coords) #this is my standard grid from which things are going to be displaced. 


#okay so this makes a grid of uniform dots, specklespcing apart, this is good. Now we need to make this grid of dots displace by a random number
#for i in range(number_of_speckles):
    #random_displacement = np.random.randint((-1 * specklespacing / 2), (specklespacing /2), 1)
    
x_disp = np.random.randint(
    (-1 * specklespacing // 2),
    (specklespacing //2) + 1,
    size = X.shape)


y_disp = np.random.randint(
    (-1 * specklespacing // 2) + 1,
    (specklespacing // 2) + 1,
    size = Y.shape)

#i think these have basically generated an array, hopefully the same size as the original grid size worth of points, full of random numbers of displacements, now i want to add these displacements onto the grid?

#new points
X_new = X + x_disp
Y_new = Y + y_disp

#plot new displaced points
plt.xlim(0, imagewidth)
plt.ylim(0, imageheight)
plt.scatter(X_new, Y_new, color = 'black')
ax = plt.gca()
ax.set_facecolor(str(blackwhite))
plt.margins(0)
plt.savefig("new_speckle_image.tiff",bbox_inches='tight',pad_inches=0)
plt.axis('equal')
plt.gca().set_aspect('equal')


distance_moved = np.sqrt(x_disp**2 + y_disp**2)
print("Average displacement:", np.mean(distance_moved))
print("Maximum displacement:", np.max(distance_moved))

plt.show()