import numpy as np
from .grid import dots_number, displaced_grid



class Pattern:
    '''
    Generates speckle pattern

    Attributes
        image_height, image_width (int): image dimensions (pix)
        dot_radius (float): radius of dots on speckle pattern
        speckle_coverage (float): measure of ratio of white pixels to black pixels on pattern
        inverted (bool): determines if image inverts greyscale or not
        contrast (float): the contrast of the image (1.0 for highest, 0 for all black image - no contrast)
        filename (str): name that the pattern is saved under
        bits (int): how many bits to encode the saved pattern (8-bit, 10-bit, 12-bit, 16-bit)
        save (bool): whether the pattern is saved or not
    
    Methods:
        dots_number(): calculates how many dots required on speckle pattern to achieve correct black_white_balance
        displaced_grid(): generates random displacements and applies to uniform grid to achieve dot locations
        image_creation(): creates the image and fills in the dots
        visualise_pattern(inverted: bool): inverts the image
        contrast(contrast: float): adjusts the contrast of the image
        bit_depth_tiff(filename: str, bits: int, save: bool): saves the image as user requests
    '''

    def __init__(self, image_width: int, image_height: int, dot_radius: float, speckle_coverage: float):
        self.image_width = image_width
        self.image_height = image_height
        self.dot_radius = dot_radius
        self.black_white_balance = 1-speckle_coverage
        self.x_new = None
        self.y_new = None
        self.dot_spacing = None
        self.image = None

        self.dot_spacing = dots_number(self.image_width, self.image_height, self.dot_radius, self.black_white_balance)
        self.x_new, self.y_new = displaced_grid(self.image_width, self.image_height, self.dot_spacing)

    def pattern_generation(self) -> np.ndarray:
        '''
        creates the image and fills in the dots
        Args:
            None
        Returns:
            None
        '''
        print(f'generating {self.image_width} x {self.image_height}')
        self.image = np.full((self.image_height, self.image_width), 1.0)
        samples = 8
        offsets = (np.arange(samples)+0.5)/samples-0.5
        yy, xx = np.meshgrid(np.arange(self.image_height), np.arange(self.image_width), indexing = 'ij')

        for x, y in zip(self.x_new.ravel(), self.y_new.ravel()):
            x_min = max(0, int(np.floor(x-self.dot_radius-1))) 
            x_max = min(self.image_width, int(np.ceil(x+self.dot_radius+1)))
            y_min = max(0, int(np.floor(y-self.dot_radius-1)))
            y_max = min(self.image_height, int(np.ceil(y+self.dot_radius+1)))

            search_x = xx[y_min:y_max, x_min:x_max]
            search_y = yy[y_min:y_max, x_min:x_max]

            grey_scale = np.zeros_like(search_x, dtype = float)

            for dx in offsets:
                for dy in offsets:
                    searching_distance = ((search_x+dx)-x)**2 + ((search_y+dy)-y)**2
                    inside_radius = searching_distance <= self.dot_radius**2
                    grey_scale = grey_scale+inside_radius

            grey_scale = grey_scale / samples**2

            self.image[y_min:y_max, x_min:x_max] = np.minimum(self.image[y_min:y_max, x_min:x_max], 1-grey_scale)
        return self.image
