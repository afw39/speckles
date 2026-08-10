from speckles import OtherPattern

pattern = OtherPattern(image_width=1000, image_height=1000, speckle_width=5.5, speckle_height=5.5, black_white_balance=0.6)
pattern.number_of_dots()
pattern.pattern()

# to invert/set contrast of the pattern
pattern.invert_contrast(inverted=False, contrast=1)

# to visualise the pattern
pattern.visualisation()
pattern.save(bits=256, filename='alternate_speckle_pattern.tiff', save=False)