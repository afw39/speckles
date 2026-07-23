#imports
import numpy as np #for number stuff
import matplotlib.pyplot as plt # for the plots/visualisatio

#speckle size correction now
specklewidth = int(input("speckle width: "))
speckleheight = int(input("speckle height: "))

speckle_area = specklewidth * speckleheight

#image details for ease
imagewidth = 10
imageheight = 10

#so now we generate some random coordiantes for the speckles...
x_rand = np.random.randint(0, 30, size=10)
y_rand = np.random.randint(0, 30, size=10) #10 random numbers

#will obv take user inputs for this
plt.scatter(x_rand, y_rand, s = speckle_area, color = 'black')
plt.show()  