#imports
import numpy as np 
import matplotlib.pyplot as plt 


#imagewidth, imageheight, specklewidth, speckleheight, bwbalance, speckle_area = inputvalues() 
def alternate_pattern_generation(imagewidth, imageheight, specklewidth, speckleheight, bwbalance, save):
    '''
    Function that generates a white image and generated random speckles based on the required density of speckles, image and speckle dimensions.

    Parameters:
    - imagewidth, imageheight (int): width of image, height of image (pixels)
    - specklewidth, speckleheight (int): width of speckle, height of speckle (pixels)
    - bwbalance (float): proportion of black to white pixels, used to calculate the number of speckles
    - save (bool): if True, saves the pattern as a .tiff

    '''
    imagearea = (imagewidth * imageheight)
    specklearea = specklewidth * speckleheight
    required_speckle_density = bwbalance
    speckle_num = int(required_speckle_density * (imagearea / specklearea))

    #generate random coordinates
    x_rand = np.random.randint(0,imageheight - specklewidth + 1, size = speckle_num)
    y_rand = np.random.randint(0, imageheight - speckleheight + 1, size = speckle_num)

    #plot image
    plt.xlim(0, imagewidth)
    plt.ylim(0, imageheight)
    plt.gca().set_aspect('equal')
    image = np.full((imageheight, imagewidth), bwbalance)

    for i in range(speckle_num):
        image[y_rand[i]:y_rand[i] + speckleheight, x_rand[i]:x_rand[i] + specklewidth] = 0
    plt.imshow(image, cmap = 'gray')
    if save:
        plt.savefig("alternate_speckle_pattern.tiff")
    plt.show()
    return None