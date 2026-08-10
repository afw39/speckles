import numpy as np
import matplotlib.pyplot as plt
import tifffile

class OtherPattern:
    ''' 
    Class that generates speckle pattern by generating random coordinates on a white image.

    Attributes:
        image_width, image_height (int) = image dimensions (pixels)
        speckle_width, speckleheight (int): dimensions of dots on speckle pattern (pixels)
        black_white_balance (float): proportion of black to white pixels
        inverted (bool): if True, generates an inverted image
        save (bool): if True, saves the pattern as a .tiff
        filename (str): the name that the pattern is saved as
        bits (int): how many bits make up the image (8-bit, 10-bit, 12-bit or 16-bit)

    Methods:
        number-of_dots() -> None:
            calculates the number of speckles required on pattern using the speckle/image dimensions

        pattern() -> np.ndarray:
            generates the random locations of the centre of the dots and fills any pixels within the dots in

        inverted(inverted: bool) -> None
            inverts the speckle pattern if inverted = True

        visualisation(filename: str, bits: 256, save: bool) -> None:
            plots the speckle pattern, saves as a user defined filename and bit number. 
    '''

    def __init__(self, image_width: int, image_height: int, speckle_width: float, speckle_height: float, black_white_balance: float=0.5) -> None:
        self.image_width = image_width
        self.image_height = image_height
        self.speckle_width = speckle_width
        self.speckle_height = speckle_height
        self.black_white_balance = 1 - black_white_balance
        self.speckle_number = None
        self.image = None

    def number_of_dots(self) -> None:
        '''
        Calculates the number of speckles required on pattern using the speckle/image dimensions
        Args: 
            None
        Returns: 
            None
        '''
        image_area = (self.image_height*self.image_width)
        speckle_area = (self.speckle_height*self.speckle_width)
        self.speckle_number = int((self.black_white_balance*image_area/speckle_area))

    def pattern(self) -> None:
        '''
        Generates the random locations of the centre of the dots and fills any pixels within the dots in 
        Args: 
            None
        Returns: 
            none
        '''

        x_random = np.random.uniform(0, self.image_width-self.speckle_width+1, size = self.speckle_number)
        y_random = np.random.uniform(0, self.image_height-self.speckle_height+1, size = self.speckle_number)

        self.image = np.full((self.image_height, self.image_width), 1.0)

        for x, y in zip(x_random.ravel(), y_random.ravel()):
            x_min = max(0, int(np.floor(x-self.speckle_width+1)))
            x_max = min(self.image_width, int(np.ceil(x+self.speckle_width-1)))
            y_min = max(0, int(np.floor(y-self.speckle_height+1)))
            y_max = min(self.image_height, int(np.ceil(y+self.speckle_height-1)))    

            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    self.image[y, x] = 0

    def invert_contrast(self, inverted: bool = False, contrast: float = 1) -> np.ndarray:
        '''
        Inverts speckle pattern
        Args: 
            inverted (bool): whether to invert the speckle pattern or not
            contrast (float): contrast of speckle pattern
        Returns:
            np.ndarray: speckle pattern 
        '''
        if inverted:
            self.image = 1 - self.image

        self.image = self.image * contrast

        return self.image

    def visualisation(self) -> None:
        ''' 
        visualising the speckle pattern
        Args: 
            filename (str): name that the pattern gets saved under
            bits (int): bit depth that the image is saved with
            save (bool): whether the image is saved or not
        Returns: 
            None
        '''

        plt.xlim(0, self.image_width)
        plt.ylim(0, self.image_height)
        plt.gca().set_aspect('equal')
        plt.imshow(self.image, cmap = 'gray')


    def save(self, bits:int = 256, filename:str = 'alternate_speckle_pattern.tiff',save: bool=False) -> None:
        '''
        determines whether of not to save the image,if so, savesto the correct bit depth and under the correct filename

        Args:
            bits (int): determines the bit depth that file is saved to
            filename (str): determines what name the file is saved under
            save (bool): determines whether file is saved
        '''

        if save:
            max_val = (1 << bits)-1
            if bits <= 8:
                dtype = np.uint8
            else:
                dtype = np.uint16

            out = np.clip(self.image, 0, 1)
            out = (out*max_val).round().astype(dtype)

            tifffile.imwrite(filename, out)

        plt.show()


