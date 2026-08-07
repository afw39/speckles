import numpy as np
import matplotlib.pyplot as plt
import tifffile

class OtherPattern:
    '''doc'''

    def __init__(self, image_width, image_height, speckle_width, speckle_height, black_white_balance) -> None:
        '''doc'''

        self.image_width = image_width
        self.image_height = image_height
        self.speckle_width = speckle_width
        self.speckle_height = speckle_height
        self.black_white_balance = black_white_balance
        self.speckle_number = None
        self.image = None


    def number_of_dots(self) -> None:
        '''doc'''
        image_area = (self.image_height*self.image_width)
        speckle_area = (self.speckle_height*self.speckle_width)
        required_speckle_density = self.black_white_balance
        self.speckle_number = int(required_speckle_density*(image_area/speckle_area))

    def pattern(self) -> np.ndarray:
        '''gdgdg '''
        x_random = np.random.uniform(0, self.image_width-self.speckle_width+1, size = self.speckle_number)
        y_random = np.random.uniform(0, self.image_height-self.speckle_height+1, size = self.speckle_number)

        self.image = np.full((self.image_height, self.image_width), 1.0)

        for x, y in zip(x_random.ravel(), y_random.ravel()):
            x_min = max(0, int(np.floor(x-self.speckle_width-1)))
            x_max = min(self.image_width, int(np.ceil(x+self.speckle_width+1)))
            y_min = max(0, int(np.floor(y-self.speckle_height-1)))
            y_max = min(self.image_height, int(np.ceil(y+self.speckle_height+1)))    

            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    self.image[y, x] = 0

        return self.image

    def inverted(self, inverted: bool = False) -> np.ndarray:
        '''docstring'''
        if inverted:
            self.image = 1 - self.image

        return self.image

    def visualisation(self, filename: str, bits: int, save: bool = True) -> None:
        ''' docstring'''

        plt.xlim(0, self.image_width)
        plt.ylim(0, self.image_height)
        plt.gca().set_aspect('equal')
        plt.imshow(self.image, cmap = 'gray ')

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
        return None


