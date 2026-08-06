import matplotlib.pyplot as plt
from speckles import generate_pattern, visualise_pattern, fft_analysis, fft_visualisation

def main() -> None:
    '''
    Speckle pattern example: generates a speckle pattern based on variables:

    - image_width (int) = dimension for image width in pixels
    - image_height (int) = dimension for image height in pixels
    - dot_radius (int) = radius of the dots in the speckle pattern in pixels
    - black_white_balance (float) = ratio of black to white pixels generated - determines speckle number/spacing (1.0 for 100% dots, 0.0 for no dots). For e.g 0.5 - won't be exactly 50% black and 50% white pixels as the speckles will overlap (so put the number a bit closer to one/bigger than desired) 
    - save (bool) = determines if speckle pattern is saved or not
    - visual_fft (bool) = determines if fft is displayed and saved (will still perform the fft and output average speckle size if visualfft = False)
    - inverted (bool) = set to True to change pattern to be black image with white dots (False for white image with black dots)
    '''

    image_width = 1000
    image_height = 1000
    dot_radius = 7
    black_white_balance = 0.7
    save = True
    visual_fft = True
    inverted = False
   
    image = generate_pattern(image_width, image_height, dot_radius, black_white_balance)
    visualise_pattern(image, save, inverted)

    if visual_fft is True:
        bin_centres, radial_mean = fft_analysis(image_height, image_width, image)
        fft_visualisation(bin_centres, radial_mean)
    else:
        fft_analysis(image_height, image_width, image)
        plt.show()

if __name__ == '__main__':
    main()