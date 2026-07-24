#imports
import numpy as np
import matplotlib.pyplot as plt

#pattern generation
def generate_pattern(imagewidth, imageheight, speckle_radius, blackwhite, grid, save):

    print(f"generating {imagewidth} x {imageheight}")
    imagesize = imagewidth * imageheight
    speckle_size = np.pi * (speckle_radius**2)
    
    #calculating speckle spacing/grid sizng
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
    x_disp = np.random.randint((-1 * speckle_spacing // 2) + 1,(speckle_spacing //2) + 1,size = X.shape)
    y_disp = np.random.randint((-1 * speckle_spacing // 2) + 1,(speckle_spacing // 2) + 1,size = Y.shape)
    
    #adding my random displacements to each grid point
    X_new = X + x_disp 
    Y_new = Y + y_disp

    #creating image of image dimensions with only white pixels
    image = np.full((imageheight, imagewidth), 1.0)
    # splitting each pixel into 16 - 4x4 subpixels
    samples = 4
    offsets = (np.arange(samples) + 0.5) / samples - 0.5

    #making sub-grid
    yy, xx = np.meshgrid(np.arange(imageheight),np.arange(imagewidth),indexing = 'ij')

    #for every single speckle, checking what pixels fall within the speckle radius
    for x, y in zip(X_new.ravel(), Y_new.ravel()):

        #instead of searching every single pixel in the image every time, going to only search pixels within the area of speckle to speed it up, so these are my like 'search regions' for each speckle (within the radius +- 1 pixel just incase)
        xmin = max(0, int(np.floor(x -speckle_radius -1))) 
        xmax = min(imagewidth, int(np.ceil(x + speckle_radius + 1)))
        ymin = max(0, int(np.floor(y -speckle_radius -1)))
        ymax = min(imageheight, int(np.ceil(y + speckle_radius + 1)))
        
        #only considering pixels within the square of speckle radius
        search_x = xx[ymin:ymax, xmin:xmax]
        search_y = yy[ymin:ymax, xmin:xmax]

        #now only considering pixels in like the square area around speckle to change their colour in the relevant region
        coverage = np.zeros_like(search_x, dtype = float)

        for dx in offsets:
            for dy in offsets:
                dist2 = ((search_x + dx)-x)**2 + ((search_y + dy)-y)**2
                coverage += dist2 <= speckle_radius**2
        coverage /= samples**2
        #need it to be greyscale proportional to how much pixel is being covered (use the np.minimum to make sure that overlapping dark areas don't get overwritten and turn lighter if on the edge of another speckle)
        image[ymin:ymax, xmin:xmax] = np.minimum(image[ymin:ymax, xmin:xmax], 1-coverage)
    plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
    if save:
        plt.savefig('new_speckle_pattern.tiff')
    return image