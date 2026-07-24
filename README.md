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
|       |---- alternate_pattern.py  #pattern generated from filling random pixels on a white image - uses rectangular speckles
|       |---- fft.py                #fast fourier transform analysis module, outputs the average speckle size in pixels
|       |---- pattern.py            #pattern generated from random displacements from uniform grid - uses circular speckles
|---- examples/
|       |---- example_scrpit_one.py #runs the pattern in pattern.py and fft.py
|       |---- example_script_two.py #runs the alternate pattern generation

```
