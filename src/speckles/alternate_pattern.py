import numpy as np
import matplotlib.pyplot as plt

def alternate_pattern_generation(image_width: int, image_height: int, speckle_width: int, speckle_height: int, black_white_balance: float, inverted: bool = False) -> np.ndarray:
    '''
    Function that generates a white image and generated random dots based on the required density of dots on speckle pattern, image and dot dimensions.
    Parameters:
    - image_width, imageheight (int): width of image, height of image (pixels)
    - speckle_width, speckleheight (int): dimensions of dots on speckle pattern (pixels)
    - black_white_balance (float): proportion of black to white pixels, used to calculate the number of dots on speckle pattern
    - save (bool): if True, saves the pattern as a .tiff
    - inverted (bool): if True, generates an inverted image (white dots on black background)
    '''
    # calculate number of speckles needed
    image_area = (image_width*image_height)
    speckle_area = speckle_width*speckle_height
    required_speckle_density = black_white_balance
    speckle_num = int(required_speckle_density*(image_area/speckle_area))

    # generate random coordinates
    x_rand = np.random.randint(0,image_height-speckle_width+1, size = speckle_num)
    y_rand = np.random.randint(0, image_height-speckle_height+1, size = speckle_num)

    #generate image and plot speckles
    image = np.full((image_height, image_width), black_white_balance)
    for i in range(speckle_num):
        image[y_rand[i]:y_rand[i]+speckle_height, x_rand[i]:x_rand[i]+speckle_width] = 0

    if inverted:
        image = 1-image

    return image

def alternate_pattern_visualisation(pattern: np.ndarray, image_width: int, image_height: int, save: bool = False) -> None:
    '''
    Function to visualise the pattern generated passes through parameters:
    - pattern (array) = the speckle pattern generated above in alternate_pattern_generation
    - image_width, image_height (int) = image dimensions for plotting
    - save (bool) = if set to True then image saved as a .tiff, if False then pattern not saved
    '''

    # plot the speckle pattern
    plt.xlim(0, image_width)
    plt.ylim(0, image_height)
    plt.gca().set_aspect('equal')
    plt.imshow(pattern, cmap = 'gray')

    if save:
        plt.savefig("alternate_speckle_pattern.tiff")

    plt.show()


# i think its easier to use classes so that when trying to split up the functions you dont have to pass through
# every parameter every time - can just use the self. to assign them and then just pass them through and it 
# will work? maybe if finish everything and have time today can do this later