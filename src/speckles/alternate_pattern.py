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

    image_area = (image_width * image_height)
    speckle_area = speckle_width * speckle_height
    required_speckle_density = black_white_balance
    speckle_num = int(required_speckle_density * (image_area / speckle_area))

    x_rand = np.random.randint(0,image_height - speckle_width + 1, size = speckle_num)
    y_rand = np.random.randint(0, image_height - speckle_height + 1, size = speckle_num)

   
    image = np.full((image_height, image_width), black_white_balance)

    for i in range(speckle_num):
        image[y_rand[i]:y_rand[i] + speckle_height, x_rand[i]:x_rand[i] + speckle_width] = 0

    if inverted is True:

        image = 1 - image

    return image

def alternate_pattern_visualisation(pattern: np.ndarray, image_width: int, image_height: int, save: bool) -> None:
    '''
    Function to visualise the pattern generated passes through parameters:
    - pattern (array) = the speckle pattern generated above in alternate_pattern_generation
    - image_width, image_height (int) = image dimensions for plotting
    - save (bool) = if set to 'True' then image saved as a .tiff
    '''
    plt.xlim(0, image_width)
    plt.ylim(0, image_height)
    plt.gca().set_aspect('equal')
    plt.imshow(pattern, cmap = 'gray')

    if save is True:
        plt.savefig("alternate_speckle_pattern.tiff")

    plt.show()
