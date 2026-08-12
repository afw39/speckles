# Python Speckle Generator 

## Overview
This is a simple python package for generation of a speckle pattern based on user inputs for variables such as image dimensions, dot radius and speckle coverage. The image of the speckle pattern is customisable. The use is able to change the contrast, the mean intensity and whether or not the pattern is black dots on a white background or white dots on a black background. It perfoms fast fourier transform analysis on the generated speckle pattern and determines the average speckle size and gives a visualisation of the pattern if desired.

## How to install
clone the repository and install package:
```
git clone <repository-url>
cd speckles
python3 -m pip install -e
```

## Structure of package
The package has four source code modules for creating a speckle pattern image:
* `pattern.py` generates the pattern from a uniform grid based on the image size and the speckle spacing and displacing each point/speckle by a randomnly generated amount within a range. This allows you to quantify 'how random' the pattern is if you wanted to. Takes inputs for image dimensions, dot radius, speckle coverage for the pattern. 
* `fft.py` module for performing the fft analysis of the pattern, takes user inputs for saving/outputting the fourier spectrum. Outputs the average speckle size in pixels and the fft spectrum if desired
* `image.py` generates the speckle image from the speckle pattern - can customise the pattern here: change the contrast, mean intensity and choose whether or not to invert the greyscale of the pattern. 
* `spacing.py` holds two functions used to calculate the grid spacing/number of speckles needed based on the value taken for speckle coverage, also calculates the random displacements of the grid points. 

```
.gitignore
LICENSE
README.md
pyproject.toml
src/
|
|---- speckles/
|       |---- __init__.py
|       |---- fft.py                # fast fourier transform analysis module, outputs the average speckle size in pixels
|       |---- image.py              # makes image from the pattern, saves and customises pattern to user specification
|       |---- pattern.py            # pattern generated from random displacements from uniform grid - uses circular speckles
|       |---- spacing.py            # grid making functions, determines number of speckles and grid spacing
|---- examples/
|       |---- images                
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

### ImageGeneration Class

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


## Examples
#### example_script_one.py

First example using the speckle generator: 

<img width="1514" height="637" alt="image" src="https://github.com/user-attachments/assets/a9a36e3e-167c-4388-9df7-93b43ffdc46f" />

This example script would output a speckle pattern image of dimensions 1500 x 1000 (pixels), dot radius of 5.5 pixels and a 40% speckle coverage. The image would not be inverted so will have black dots on a white background and a maximum contrast of 1. The mean intensity of the image would be 0.5 and the image would be saved as an 8-bit image in the file 'speckle_pattern_1.tiff' within the images folder in the examples folder. The FFT spectrum would not be shown as `visual_fft` is set to `False`, the fft analysis is still performed and the average speckle size would be printed out. This is what the speckle pattern would look like:

<img width="2402" height="1169" alt="image" src="https://github.com/user-attachments/assets/56f987f0-eddc-40c2-ad52-49fed27c9c64" />

The file that the image is saved as will have no axes and will be saved just as the raw pattern. These parameters give an average speckle size of 20.8 pixels

#### example_script_two.py
Using the same speckle pattern generator but demonstrating use of different values for parameters.  
<img width="1696" height="705" alt="image" src="https://github.com/user-attachments/assets/a935b0d3-015c-49ae-b9e0-0489ee50e5ff" />

This example script will create and output a speckle pattern image of dimensions 1000 x 1000 pixels, dot radius of 4.2 pixels and speckle coverage of 70%. The `inverted` parameter is set to `True` so the pattern will be white dots on a black background with a contrast of 0.8. The pattern is given a mean intensity of 0.6 and the image will be saved as a 12-bit image under the name 'speckle_pattern_2.tiff'. This script will also visualise the fft spectrum as `visual_fft` is set to True. The speckle pattern output and the saved image file are:

<img width="644" height="565" alt="image" src="https://github.com/user-attachments/assets/27a4e4fd-b5c3-4136-8f1b-71a6e10197ea" />
<img width="1009" height="1014" alt="image" src="https://github.com/user-attachments/assets/093fb62e-5312-4c03-a821-a59560440b74" />

The fft spectrum that is displayed:

<img width="957" height="682" alt="image" src="https://github.com/user-attachments/assets/71a7cb59-0bc7-41b8-8806-de04618223e9" />

The average speckle size is also outputted as 24.5 pixels.
