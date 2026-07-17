#imports
import numpy as np 
import matplotlib.pyplot as plt 

#start with some user inputs:
def inputvalues():
    imagewidth = int(input("Enter image width "))
    imageheight = int(input("Enter image height "))

    speckles = True
    while speckles == True:
        specklewidth= int(input("Enter width of speckles. "))
        speckleheight= int(input("Enter height of speckles. "))
        speckle_area = specklewidth * speckleheight
        if specklewidth < 3 or speckleheight < 3:
            print("Speckles must be at least 3 pixels wide"
            " and 3 pixels tall. Please try again.")
            speckles = True
        elif speckle_area > 9 and speckleheight > 3 and specklewidth > 3:
            speckles = False
        else:
            speckles = False

    # using this as the density of speckles
    bw = True
    while bw == True:
        bwbalance = float(input("Enter black and white balance (0.0 is black- 1.0 is white). "))
        if bwbalance < 0.0 or bwbalance > 1.0:
            print("Incorrect value. Please enter a value between 0.0 and 1.0.")
            bw = True
        else:
            bw = False

    return imagewidth, imageheight, specklewidth, speckleheight, bwbalance, speckle_area


imagewidth, imageheight, specklewidth, speckleheight, bwbalance, speckle_area = inputvalues() 

def speckle_num(imagewidth, imageheight, specklewidth, speckleheight, bwbalance):
    imagearea = (imagewidth * imageheight)
    specklearea = specklewidth * speckleheight
    required_speckle_density = bwbalance
    speckle_num = required_speckle_density * (imagearea / specklearea)
    return int(speckle_num)

number_of_speckles = speckle_num(imagewidth, imageheight, specklewidth, speckleheight, bwbalance)
speckle_area = specklewidth * speckleheight

#generating random coordinates
x_rand = np.random.randint(
    0,
    imagewidth - specklewidth + 1,
    size=number_of_speckles)

y_rand = np.random.randint(
    0,
    imageheight - speckleheight + 1,
    size=number_of_speckles)


#plotting the image size
plt.xlim(0, imagewidth)
plt.ylim(0, imageheight)
plt.gca().set_aspect('equal')

image = np.full((imageheight,imagewidth), bwbalance)

for i in range(number_of_speckles): #changing each pixel one by one to black from background colour
    image[
        y_rand[i]:y_rand[i] + speckleheight,
        x_rand[i]:x_rand[i] + specklewidth
    ] = 0

plt.imshow(image, cmap = 'gray')
plt.savefig("speckle_image.tiff") 
plt.show()