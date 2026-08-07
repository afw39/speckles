from speckles import Image, FFTAnalysis

#enter image dimensions
image_height = 1000
image_width = 1000

# generate pattern and input parameters
pattern = Image(image_width, image_height, dot_radius=5.5, black_white_balance=0.5)
pattern.dots_number()
pattern.displaced_grid()
pattern.image_creation()
pattern.contrast(contrast=1)

# for visualising/inverting the image
speckle_pattern = pattern.visualise_pattern(inverted=False)

# for saving the pattern
pattern.bit_depth_tiff(filename= 'speckle_pattern.tiff',bits= 16,save=True)

#for the fft
fft = FFTAnalysis(speckle_pattern, image_width, image_height)
fft.fft_analysis()

# to visualise the fft
fft.visual_fft(visual_fft=False)
