print("Mulai")

import numpy as np
from matplotlib import pyplot as plt

# Translasi
def translasi(object,u,v,th):
    row,col,depth=np.shape(object)
    print("Row, Col, Depth = ",row,col,depth)
    print("u, v, th=",u,v,th)

    obj_out=np.zeros(shape=(row,col,3),dtype=np.uint8)#template for output
    for i in range(0,row-u-1):
        for j in range(0,col-v-1):
            value=object[i,j,0]+object[i,j,1]+object[i,j,2]
            if value>th:
                obj_out[i+u,j+v,0]=object[i,j,0]
                obj_out[i+u,j+v,1]=object[i,j,1]
                obj_out[i+u,j+v,2]=object[i,j,2]
    return obj_out


u=1;v=0;th=15
model = np.load("Circle.npy")
row,col,depth=np.shape(model)
model_translated=translasi(model,u,v,th)
plt.figure(figsize=(3,3),dpi=200)
plt.imshow(model)


u = 1; v = 0
for i in range(1,25):
    model_translated = translasi(model, u, v, th)
    plt.imshow(model_translated)
    plt.pause(0.01)
    model = model_translated

u = -1; v = 0
for i in range(1,51):
    model_translated = translasi(model, u, v, th)
    plt.imshow(model_translated)
    plt.pause(0.01)
    model = model_translated

plt.show() #syarat menampilkan
