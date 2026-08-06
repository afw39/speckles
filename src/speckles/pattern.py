import numpy as np
import matplotlib.pyplot as plt

def generate_pattern(image_width: int, image_height:int, dot_radius:int, black_white_balance: int) -> np.ndarray:

    '''
    Function that generates a random speckle pattern based on random displacements from a uniform grid. 
    Displaces midpoints of speckles and fills in any pixels within that radius. 

    Parameters:
    - image_width, image_height (int) = image dimensions (pixels)
    - dot_radius (int) = radius of dots on speckle pattern (pixels)
    - black_white_balance (float) = proportion of black:white pixels (0.0 is completely white, 1.0 is completely black)
    '''

    print(f"generating {image_width} x {image_height}")

    image_size = image_width * image_height
    dot_size = np.pi * (dot_radius**2)
    number_of_dots = image_size * black_white_balance / dot_size
    dot_spacing = np.sqrt(image_size / number_of_dots)

    x_coords = np.arange(0, image_width, dot_spacing)
    y_coords = np.arange(0, image_height, dot_spacing)
    x, y = np.meshgrid(x_coords, y_coords)
    dot_spacing = int(round(dot_spacing))
    x_displacements = np.random.randint((-1 * dot_spacing // 2),(dot_spacing // 2), size = x.shape)
    y_displacements = np.random.randint((-1 * dot_spacing // 2),(dot_spacing // 2), size = y.shape)
    x_new = x + x_displacements
    y_new = y + y_displacements

    image = np.full((image_height, image_width), 1.0)
    samples = 4
    offsets = (np.arange(samples) + 0.5) / samples - 0.5
    yy, xx = np.meshgrid(np.arange(image_height),np.arange(image_width),indexing = 'ij')

    for x, y in zip(x_new.ravel(), y_new.ravel()):

        x_min = max(0, int(np.floor(x - dot_radius -1))) 
        x_max = min(image_width, int(np.ceil(x + dot_radius + 1)))
        y_min = max(0, int(np.floor(y - dot_radius -1)))
        y_max = min(image_height, int(np.ceil(y + dot_radius + 1)))

        search_x = xx[y_min:y_max, x_min:x_max]
        search_y = yy[y_min:y_max, x_min:x_max]

        grey_scale = np.zeros_like(search_x, dtype = float)

        for dx in offsets:

            for dy in offsets:

                searching_distance = ((search_x + dx)-x)**2 + ((search_y + dy)-y)**2
                inside_radius = searching_distance <= dot_radius**2
                grey_scale = grey_scale + inside_radius

        grey_scale = grey_scale / samples**2

        image[y_min:y_max, x_min:x_max] = np.minimum(image[y_min:y_max, x_min:x_max], 1 - grey_scale)

    return image


def visualise_pattern(pattern: np.ndarray,save: bool, inverted: bool = False) -> None:
    ''' 
    Function to visualise the pattern generated in the function `generate_pattern`. Parameters:
    - pattern (array) = image generated in function above 
    - save (bool) = set to True to save the pattern as a .tiff
    - inverted (bool) = set to True to invert the greyscale (have white dots on a black background)
    '''

    if inverted is True:
        pattern = 1 - pattern
    
    plt.imshow(pattern, cmap = 'gray', vmin = 0, vmax = 1)

    if save is True:
        plt.savefig('new_speckle_pattern.tiff')