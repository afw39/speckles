# Python Speckle Generator 

## Overview
This is a simple python package for generation of a speckle pattern based on user inputs for variables such as imageheight, imagewidth, speckle size, black and white balance and the speckle spacing. It perfoms fast fourier analysis on the generated speckle pattern and determines the average speckle size and gives a visualisation of the pattern. 

## How to install
clone the repository and install package:
```
git clone <repository-url>
cd speckles
pip install
```

## Structure of package
The package has two source code modules for two different ways of generating random speckles:
* `speckle_generation.py` generates the pattern by plotting a uniform grid of speckles based on the image size and the speckle spacing and displacing each point/speckle by a randomnly generated amount within a range. This allows you to quantify 'how random' the pattern is if you wanted to.
* `alternate_speckle_generation.py` generates the speckle pattern by simply creating a white image of the dimensions inputted by the user and then randomnly generating points/speckles within image dimensions and changing those pixels to black. The input for black and white balance is treated as a measure of the 'density of speckles' which is used with the image size and speckle size to calculate how many speckles/points need to be generated. There is no fourier analysis in this module.
* `circular_speckles.py` generates speckle pattern also by creating a white image and adding a uniform grid over the top. These grid points are then given random displacements in x and y and then the new random points/speckles are plotted - however these speckles are plotted as circles not as squares/rectangles. Inputs are the image dimensions, the black and white balance and the speckle radius. It also splits each pixel into 16 subpixels and quantifies what proportion of that pixel is also in the radius and colours it accordingly, so the pixels appear more circular. There is fourier analysis to calculate the average speckle size which is outputted to the user. 

```
.gitignore
LICENSE
README.md
pyproject.toml
src/
|---- alternate_speckle_generation.py  #generation of speckle pattern via random coordinate generation
|---- circular_speckles.py             #generation of circular speckles via grid displacements
|---- speckle_generation.py            #generation of speckle pattern via random displacements from uniform grid.

```

## Example scripts
also need to work out how to do this
