import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('last.jpg')
print(img)
imgplot = plt.imshow(img)
plt.show()