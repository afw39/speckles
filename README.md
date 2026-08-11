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
* `visual_fft (bool)`: determines if the fft is visualised

#### Methods
* `fft_analysis() -> None`: computes the average speckle size using fft analysis
* `visual_fft(visual_fft) -> None`: plots fft spectrum and displays if user desires along with speckle pattern

### Other Pattern Class

Generates speckle pattern using alternate method of randomnly filling in rectangles of user specified dimensions

#### Attributes
* `image_width, image_height (int)`: image dimensions (pixels)
* `speckle_width, speckleheight (int)`: dimensions of dots on speckle pattern (pixels)
* `black_white_balance (float)`: proportion of black to white pixels
* `inverted (bool)`: if True, generates an inverted image
* `save_path (str)`: where/if file is saved
* `bits (int)`: how many bits make up the image (8-bit, 10-bit, 12-bit or 16-bit)

#### Methods
* `number-of_dots() -> None`: calculates the number of speckles required on pattern using the speckle/image dimensions
* `pattern() -> np.ndarray`: generates the random locations of the centre of the dots and fills any pixels within the dots in
* `inverted(inverted: bool) -> None`: inverts the speckle pattern if inverted = True
* `visualisation() -> None`: plots the speckle pattern
* `save(bits: int, save_path: Path | None = None) -> None`: saves the image to specified bit-depth


## Examples
#### example_script_one.py

First example using the speckle generator: 

<img width="1206" height="642" alt="image" src="https://github.com/user-attachments/assets/6774b6c5-67a5-4812-adc0-68b4056c30a4" />

This example script would output a speckle pattern image of dimensions 1000 x 1000 (pixels), dot radius of 5.5 pixels and a 40% speckle coverage. The image would not be inverted so will have black dots on a white background and a maximum contrast of 1. The mean intensity of the image would be 0.5 and the image would be saved as an 8-bit image in the file 'speckle_pattern_1.tiff' within the images folder in the examples folder. The FFT spectrum would not be shown as `visual_fft` is set to `False` and the average speckle size would be printed out. This is what the speckle pattern would look like:

<img width="1119" height="1089" alt="image" src="https://github.com/user-attachments/assets/c0aca91f-aaa7-4c71-b629-d87e72f48251" />

The file that the image is saved as will have no axes and will be saved just as the raw pattern. These parameters give an average speckle size of 20.8 pixels

#### example_script_two.py
Using the same speckle pattern generator but demonstrating use of different values for parameters.  

<img width="1534" height="461" alt="image" src="https://github.com/user-attachments/assets/1972a473-573c-4fd5-902a-a40af63a4fa0" />

This example script will create and output a speckle pattern image of dimensions 1500 x 1000 pixels, dot radius of 4.2 pixels and speckle coverage of 70%. The `inverted` parameter is set to `True` so the pattern will be white dots on a black background with a contrast of 0.6. The pattern is given a mean intensity of 0.8 and the image will be saved as a 12-bit image under the name 'speckle_pattern_2.tiff'. This script will also visualise the fft spectrum as it is 
