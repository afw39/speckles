# Python Speckle Generator 

## Overview
This is a simple python package for generation of a speckle pattern based on user inputs for variables such as imageheight, imagewidth, speckle_radius, black and white balance. It perfoms fast fourier transform analysis on the generated speckle pattern and determines the average speckle size and gives a visualisation of the pattern. 

## How to install
clone the repository and install package:
```
git clone <repository-url>
cd speckles
python3 -m pip install -e
```

## Structure of package
The package has three source code modules for two different ways of generating random speckles:
* `pattern.py` generates the pattern by plotting a uniform grid of speckles based on the image size and the speckle spacing and displacing each point/speckle by a randomnly generated amount within a range. This allows you to quantify 'how random' the pattern is if you wanted to. Takes inputs for image dimensions, speckle radius, black and white balance for the pattern. 
* `fft.py` module for performing the fft analysis of the pattern, takes user inputs for saving/outputting the fourier spectrum. Outputs the average speckle size in pixels
* `alternate_speckle_generation.py` generates the speckle pattern by simply creating a white image of the dimensions inputted by the user and then randomnly generating points/speckles and changing those pixels to black. The input for black and white balance is treated as a measure of the 'density of speckles' which is used with the image size and speckle size to calculate how many speckles/points need to be generated. There is no fourier analysis in this module.

```
.gitignore
LICENSE
README.md
pyproject.toml
src/
|
|---- speckles/
|       |---- __init__.py
|       |---- alternate_pattern.py  # pattern generated from filling random pixels on a white image - uses rectangular speckles
|       |---- fft.py                # fast fourier transform analysis module, outputs the average speckle size in pixels
|       |---- image.py              # makes image from the pattern, saves and customises pattern to user specification
|       |---- pattern.py            # pattern generated from random displacements from uniform grid - uses circular speckles
|       |---- spacing.py            # grid making functions, determines number of speckles and grid spacing
|---- examples/
|       |---- images                # saves speckle patterns in here
|               |---- alternate_speckle_pattern.tiff
|               |---- speckle_pattern.tiff
|       |---- example_scrpit_one.py # runs the pattern in pattern.py and fft.py
|       |---- example_script_two.py # runs the alternate pattern generation

```
## Key Classes and Methods

### Pattern Class

Generates the speckle pattern from user inputs.

#### Attributes
* `image_height (int), image_width (int)`: dimensions of image in pixels
* `dot_radius (float)`: radius of dots used to create speckle pattern
* `speckle_coverage (float)`: measure of the density of speckles - ratio between black and white pixels

#### Methods
* `pattern_generation() -> None`: creates the image and fills in dots to create initial speckle pattern

### Image Class

Customises the pattern to create image with user specified porperties

#### Attributes
* `speckle_pattern (np.ndarray)`: speckle pattern generated in `Pattern` Class
* `mean_intensity (float)`: desired mean intensity of image as a fraction of bit depth (0-1 scale)
* `inverted (bool)`: determines whether image inverts or not (black speckles on white background is inverted)
* `contrast (float)`: desired contrast of the image as a fraction of bit depth (0-1 scale)
* `bits (int)`: how many bits the image is saved to (can be 8-bit, 10-bit, 12-bit or 16-bit)
* `save_path (str)`: determines where the image is saved/if it is saved at all

#### Methods
* `visualise_pattern(inverted: bool, contrast: float) -> None`: if desired, inverts image
* `mean_intensity() -> np.ndarray`: changes brightness/intensity of image based on user input
* `save(bits: int, save_path: Path | None = None) -> None`: saves the image with specified bit depth and path

### FFTAnalysis Class

Performs fast fourier transform analysis on the image to determine average speckle size

#### Attributes
* `image (np.ndarray)`: the result from the Image Class
*

### Other Pattern Class