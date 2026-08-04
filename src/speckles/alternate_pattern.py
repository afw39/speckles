#imports
import numpy as np 
import matplotlib.pyplot as plt 

def alternate_pattern_generation(imagewidth, imageheight, specklewidth, speckleheight, bwbalance, save, inverted):
    '''
    Function that generates a white image and generated random dots based on the required density of dots on speckle pattern, image and dot dimensions.

    Parameters:
    - imagewidth, imageheight (int): width of image, height of image (pixels)
    - specklewidth, speckleheight (int): dimensions of dots on speckle pattern (pixels)
    - bwbalance (float): proportion of black to white pixels, used to calculate the number of dots on speckle pattern
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
    if inverted == True:
        image = 1 - image
    else:
        image = image
    plt.imshow(image, cmap = 'gray')
    if save:
        plt.savefig("alternate_speckle_pattern.tiff")
    plt.show()
    return None









#howdyen
#add the inverse ability to this when have time