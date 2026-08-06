from speckles import alternate_pattern_generation


def main():
    '''
    Alternate speckle generator: generates speckle pattern using rectangles. Does not generate points from a random displacement from a grid but just fills in random pixels on the image. 
    - image_height (int) = dimension of the image in pixels
    - image_width (int) = dimension of the image in pixels
    - speckle_height (int) = height of rectangle on speckle pattern in pixels
    - speckle_width (int) = width of rectangle on speckle pattern in pixels
    - black_white_balance (float) = ratio of black pixels to white pixels (~density of black pixels) between 0.0 and 1.0 (1.0 is most black, 0 is all white pixels)
    - save (bool) = determines if speckle patten is saved or not (saved in lossless format of a tiff) 
    '''

    #inputs
    image_height = 1000
    image_width = 1000
    speckle_height = 10
    speckle_width = 10
    black_white_balance = 0.7
    save = True
    inverted = False

    alternate_pattern_generation(image_width, image_height, speckle_width, speckle_height, black_white_balance, save, inverted)
    

if __name__ == '__main__':
    main()