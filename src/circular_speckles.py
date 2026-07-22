#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft
from scipy.fft import fft, fftfreq
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks

#functions
def userinputs():
    imageheight = int(input("Enter height of image in pixels: "))
    imagewidth = int(input("Enter width of the image in pixels: "))

    specksize = True
    while specksize == True:
        speckle_radius = int(input("Enter the speckle radius in pixels: "))
        if speckle_radius < 3:
            print("Speckles must be at least 3 pixels in radius")
            specksize = True
        else:
            specksize = False


    bwbal = True
    while bwbal == True:
        blackwhite = float(input("Enter the black/white balance as a number between 0.0 and 1.0 (between white and black):  "))
        if blackwhite >= 0.0 and blackwhite <= 1.0:
            bwbal = False
        else:
            print("Please enter a number in the correct range.")
            bwbal = True

    return imagewidth, imageheight, speckle_radius, blackwhite

#calculating my grid
def specklespacing():
    number_of_speckles = imagesize * blackwhite / speckle_size
    speckle_spacing = np.sqrt(imagesize / number_of_speckles)
    return speckle_spacing

#generating the uniform grid
def coordinate_generation():
    x_coords = np.arange(0, imagewidth, speckle_spacing)
    y_coords = np.arange(0, imageheight, speckle_spacing)
    X, Y = np.meshgrid(x_coords, y_coords) #making my grid
    #plt.scatter(X,Y) remove the hash if want to see the original grid

    #generating random displacements
    x_disp = np.random.randint(
        (-1 * speckle_spacing // 2) + 1,
        (speckle_spacing //2) + 1,
        size = X.shape)

    y_disp = np.random.randint(
        (-1 * speckle_spacing // 2) + 1,
        (speckle_spacing // 2) + 1,
        size = Y.shape)
    
    #adding my random displacements to each grid point
    X_new = X + x_disp 
    Y_new = Y + y_disp
    return X_new, Y_new

#new imagegeneration code:
def imagegeneration():
    image = np.full((imageheight, imagewidth), 1.0)
    # splitting each pixel into 16 - 4x4 subpixels
    samples = 4
    offsets = (np.arange(samples) + 0.5) / samples - 0.5

    yy, xx = np.meshgrid(
        np.arange(imageheight),
        np.arange(imagewidth),
        indexing = 'ij')
    for x, y in zip(X_new.ravel(), Y_new.ravel()):
        coverage = np.zeros_like(image, dtype = float)
        for dx in offsets:
            for dy in offsets:
                dist2 = ((xx+dx)-x)**2 + ((yy+dy)-y)**2
                coverage += dist2 <= speckle_radius**2
        coverage /= samples**2
        #need it to be greyscale proportional to how much pixel is being covered
        image = np.minimum(image, 1 - coverage)
    return image

#fft analysis
def fftanalysis():
    x_profile = np.mean(image, axis = 0) #gives 1 value per column
    x_profile = x_profile - np.mean(x_profile)
    x_fft = fft(x_profile)
    #magnitude spectrum
    x_magnitude = np.abs(x_fft)
    #same for the y direction
    y_profile = np.mean(image, axis = 1)
    y_profile = y_profile - np.mean(y_profile)
    y_fft = fft(y_profile)
    y_magnitude = np.abs(y_fft)

    #frequency axis
    freq = fftfreq(len(x_profile), d = 1)

    positive = freq > 0
    freq = freq[positive]
    x_magnitude = x_magnitude[positive]
    y_magnitude = y_magnitude[positive]
    #can take an average magnitude as the speckles are circular - no favourtism between x/y
    avg_magnitude = (x_magnitude + y_magnitude) / 2
    avg_magnitude = gaussian_filter1d(avg_magnitude, sigma = 3) #smoothing out the signal

    peaks, properties = find_peaks(avg_magnitude)
    fft_speckle_size = 1/(freq[peaks[2]])
    return fft_speckle_size

imagewidth, imageheight, speckle_radius, blackwhite = userinputs()
imagesize = imagewidth * imageheight
speckle_size = np.pi * (speckle_radius**2)
speckle_spacing = specklespacing()
X_new, Y_new = coordinate_generation()
image = imagegeneration()
fft_speckle_size = fftanalysis()
plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 1)
plt.savefig('new_speckle_pattern.tiff')

print(f"Estimated average speckle size is {fft_speckle_size:.2f} pixels.")
print(speckle_spacing)
#plt.figure()
#plt.plot(freq, avg_magnitude)
#plt.axvline(
#    peak_frequency,
#    color = 'red',
#    linestyle = '--',
#    )
#plt.xlabel("Spatial frequency (cycles/pixel)")
#plt.ylabel("Magnitude")
#plt.savefig("fft_pattern.tiff")

plt.show()