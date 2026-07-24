#import functions 
from speckles import generate_pattern, fftanalysis

def main() -> None:
    '''
    Speckle pattern example: generates a speckle pattern based on variables:
    imagewidth (int) = dimension for image width in pixels
    imageheight (int) = dimension for image height in pixels
    speckle_radius (int) = radius of the speckle in pixels
    blackwhite (float) = ratio of black to white pixels generated - determines speckle number/spacing (1.0 for 100% speckels, 0.0 for no speckles). For e.g 0.5 - won't be exactly 50% black and 50% white pixels as the speckles will overlap (so put the number a bit closer to one/bigger than desired) 
    grid (bool) = determines if original grid is printed over speckle pattern (to see displacements from original points - not reccommended)
    save (bool) = determines if speckle pattern is saved or not
    visualfft (bool) = determines if fft is displayed and saved 
    '''
    imagewidth = 1000
    imageheight = 1000
    speckle_radius = 10
    blackwhite = 0.8
    grid = False
    save = True
    visualfft = True

    image = generate_pattern(imagewidth, imageheight, speckle_radius, blackwhite, grid, save)
    fftanalysis(image,visualfft)

if __name__ == '__main__':
    main()
