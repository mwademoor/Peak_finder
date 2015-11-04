"""function that generates noisy signal with peak"""
import numpy as np

def generate_array(length, position=0.5, width = 0.1, maximum = 10., noise = True):
    """generates a noisy (if noise = True) array of length 'length' with a Gaussian peak 
           at relative position 'position'*length, with width 'width'*length and maximum 'maximum'.
        PARAMETERS
        ================
        length - specifies the length of the array
        position - specifies the relative position of the single peak. default = 0.5
        width - specifies the relative width of the single peak. default = 0.1
        maximum - specifies the maximum of the single peak. default = 10.
        noise - specifies whether to add noise to the data. default = True
    """
    x = np.linspace(0,1,length)
    if noise: 
        noise = np.random.rand(len(x))
    else:
        noise = np.zeros(len(x))

    peak = maximum * np.exp( - (x - position)**2/width**2 )

    y = np.add(noise,peak)

    return y

   

   

