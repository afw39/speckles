import numpy as np

def dots_number(image_width: int, image_height: int, dot_radius: float, black_white_balance: float) -> np.array:

    '''
    calculates how many dots required on speckle pattern to achieve correct black_white_balance
    Args:
        None
    Returns:
        None
    '''
    image_size = image_width * image_height
    dot_size = np.pi * (dot_radius**2)
    number_of_dots = image_size * black_white_balance / dot_size
    dot_spacing = np.sqrt(image_size/number_of_dots)
    return dot_spacing

def displaced_grid(image_width:int, image_height: int, dot_spacing: float) -> np.array:

    '''
    generates random displacements and applies to uniform grid to achieve dot locations
    Args:
        None
    Returns:
        None
    '''
    x_coords = np.arange(0, image_width, dot_spacing)
    y_coords = np.arange(0, image_height, dot_spacing)
    x, y = np.meshgrid(x_coords, y_coords)

    x_displacements = np.random.uniform((-1 * dot_spacing // 2),(dot_spacing // 2), size = x.shape)
    y_displacements = np.random.uniform((-1 * dot_spacing // 2),(dot_spacing // 2), size = y.shape)

    x_new = x+x_displacements
    y_new = y+y_displacements

    return x_new, y_new
