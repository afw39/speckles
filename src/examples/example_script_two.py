from pathlib import Path
from speckles import Pattern, ImageGeneration, FFTAnalysis

# generate pattern and input parameters
pattern = Pattern(image_width=1000, image_height=1000, dot_radius=4.2, speckle_coverage=0.7)
speckle_pattern = pattern.pattern_generation()
image = ImageGeneration(speckle_pattern)

# adjust for inverting pattern and setting the contrast
image.visualise_pattern(inverted=True, contrast=0.8)

# can set the mean intensity of the image

# set the mean intensity
image.mean_intensity(mean_intensity=0.6)

# saving the image
image.save(bits=12, save_path=Path(__file__).parent / 'images' / 'speckle_pattern_2.tiff')

# for the fft
fft = FFTAnalysis(image.image)
fft.fft_analysis()

# to visualise the fft
fft.visual_fft(visual_fft=True)

