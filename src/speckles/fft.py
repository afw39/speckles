from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

def fft_analysis(image_height: int, image_width: int, image: np.ndarray):
    '''
    Performs fast fourier transform (fft) analysis on the speckle pattern generated in order to determine the average speckle size. Parameters:
    - image_height, image_width (int) = image dimensiosn
    - image (array) = speckle pattern generated in `pattern.py`
    '''

    image_height, image_width = image.shape
    frequency_y = np.fft.fftshift(np.fft.fftfreq(image_height))
    frequency_x = np.fft.fftshift(np.fft.fftfreq(image_width))
    freq_x, freq_y = np.meshgrid(frequency_x, frequency_y)
    radial_freq = np.sqrt(freq_x**2 + freq_y**2)
    f_f_t = np.fft.fftshift(np.fft.fft2(image))
    magnitude = np.abs(f_f_t)

    radial = radial_freq.ravel()
    mag = magnitude.ravel()
    mask = radial > 0
    radial = radial[mask]
    mag = mag[mask]

    bins = np.linspace(0, radial_freq.max(), 200)
    radial_mean = np.zeros(len(bins) - 1)

    for i in range(len(bins) - 1):
        mask = (radial >= bins[i]) & (radial < bins[i + 1])

        if np.any(mask):
            radial_mean[i] = np.mean(mag[mask])

    bin_centres = 0.5 * (bins[:-1] + bins[1:])

    peaks, _ = find_peaks(radial_mean)
    peak_idx = peaks[1]
    peak_freq = bin_centres[peak_idx]
    average_speckle_size = 1 / peak_freq

    print(f'average speckle size of pattern is {average_speckle_size:.1f} pixels')
    return bin_centres, radial_mean

def fft_visualisation(bin_centres: np.array, radial_mean: np.array) -> None:
    ''' 
    Function to visualise the fft plot, plots `bin_centres` against `radial_mean` to see the peaks 
    '''
    plt.figure(figsize = (8,4))
    plt.plot(bin_centres, np.log1p(radial_mean))
    plt.xlabel('radial frequency')
    plt.ylabel('mean fft mag')
    plt.title('radial fft profile')
    plt.grid(True)
    plt.show()