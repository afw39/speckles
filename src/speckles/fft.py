#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks

def fftanalysis(image, visualfft):
    x_profile = np.mean(image, axis =0)
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

    #to visualise the spectrum
    if visualfft:
        plt.figure()
        plt.plot(freq, avg_magnitude)
        plt.axvline(freq[peaks[2]], color = 'black')
        plt.xlabel("Spatial frequency (cycles per pixel)")
        plt.ylabel("magnitude")
        plt.savefig("fft_pattern.tiff")
    
    print(f"Estimated average speckle size is {fft_speckle_size:.2f}")
    plt.show()
