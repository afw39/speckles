#imports at the top
from speckles import generate_pattern, fftanalysis

#enter dimensions for image (pixels), the black-white balance of the speckle pattern and the speckle radius

#generating the speckle pattern/fft (if necessary). put 'save = True' above if you want the file(s) saved. 
image = generate_pattern(imagewidth = 500, imageheight = 500, speckle_radius = 5, blackwhite = 0.5, save = True)
fftanalysis(image,visualfft = True)
