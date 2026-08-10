import numpy as np
import matplotlib.pyplot as plt
import tifffile
from PIL import Image

class ImageGeneration:
    '''
    Generates image from speckle pattern

    Attributes:
        pattern (np.ndarray): the speckle pattern generated in pattern.py
        image_intensity (float): mean intensity of the image
        inverted (bool): set to True to invert greyscale of image
        contrast (float): 0 - 1 measure of contrast of image
        filename (str): name that file is saved under
        bits (int): how many bits encode image that is saved
        save (bool): whether the image is saved or not

    Methods:
        visualise_pattern(inverted: bool, contrast: float): if required, inverts image and sets contrast
        mean_intensity(): changes the image based on the user inputted mean intensity
        save(filename: str, bits: int, save: bool): saves the image with specified bit depth and filename


    '''
    def __init__(self, speckle_pattern: np.ndarray):
        self.image = speckle_pattern
        self.inverted = None
        self.image_intensity = None
        self.contrast = None

    def visualise_pattern(self, inverted: bool = False, contrast: float = 1) -> np.ndarray:
        '''
        inverts the image, allows user to specify a contrast for the image
        Args:
            inverted (bool): if True, greyscale values for whole image invert, contrast (float): between 0 and 1 for the contrast of image (1 is high contrast)
        Returns:
            np.ndarray: speckle pattern
        '''

        if inverted:
            self.image = 1 - self.image

        self.image = self.image*contrast

        plt.imshow(self.image, cmap = 'gray', vmin = 0, vmax = 1)
        return self.image


    def mean_intensity(self, image_intensity) -> None:
        '''
        Allows the user to specify a value for the mean intensity of the image
        Args:
        mean (int): the mean intensity of the image
        Returns:
            None
        '''

        self.image_intensity = image_intensity

        #now need to adjust the greyscale values of each pixel to match the desired intensity 


    def save(self, filename: str, bits: int = 8, save: bool = True) -> None:
        '''
        saves the image as user requests
        Args:
            filename (str): name that the file is saved under
            bits (int): number of bits that encode the saved image (8-bit, 10-bit, 12-bit, 16-bit)
            save (bool): determines if the image is saved
        Returns:
            None
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