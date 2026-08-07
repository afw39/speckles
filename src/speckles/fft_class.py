from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

class FFT_Analysis():
    '''docstring'''

    def __init__(self, image: np.ndarray, image_height: int, image_width: int):
        '''doc'''

        self.image_height = image_height
        self.image_width = image_width
        self.image = image
        self.average_speckle_size = None
        self.bin_centres = None
        self.radial_mean = None

    def fft_analysis(self) -> None:
        '''doc'''

        self.image_width, self.image_height = self.image.shape

        frequency_y = np.fft.fftshift(np.fft.fftfreq(self.image_height))
        frequency_x = np.fft.fftshift(np.fft.fftfreq(self.image_width))
        freq_x, freq_y = np.meshgrid(frequency_x, frequency_y)
        radial_freq = np.sqrt(freq_x**2 + freq_y**2)
        f_f_t = np.fft.fftshift(np.fft.fft2(self.image))
        magnitude = np.abs(f_f_t)

        radial = radial_freq.ravel()
        mag = magnitude.ravel()
        mask = radial > 0
        radial = radial[mask]
        mag = mag[mask]

        bins = np.linspace(0, radial_freq.max(), 200)
        self.radial_mean = np.zeros(len(bins) - 1)

        for i in range(len(bins) - 1):
            mask = (radial >= bins[i]) & (radial < bins[i + 1])

            if np.any(mask):
                self.radial_mean[i] = np.mean(mag[mask])

        self.bin_centres = 0.5 * (bins[:-1] + bins[1:])

        peaks, _ = find_peaks(self.radial_mean)
        peak_idx = peaks[1]
        peak_freq = self.bin_centres[peak_idx]
        self.average_speckle_size = 1 / peak_freq

        print(f'average speckle size of pattern is {self.average_speckle_size:.1f} pixels')

    def visual_fft(self, visual_fft: bool = False):
        '''docstring'''
        if visual_fft:
            plt.figure(figsize = (8,4))
            plt.plot(self.bin_centres, np.log1p(self.radial_mean))
            plt.xlabel('radial frequency')
            plt.ylabel('mean fft mag')
            plt.title('radial fft profile')
            plt.grid(True)

        plt.show()
            
        