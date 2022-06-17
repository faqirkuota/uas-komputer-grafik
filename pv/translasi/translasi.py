import tkinter as tk
from tkinter import font as tkfont
import numpy as np
from matplotlib import pyplot as plt
import math

inputResolusi = ''
inputModel=''
inputTranslasi=''

def translationMaker():
    def createCircleModel(col, row, a, b):
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

    def createSquareModel(col, row, a, b):
        # Square size
        length = 3

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
    def translation(object, u, v, th):
        row, col, depth = np.shape(object)

        obj_out = np.zeros(shape=(row, col, 3), dtype=np.uint8)  # template for output
        for i in range(0, row - u - 1):
            for j in range(0, col - v - 1):
                value = object[i, j, 0] + object[i, j, 1] + object[i, j, 2]
                if value > th:
                    obj_out[i + u, j + v, 0] = object[i, j, 0]
                    obj_out[i + u, j + v, 1] = object[i, j, 1]
                    obj_out[i + u, j + v, 2] = object[i, j, 2]
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

    def square(model):
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

        u = -1
        v = 0
        for i in range(1, 10):
            model_translated = translation(model, u, v, th)
            plt.imshow(model_translated)
            plt.pause(0.01)
            model = model_translated

        u = 0
        v = -1
        for i in range(1, 10):
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

    def zigzag(model, col):

        for j in range(1, int(round(col / 15))):
            u = -1
            v = 1
            th = 15
            for i in range(1, 10):
                model_translated = translation(model, u, v, th)
                plt.imshow(model_translated)
                plt.pause(0.01)
                model = model_translated

            u = 1
            v = 1
            for i in range(1, 10):
                model_translated = translation(model, u, v, th)
                plt.imshow(model_translated)
                plt.pause(0.01)
                model = model_translated
        plt.show()  # syarat menampilkan

    col = 0;
    row = 0
    if inputResolusi.lower() == 'a':
        col = 60;
        row = 60
    elif inputResolusi.lower() == 'b':
        col = 80;
        row = 80
    elif inputResolusi.lower() == 'c':
        col = 100;
        row = 100

    if inputModel.lower() == 'a':
        createSquareModel(col, row, int(round(col / 2)), int(round(row / 2)))
        model = np.load("Square.npy")
    elif inputModel.lower() == 'b':
        createCircleModel(col, row, int(round(col / 2)), int(round(row / 2)))
        model = np.load("Circle.npy")


    if inputTranslasi.lower() == 'a':
        bounce(model)
    elif inputTranslasi.lower() == 'b':
        square(model)
    elif inputTranslasi.lower() == 'c':
        diagonal(model)
    elif inputTranslasi.lower() == 'd':
        if inputModel.lower() == 'a':
            createSquareModel(col, row, int(round(col / 2)), int(round(5)))
            model = np.load("Square.npy")
        elif inputModel.lower() == 'b':
            createCircleModel(col, row, int(round(5)), int(round(row / 2)))
            model = np.load("Circle.npy")
        zigzag(model, col)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilih Resolusi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def chooseResolution(value):
            global inputResolusi
            inputResolusi = value
            controller.show_frame("PageOne")

        button1 = tk.Button(self, text="60 x 60",
                            command=lambda *args: chooseResolution('a'))
        button2 = tk.Button(self, text="80 x 80",
                            command=lambda *args: chooseResolution('b'))
        button3 = tk.Button(self, text="100 x 100",
                            command=lambda *args: chooseResolution('c'))
        button1.pack()
        button2.pack()
        button3.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilih Model", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def chooseModel(value):
            global inputModel
            inputModel = value
            controller.show_frame("PageTwo")

        button1 = tk.Button(self, text="Persegi",
                            command=lambda *args: chooseModel('a'))
        button2 = tk.Button(self, text="Lingkaran",
                            command=lambda *args: chooseModel('b'))
        button1.pack()
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilih Translasi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def chooseTranslation(value):
            global inputTranslasi
            inputTranslasi = value
            controller.show_frame("PageThree")

        button1 = tk.Button(self, text="Bounce",
                            command=lambda *args: chooseTranslation('a'))
        button2 = tk.Button(self, text="Square",
                            command=lambda *args: chooseTranslation('b'))
        button3 = tk.Button(self, text="Diagonal",
                            command=lambda *args: chooseTranslation('c'))
        button4 = tk.Button(self, text="Zig-Zag",
                            command=lambda *args: chooseTranslation('d'))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hasil", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Tampilkan Animasi",
                           command=lambda *args: translationMaker())
        button2 = tk.Button(self, text="Kembali ke laman awal",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()