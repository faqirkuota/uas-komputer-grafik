print("Mulai")

import numpy as np
from matplotlib import pyplot as plt

# Square size
length=3

# Square Position
a,b=30,30

# Screen size
col=60;row=60

# Preparation
plt.figure(figsize=(4,4),dpi=200) #Width and height in inches

#Preparing template for 2D Screen
screen_2d = np.zeros(shape=(row,col,3),dtype=np.uint8)

hl=round(length/2) #Half Lenght

#Drawing Square
for j in range (a-hl,a+hl):
    for i in range (b-hl,b+hl):
        screen_2d[j,i,2]=255

np.save("Square"+".npy",screen_2d)
dummy=np.load("Square.npy")

plt.imshow(dummy)
plt.show()