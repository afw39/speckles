#imports
import numpy as np
import matplotlib.pyplot as plt


#okay in here want to pass an extra parameter which is gonna decide whether the pattern is white with black dots or black with white dots
#for inverted pattern (black background and white dots, set inverted = True)

#pattern generation
def generate_pattern(imagewidth, imageheight, speckle_radius, blackwhite, grid, save, inverted):
    '''
    Function that generates a random speckle pattern based on random displacements from a uniform grid. Displaces midpoints of speckles and fills in any pixels within that radius. 

    Parameters:
    - imagewidth, imageheight (int) = image dimensions (pixels)
    - speckle_radius (int) = radius of dots on speckle pattern (pixels)
    - blackwhite (float) = proportion of black:white pixels (0.0 is completely white, 1.0 is completely black)
    - grid (bool) = set to True to see original grid printed over the speckle pattern (not very useful to see so set to False)
    - save (bool) = set to True to save the pattern as a .tiff
    
    '''

    print(f"generating {imagewidth} x {imageheight}")
    imagesize = imagewidth * imageheight
    speckle_size = np.pi * (speckle_radius**2)
    
    #calculating speckle spacing/grid sizing
    number_of_speckles = imagesize * blackwhite / speckle_size
    speckle_spacing = np.sqrt(imagesize / number_of_speckles)

    #making my grid
    x_coords = np.arange(0, imagewidth, speckle_spacing)
    y_coords = np.arange(0, imageheight, speckle_spacing)
    X, Y = np.meshgrid(x_coords, y_coords)
    if grid:
        plt.scatter(X,Y)

    #rounding my spacing to integer
    speckle_spacing = int(round(speckle_spacing))
    #generating random displacements
    x_disp = np.random.randint((-1 * speckle_spacing // 2),(speckle_spacing // 2), size = X.shape)
    y_disp = np.random.randint((-1 * speckle_spacing // 2),(speckle_spacing // 2), size = Y.shape)
    
    #adding my random displacements to each grid point
    x_new = X + x_disp 
    y_new = Y + y_disp

    #creating image of image dimensions with only white pixels
    #if inverted:
        #set background to black
       # image = np.full((imageheight, imagewidth), 0)
    #else:
        #set background to white
        #image = np.full((imageheight, imagewidth), 1.0)
    image = np.full((imageheight, imagewidth), 1.0)
    # splitting each pixel into 16 - 4x4 subpixels
    samples = 4
    offsets = (np.arange(samples) + 0.5) / samples - 0.5

    #making sub-grid
    yy, xx = np.meshgrid(np.arange(imageheight),np.arange(imagewidth),indexing = 'ij')

    #for every single speckle, checking what pixels fall within the speckle radius
    for x, y in zip(x_new.ravel(), y_new.ravel()):

        #instead of searching every single pixel in the image every time, going to only search pixels within the area of speckle to speed it up, so these are my like 'search regions' for each speckle (within the radius +- 1 pixel just incase)
        xmin = max(0, int(np.floor(x - speckle_radius -1))) 
        xmax = min(imagewidth, int(np.ceil(x + speckle_radius + 1)))
        ymin = max(0, int(np.floor(y - speckle_radius -1)))
        ymax = min(imageheight, int(np.ceil(y + speckle_radius + 1)))
        
        #only considering pixels within the square of speckle radius
        search_x = xx[ymin:ymax, xmin:xmax]
        search_y = yy[ymin:ymax, xmin:xmax]

        #now only considering pixels in like the square area around speckle to change their colour in the relevant region
        #zero in colour means black
        #making an array full of zeroes
        coverage = np.zeros_like(search_x, dtype = float)

        for dx in offsets:
            for dy in offsets:
                dist2 = ((search_x + dx)-x)**2 + ((search_y + dy)-y)**2
                coverage += dist2 <= speckle_radius**2
        coverage /= samples**2
        #need it to be greyscale proportional to how much pixel is being covered (use the np.minimum to make sure that overlapping dark areas don't get overwritten and turn lighter if on the edge of another speckle or vice versa with np.maximum)
        image[ymin:ymax, xmin:xmax] = np.minimum(image[ymin:ymax, xmin:xmax], 1 - coverage)
        #if inverted:
           #image[ymin:ymax, xmin:xmax] = np.maximum(image[ymin:ymax, xmin:xmax], coverage)
        #else:
           # image[ymin:ymax, xmin:xmax] = np.minimum(image[ymin:ymax, xmin:xmax], 1 - coverage)
        if inverted:
            image = 1 - image
    plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
    if save:
        plt.savefig('new_speckle_pattern.tiff')
    plt.show()
    return image

def main() -> None:
    '''
    Speckle pattern example: generates a speckle pattern based on variables:
    - imagewidth (int) = dimension for image width in pixels
    - imageheight (int) = dimension for image height in pixels
    - speckle_radius (int) = radius of the dots on speckle pattern in pixels
    - blackwhite (float) = ratio of black to white pixels generated - determines speckle number/spacing (1.0 for 100% speckels, 0.0 for no speckles). For e.g 0.5 - won't be exactly 50% black and 50% white pixels as the speckles will overlap (so put the number a bit closer to one/bigger than desired) 
    - grid (bool) = determines if original grid is printed over speckle pattern (to see displacements from original points - not reccommended)
    - save (bool) = determines if speckle pattern is saved or not
    - visualfft (bool) = determines if fft is displayed and saved (will still perform the fft and output average speckle size if visualfft = False)
    '''
    imagewidth = 1000
    imageheight = 1000
    speckle_radius = 5
    blackwhite = 0.55
    grid = False
    save = True
    inverted = True
    #visualfft = False

    image = generate_pattern(imagewidth, imageheight, speckle_radius, blackwhite, grid, save, inverted)
    #fftanalysis(image,visualfft)

if __name__ == '__main__':
    main()
