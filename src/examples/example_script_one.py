from speckles import Pattern, ImageGeneration, FFTAnalysis

image_width = 1000
image_height = 1000

# generate pattern and input parameters
pattern = Pattern(image_width, image_height, dot_radius=5.5, black_white_balance=0.4)
speckle_pattern = pattern.pattern_generation()
image = ImageGeneration(speckle_pattern, image_intensity=0.5)

# adjust for inverting pattern and setting the contrast
image.visualise_pattern(inverted=False, contrast=1)

# can set the mean intensity of the image
image.mean_intensity() 

#saving the image
image.save(filename='speckle_pattern.tiff',bits= 16,save=False)


#for the fft
fft = FFTAnalysis(image.image, image_height, image_width)
fft.fft_analysis()

# to visualise the fft
fft.visual_fft(visual_fft=False)

