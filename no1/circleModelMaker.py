print("Mulai")

import numpy as np
from matplotlib import pyplot as plt
import math

width, height = 11, 11
a, b = 30, 30
r = 2
EPSILON = 2.2

# Screen size
col=60;row=60

# Preparation
plt.figure(figsize=(4,4),dpi=200) #Width and height in inches

#Preparing template for 2D Screen
screen_2d = np.zeros(shape=(row,col,3),dtype=np.uint8)

for angle in range(0, 360, 5):
    x = r * math.sin(math.radians(angle)) + a
    y = r * math.cos(math.radians(angle)) + b
    screen_2d[int(round(y)), int(round(x)), 2] = 255

np.save("Circle"+".npy",screen_2d)
dummy=np.load("Circle.npy")

plt.imshow(dummy)
plt.show()