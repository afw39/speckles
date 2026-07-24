#THIS EXAMPLE SCRIPT IS FOR ALTERNATE SPECKLE GENERATION 

from speckles import alternate_pattern_generation


def main():
    '''
    Alternate speckle generator: generates speckles as squares rather than circles. Does not generate points from a random displacement from a grid but just fills in random pixels on the image. 
    - imageheight (int) = dimension of the image in pixels
    - imagewidth (int) = dimension of the image in pixels
    - speckleheight (int) = height of speckle in pixels
    - specklewidth (int) = width of speckle in pixels
    - bwbalance (float) = ratio of black pixels to white pixels (~density of speckles) between 0.0 and 1.0 (0 is black, 1.0 is white)
    - save (bool) = determines if speckle patten is saved or not (saved in lossless format of a tiff) 
    '''

    #inputs
    imageheight = 1000
    imagewidth = 1000
    speckleheight = 4
    specklewidth = 4
    bwbalance = 0.5
    save = True

    image = alternate_pattern_generation(imagewidth, imageheight, specklewidth, speckleheight, bwbalance, save)

if __name__ == '__main__':
    main()