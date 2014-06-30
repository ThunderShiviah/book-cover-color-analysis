import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

"""
Maps a list of triplets (rgb values) to a grid.
"""

data2 = [[[ 1,  0,  0],
        [ 0,  1,  0]]]

print np.shape(data2)

data2array = np.array(data2)

imgplot = plt.imshow(data2array,interpolation='nearest')   #Note: it seems like I need to specify nearest or else it gets blurry.

plt.show(imgplot)
