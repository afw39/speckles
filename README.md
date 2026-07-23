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
* `speckle_generation.py` generates the pattern by plotting a uniform grid of speckles based on the image size and the speckle spacing and displacing each point/speckle by a randomnly generated amount within a range. This allows you to quantify 'how random' the pattern is if you wanted to. There is fourier analysis outputting the average speckle size (different from inputted speckle dimensions as the speckles overlap/connect) of each pattern. 
* `alternate_speckle_generation.py` generates the speckle pattern by simply creating a white image of the dimensions inputted by the user and then randomnly generating points/speckles and changing those pixels to black. The input for black and white balance is treated as a measure of the 'density of speckles' which is used with the image size and speckle size to calculate how many speckles/points need to be generated. There is no fourier analysis in this module.
* `circular_speckles.py`

```
.gitignore
LICENSE
README.md
pyproject.toml
src/
|---- alternate_speckle_generation.py  #generation of speckle pattern via random coordinate generation
|---- speckle_generation.py            #generation of speckle pattern via random displacements from uniform grid.

```

## Example scripts
also need to work out how to do this

To do today: (22/07/29)

make a list of things to ask lloyd about = before lunch! (example scripts)
finish my speckles/tidy up the fileage (keep the three different files on main branch, only have circular on dev but keep the code on dev for plotting the fft incase its needed and delete circles branch - this branch!)
finish first part of DIC presentation
try get happy with practice lab contents
watch more MatchID lectures
