#imports
import numpy as np
import matplotlib.pyplot as plt

#pattern generation
def generate_pattern(image_width, image_height, dot_radius, black_white_balance, grid, save, inverted):
    '''
    Function that generates a random speckle pattern based on random displacements from a uniform grid. 
    Displaces midpoints of speckles and fills in any pixels within that radius. 

    Parameters:
    - image_width, image_height (int) = image dimensions (pixels)
    - dot_radius (int) = radius of dots on speckle pattern (pixels)
    - black_white_balance (float) = proportion of black:white pixels (0.0 is completely white, 1.0 is completely black)
    - grid (bool) = set to True to see original grid printed over the speckle pattern (not very useful to see so set to False)
    - save (bool) = set to True to save the pattern as a .tiff
    - inverted (bool) = set to True to invert the greyscale (have white dots on a black background)
    
    '''
    print(f"generating {image_width} x {image_height}")
    image_size = image_width * image_height
    dot_size = np.pi * (dot_radius**2)
    
    #calculating speckle spacing/grid sizing
    number_of_dots = image_size * black_white_balance / dot_size
    dot_spacing = np.sqrt(image_size / number_of_dots)

    #making my grid
    x_coords = np.arange(0, image_width, dot_spacing)
    y_coords = np.arange(0, image_height, dot_spacing)
    x, y = np.meshgrid(x_coords, y_coords)
    if grid:
        plt.scatter(x,y)

    #rounding my spacing to integer
    dot_spacing = int(round(dot_spacing))
    
    #generating random displacements
    x_displacements = np.random.randint((-1 * dot_spacing // 2),(dot_spacing // 2), size = X.shape)
    y_displacements = np.random.randint((-1 * dot_spacing // 2),(dot_spacing // 2), size = Y.shape)
    
    #adding my random displacements to each grid point
    x_new = x + x_displacements
    y_new = y + y_displacements

    #creating image of image dimensions with only white pixels
    image = np.full((image_height, image_width), 1.0)
    # splitting each pixel into 16 - 4x4 subpixels
    samples = 4
    offsets = (np.arange(samples) + 0.5) / samples - 0.5

    #making sub-grid
    yy, xx = np.meshgrid(np.arange(image_height),np.arange(image_width),indexing = 'ij')

    #for every single dot, checking what pixels fall within the dot radius and to what extent
    for x, y in zip(x_new.ravel(), y_new.ravel()):

        #setting up an area in the immediate vacinity of each dot for searching
        x_min = max(0, int(np.floor(x - dot_radius -1))) 
        x_max = min(image_width, int(np.ceil(x + dot_radius + 1)))
        y_min = max(0, int(np.floor(y - dot_radius -1)))
        y_max = min(image_height, int(np.ceil(y + dot_radius + 1)))

        #classfiying search area for each direction
        search_x = xx[y_min:y_max, x_min:x_max]
        search_y = yy[y_min:y_max, x_min:x_max]

        #making an array full of zeroes to then store coverage/greyscale values in
        grey_scale = np.zeros_like(search_x, dtype = float)

        #iterating over each subpixel increment
        for dx in offsets:
            for dy in offsets:
                #setting dist2 to within the search radius
                searching_distance = ((search_x + dx)-x)**2 + ((search_y + dy)-y)**2
                #making a new variable for if the distance within the search radius is within the dot radius
                inside_radius = searching_distance <= dot_radius**2
                grey_scale = grey_scale + inside_radius
        grey_scale = grey_scale / samples**2

        #need it to be greyscale proportional to how much pixel is being covered
        image[y_min:y_max, x_min:x_max] = np.minimum(image[y_min:y_max, x_min:x_max], 1 - grey_scale)

    #flipping every pixel greyscale for the inverted image
    if inverted is True:
        image = 1 - image
    #plotting the image
    plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
    if save:
        plt.savefig('new_speckle_pattern.tiff')
    plt.show()
    return image