print("Mulai")

import numpy as np
from matplotlib import pyplot as plt
import math

# MODEL
def createCircleModel(col,row):
    a, b = col/2, row/2
    r = 2

    # Preparation
    plt.figure(figsize=(4, 4), dpi=200)  # Width and height in inches

    # Preparing template for 2D Screen
    screen_2d = np.zeros(shape=(row, col, 3), dtype=np.uint8)

    for angle in range(0, 360, 5):
        x = r * math.sin(math.radians(angle)) + a
        y = r * math.cos(math.radians(angle)) + b
        screen_2d[int(round(y)), int(round(x)), 2] = 255

    np.save("Circle" + ".npy", screen_2d)

def createSquareModel(col,row):
    # Square size
    length = 3

    # Square Position
    a, b = int(round(col/2)), int(round(row/2))

    # Preparation
    plt.figure(figsize=(4, 4), dpi=200)  # Width and height in inches

    # Preparing template for 2D Screen
    screen_2d = np.zeros(shape=(row, col, 3), dtype=np.uint8)

    hl = round(length / 2)  # Half Lenght

    # Drawing Square
    for j in range(a - hl, a + hl):
        for i in range(b - hl, b + hl):
            screen_2d[j, i, 2] = 255

    np.save("Square" + ".npy", screen_2d)



# TRANSLASI
def translation(object,u,v,th):
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

def bounce(model):
    u = 1
    v = 0
    th = 15

    for i in range(1, 25):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = -1;
    v = 0
    for i in range(1, 51):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    plt.show()  # syarat menampilkan

def around(model):
    u = 1
    v = 0
    th = 15

    for i in range(1, 10):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = 0
    v = 1
    for i in range(1, 10):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = -1;
    v = 0
    for i in range(1, 10):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = 0;
    v = -1
    for i in range(1, 10):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    plt.show()  # syarat menampilkan

def zigzag(model):
    u = 1
    v = -1
    th = 15

    for i in range(1, 25):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = -1;
    v = 0
    for i in range(1, 51):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    plt.show()  # syarat menampilkan

def diagonal(model):
    u = 1
    v = -1
    th = 15

    for i in range(1, 25):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    u = -1;
    v = 1
    for i in range(1, 51):
        model_translated = translation(model, u, v, th)
        plt.imshow(model_translated)
        plt.pause(0.01)
        model = model_translated

    plt.show()  # syarat menampilkan

## MAIN PROGRAM ##
print("Pilih Resolusi")
print("A. 60 x 60")
print("B. 80 x 80")
print("C. 90 x 90")

inputResolusi = input("Pilih Resolusi  : ")
col=0;row=0
if inputResolusi.lower() == 'a':
    col=60;row=60
    print('A')
elif inputResolusi.lower() == 'b':
    col=80;row=80
    print('B')
elif inputResolusi.lower() == 'c':
    col=90;row=90
    print('C')

print("Pilih Model")
print("A. Persegi")
print("B. Lingkar")

inputModel = input("Pilih Model : ")
if inputModel.lower() == 'a':
    createSquareModel(col,row)
    model = np.load("Square.npy")
    print('A')
elif inputModel.lower() == 'b':
    createCircleModel(col,row)
    model = np.load("Circle.npy")
    print('B')

print("Pilih Translasi")
print("A. Bounce")
print("B. Around")
print("C. Diagonal")
print("D. Zig-Zag")

inputTranslasi = input("Pilih Translasi : ")
if inputTranslasi.lower() == 'a':
    bounce(model)
elif inputTranslasi.lower() == 'b':
    around(model)
elif inputTranslasi.lower() == 'c':
    diagonal(model)
elif inputTranslasi.lower() == 'c':
    zigzag(model)