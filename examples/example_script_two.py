#THIS EXAMPLE SCRIPT IS FOR ALTERNATE SPECKLE GENERATION 

from speckles import alternate_pattern_generation


def main():
    '''
    description
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