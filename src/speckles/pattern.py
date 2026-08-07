import numpy as np
import tifffile
import matplotlib.pyplot as plt



class Image:
    ''' doctsring for class - generates pattern ig'''

    def __init__(self, image_width: int, image_height: int, dot_radius: float, black_white_balance: float):
        '''doctsirng -parameters'''

        self.image_width = image_width
        self.image_height = image_height
        self.dot_radius = dot_radius
        self.black_white_balance = black_white_balance
        self.x_new = None
        self.y_new = None
        self.dot_spacing = None
        self.image = None


    def dots_number(self) -> None:
        '''docstring'''
        image_size = self.image_width * self.image_height
        dot_size = np.pi*(self.dot_radius**2)
        number_of_dots = image_size*self.black_white_balance/dot_size
        self.dot_spacing = np.sqrt(image_size/number_of_dots)

        return None
    

    def displaced_grid(self) -> None:
        '''docstring'''
        x_coords = np.arange(0, self.image_width, self.dot_spacing)
        y_coords = np.arange(0, self.image_height, self.dot_spacing)
        x, y = np.meshgrid(x_coords, y_coords)

        x_displacements = np.random.uniform((-1*self.dot_spacing//2),(self.dot_spacing//2), size = x.shape)
        y_displacements = np.random.uniform((-1*self.dot_spacing//2),(self.dot_spacing//2), size = y.shape)

        self.x_new = x+x_displacements
        self.y_new = y+y_displacements

        return None
    

    def image_creation(self) -> np.ndarray:
        '''docstring'''
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

    def visualise_pattern(self, inverted: bool = False) -> None:
        '''docstring'''

        if inverted:
            self.image = 1 - self.image

        plt.imshow(self.image, cmap = 'gray', vmin = 0, vmax = 1)
        return None


    def bit_depth_tiff(self, filename: str, bits: int, save: bool = True) -> None:
        '''docstring'''

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

