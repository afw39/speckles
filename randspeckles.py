#alright in this one we are doing the same thing but instead of asking for the speckle dimensions, we just going to ask for the speckle size and then randomnly generate the dimensions

#imports
import numpy as np #for number stuff
import matplotlib.pyplot as plt # for the plots/visualisation

#inputs
def userinputs():
    imagewidth = int(input("Enter image width "))
    imageheight = int(input("Enter image height "))
    area_of_speckle = int(input("enter speckle size in pixels: "))


    bw = True
    while bw == True:
        bwbalance = float(input("Enter black and white balance (0.0 is white - 1.0 is black). "))
        if bwbalance < 0.0 or bwbalance > 1.0:
            print("Incorrect value. Please enter a value between 0.0 and 1.0.")
            bw = True
        else:
            bw = False
    return imagewidth, imageheight, area_of_speckle, bwbalance


imagewidth, imageheight, area_of_speckle, bwbalance = userinputs()


#from that need to work out how many speckles we are going to have using the function in the other one:
def speckle_num(density, imageheight, imagewidth, area_of_speckle):
    image_size = imageheight * imagewidth
    number_of_speckles = density * image_size / area_of_speckle
    return number_of_speckles

number_of_speckles = speckle_num(bwbalance, imageheight, imagewidth, area_of_speckle)

#gonna make an empty array to store my dimensions in? 
x_dims = [] * number_of_speckles
y_dims = [] * number_of_speckles
#orrrr can i do a 2D one? might leave as 2 1D ones for now will make it easier to plot? 

#so now we know how many speckles we have, this is all the same as before i think. now we are going to generate the dimensions randomnly but then we can probs just use the same code again, we just going to like save an array full of the dimensions for x and y?? dk if you can do that but well try
for i in range(number_of_speckles):
    x_dimension = np.random.randint(1, area_of_speckle, 1) #this how im getting random dimensions but idk how to do this for all of them
    y_dimension = area_of_speckle / x_dimension
    x_dims = np.append(x_dims, x_dimension)




#so think i need to make an array for speckle area and then two corresponding (or maybe i only need one) arrays for x and y dimensions. will change the pixel filling as well but we will see. 