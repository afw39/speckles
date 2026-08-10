from pathlib import Path
from speckles import OtherPattern

pattern = OtherPattern(image_width=1000, image_height=1000, speckle_width=5.5, speckle_height=5.5, speckle_coverage=0.6)
pattern.number_of_dots()
pattern.pattern()

# to invert/set contrast of the pattern
pattern.invert_contrast(inverted=False, contrast=1)

# to visualise the pattern
pattern.visualisation()

# to save the pattern
pattern.save(bits=8, save_path=Path(__file__).parent / 'images' / 'alternate_speckle_pattern.tiff')
