Python Speckle generator:   
Aim: Develop a python package that can generate an image of a speckle pattern suitable for digital image correlation.  
Inputs & Outputs:   
The user should be required to specify the following parameters:  
* The width and height of the speckle image in pixels
* The size of the speckles in pixels
* The black/white balance as a number from 0.0-1.0
* A lossless format for saving the file (bitmap / tiff)

Optional inputs: the image resolution in ppi (pixels per inch) for printing at the correct scale, if the pattern is black dots on a white background or white dots on a black background. 

Outputs:
* A visualisation of the speckle pattern using matplotlib
* A saved image file in a lossless format (i think that means save it as a.tiff not as a jpeg)
* A fast fourier transform analysis of the average speckle size?????
* extension: diagnostics for the speckle pattern (you will have to dig in the literature to find different algorithms)

Deliverables:
1. A python package openly available on github using an MIT license with the `src` layout
    - readme.md file to help users install the package
    - pyproject.toml file to be able to build the package and get dependencies
    - LICENSE file with the MIT license (should be auto generated during package creation)
2. The github project should have at least 3 branches: main, dev and your dev branch. Setup branch protection rules on main and dev
3. Source code (in the `src`)for creating the speckle pattern broken into modules, classes and functions as necessary

Once you have a decent working version you are happy with move onto these deliverables:
1. A test suite built using `pytest` to help maintain the code
2. Suitable docstrings to explain how the code works
3. A final code review and pull request to main to create v1.0