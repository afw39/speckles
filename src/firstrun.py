#okay we gonna try make a pattern with some user inputs then we will fix whatever needs to be fixed.
import numpy as np #for number stuff
import matplotlib.pyplot as plt # for the plots/visualisation

#start with some user inputs:
def inputvalues():
    #need to see that the image size is the right height, might do this as a function to see if their will be enough speckles in the image, run it first to get the measurements and if not, then will run it again to see if they will change it? for now will leave it and im just gonna enter allowed values.
    imagewidth = int(input("Enter image width "))
    imageheight = int(input("Enter image height "))


    #   asking for speckle dimensions and seeing if they are at least 3 x 3
    speckles = True
    while speckles == True:
        specklewidth= int(input("Enter width of speckles. "))
        speckleheight= int(input("Enter height of speckles. "))
        speckle_area = specklewidth * speckleheight
        if specklewidth < 3 or speckleheight < 3:
            print("Speckles must be at least 3 pixels wide and 3 pixels tall. Please try again.")
            speckles = True
        elif speckle_area > 9 and speckleheight > 3 and specklewidth > 3:
            speckles = False
        else:
            speckles = False
    # maybe should also add that there needs to be a certain number of speckles per image (maybe put both the image questions and the speckle questions in the same loop)


    # using this as the density of speckles?
    bw = True
    while bw == True:
        bwbalance = float(input("Enter black and white balance (0.0 is white - 1.0 is black). "))
        if bwbalance < 0.0 or bwbalance > 1.0:
            print("Incorrect value. Please enter a value between 0.0 and 1.0.")
            bw = True
        else:
            bw = False

    return imagewidth, imageheight, specklewidth, speckleheight, bwbalance, speckle_area


imagewidth, imageheight, specklewidth, speckleheight, bwbalance, speckle_area = inputvalues() # calling the function now
#need to make a new variable which takes into account the image size and the speckle size/area and the bwbalance which is the density to work out how many speckles/numbers to generate - that will go into the size bit. 

def speckle_num(imagewidth, imageheight, specklewidth, speckleheight, bwbalance):
    imagearea = (imagewidth * imageheight)
    specklearea = specklewidth * speckleheight
    required_speckle_density = bwbalance
    speckle_num = required_speckle_density * (imagearea / specklearea)
    return int(speckle_num)

number_of_speckles = speckle_num(imagewidth, imageheight, specklewidth, speckleheight, bwbalance)
speckle_area = specklewidth * speckleheight

x_rand = np.random.randint(
    0,
    imagewidth - specklewidth + 1,
    size=number_of_speckles)

y_rand = np.random.randint(
    0,
    imageheight - speckleheight + 1,
    size=number_of_speckles)


#will obv take user inputs for this
plt.xlim(0, imagewidth)
plt.ylim(0, imageheight)
plt.gca().set_aspect('equal')

image = np.ones((imageheight,imagewidth)) #can make two options but cant be bothered (would just change the np.ones to np.zeroes and then when im changing pixel colours would change them to 1 instead of 0 based off of user input.) I would make each one, black on white or white on black background a different function. 

for i in range(number_of_speckles): #changing each pixel one by one to black from white
    image[
        y_rand[i]:y_rand[i] + speckleheight,
        x_rand[i]:x_rand[i] + specklewidth
    ] = 0


print(np.average(image))
plt.imshow(image, cmap = 'gray')
plt.savefig("speckle_image.tiff") # just saving it as only a .tiff cause idk how to make it a bitmap


#now i need to output a fast fourier transform of the average speckle size? obv the minimum speckle size is just whatever the user inputs but when the speckles join together/overlap so the main is kinda alot. 
fft = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft) # moves 0 frequency bit to the centre - easier to read
magnitude = np.abs(fft_shifted)

#display the fft
plt.figure()
plt.imshow(np.log(magnitude+1), cmap = 'gray')
plt.title("FFT Magnitude")
plt.savefig("fft.tiff")


#editing this in the new branch dev now!
#to find average speckle size, need to find the dominant frequency as the speckle size is 1 over the dominant frequency, need to find that then i can find my average speckle size. 

# first step is to compute the FFT power spectrum
power = np.abs(fft_shifted)**2
#next need to calculate the radial distance from the centre
rows, cols = power.shape
cy = rows // 2
cx = cols // 2

y, x = np.indices((rows, cols))

r = np.sqrt((x-cx)**2 + (y+cy)**2)
r = r.astype(int) #need to know what this FFT value is??
#now every FFT pixel has a radius from the centre
counts = np.bincount(r.ravel())
sums = np.bincount(r.ravel(), weights = power.ravel())
radial_profile = sums / np.maximum (counts, 1)
plt.figure()
plt.plot(radial_profile)
plt.xlabel("radius")
plt.ylabel("Average FFT power")


peak_idx = np.argmax(radial_profile[1:])+1


dominant_frequency = peak_idx/imagewidth
average_speckle_size = 1/dominant_frequency
print("estimated speckle size:", average_speckle_size, "pixels")
plt.show()