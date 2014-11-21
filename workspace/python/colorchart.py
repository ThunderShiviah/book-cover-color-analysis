import numpy as np
import matplotlib.pyplot as plt


# Make some random data to represent your r, g, b bands.
ny, nx = 2, 2
r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)] # this generates a random list of length nx*ny and then reformats it into an array of dimensions (nx, ny)

#r, g, b = [199,183,184]
#r, g, b = [float(r),float(g),float(b)]
print r, g, b  
c = np.dstack([r,g,b])
#c = c/255 #divide by 255 to normalize for matplotlib and display correct colors
print c
plt.imshow(c, interpolation='nearest')
plt.show()

