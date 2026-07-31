#import functions 
from speckles import generate_pattern, fftanalysis

def main() -> None:
    '''
    Speckle pattern example: generates a speckle pattern based on variables:
    imagewidth (int) = dimension for image width in pixels
    imageheight (int) = dimension for image height in pixels
    speckle_radius (int) = radius of the dots in the speckle pattern in pixels
    blackwhite (float) = ratio of black to white pixels generated - determines speckle number/spacing (1.0 for 100% dots, 0.0 for no dots). For e.g 0.5 - won't be exactly 50% black and 50% white pixels as the speckles will overlap (so put the number a bit closer to one/bigger than desired) 
    grid (bool) = determines if original grid is printed over speckle pattern (to see displacements from original points - not reccommended)
    save (bool) = determines if speckle pattern is saved or not
    visualfft (bool) = determines if fft is displayed and saved (will still perform the fft and output average speckle size if visualfft = False)
    inverted (bool) = set to True to change pattern to be black image with white dots (False for white image with black dots)
    '''
    imagewidth = 1000
    imageheight = 1000
    dot_radius = 7
    blackwhite = 0.7
    grid = False
    save = True
    visualfft = False
    inverted = False

    image = generate_pattern(imagewidth, imageheight, dot_radius, blackwhite, grid, save, inverted)
    fftanalysis(image,visualfft)

if __name__ == '__main__':
    main()
