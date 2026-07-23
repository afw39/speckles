#imports at the top
from speckles import generate_pattern
from speckles import fftanalysis


#enter dimensions for image (pixels), the black-white balance of the speckle pattern and the speckle radius

imageheight = 50
imagewidth = 50
blackwhite = 0.5
speckle_radius = 5
save = True 
visualfft = True

#generating the speckle pattern/fft (if necessary). put 'save = True' above if you want the file(s) saved. 
generate_pattern(imagewidth, imageheight, speckle_radius, blackwhite, save)
fftanalysis(visualfft)
