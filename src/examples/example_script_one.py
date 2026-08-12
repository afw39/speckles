from pathlib import Path
from speckles import Pattern, ImageGeneration, FFTAnalysis

# generate pattern and input parameters
pattern = Pattern(image_width=1500, image_height=1000, dot_radius=5.5, speckle_coverage=0.4)
speckle_pattern = pattern.pattern_generation()
image = ImageGeneration(speckle_pattern)

# adjust for inverting pattern and setting the contrast
image = image.visualise_pattern(inverted=False, contrast=1)

# can set the mean intensity of the image
image = image.mean_intensity(mean_intensity=0.5)

# saving the image
image.save(bits=8, save_path=Path(__file__).parent / 'images' / 'speckle_pattern_1.tiff')

# for the fft
fft = FFTAnalysis(image.image)
fft.fft_analysis()

# to visualise the fft
fft.visual_fft(visual_fft=False)









