from speckles import Pattern, ImageGeneration, FFTAnalysis

image_width = 1000
image_height = 1000

# generate pattern and input parameters
pattern = Pattern(image_width, image_height, dot_radius=5.5, black_white_balance=0.2)

# this should save the speckle pattern under 'speckle_pattern'
#speckle_pattern = pattern.pattern_generation()

# now running the 'speckle_pattern' through to generate the image
image = ImageGeneration(pattern.pattern_generation(), image_intensity=0.5, inverted=False, contrast=1)
image.save(filename='speckle_pattern.tiff',bits= 16,save=True)

#for the fft
fft = FFTAnalysis(image.image, image_height, image_width)
fft.fft_analysis()

# to visualise the fft
fft.visual_fft(visual_fft=False)

