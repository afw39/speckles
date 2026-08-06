#imports
import numpy as np
import matplotlib.pyplot as plt

def alternate_pattern_generation(image_width, image_height, speckle_width, speckle_height, black_white_balance, save, inverted):
    '''
    Function that generates a white image and generated random dots based on the required density of dots on speckle pattern, image and dot dimensions.

    Parameters:
    - image_width, imageheight (int): width of image, height of image (pixels)
    - speckle_width, speckleheight (int): dimensions of dots on speckle pattern (pixels)
    - black_white_balance (float): proportion of black to white pixels, used to calculate the number of dots on speckle pattern
    - save (bool): if True, saves the pattern as a .tiff

    '''
    image_area = (image_width * image_height)
    speckle_area = speckle_width * speckle_height
    required_speckle_density = black_white_balance
    speckle_num = int(required_speckle_density * (image_area / speckle_area))

    #generate random coordinates
    x_rand = np.random.randint(0,image_height - speckle_width + 1, size = speckle_num)
    y_rand = np.random.randint(0, image_height - speckle_height + 1, size = speckle_num)

    #plot image
    plt.xlim(0, image_width)
    plt.ylim(0, image_height)
    plt.gca().set_aspect('equal')
    image = np.full((image_height, image_width), black_white_balance)

    for i in range(speckle_num):
        image[y_rand[i]:y_rand[i] + speckle_height, x_rand[i]:x_rand[i] + speckle_width] = 0
    if inverted is True:
        image = 1 - image
    plt.imshow(image, cmap = 'gray')
    if save:
        plt.savefig("alternate_speckle_pattern.tiff")
    plt.show()
    return None









#howdyen
#add the inverse ability to this when have time