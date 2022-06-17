import tkinter as tk
from tkinter import font as tkfont
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilih Gambar", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)

        def chooseImage(value):
            global inputNamaFile
            inputNamaFile = value
            controller.show_frame("PageOne")

        button1 = tk.Button(self, text="Alien",
                            command=lambda *args: chooseImage('a'))
        button2 = tk.Button(self, text="Kupu-Kupu",
                            command=lambda *args: chooseImage('b'))
        button3 = tk.Button(self, text="Hellboy",
                            command=lambda *args: chooseImage('c'))
        button1.pack()
        button2.pack()
        button3.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilih Rotasi", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)

        def chooseDeg(value):
            global inputDerajat
            inputDerajat = value
            controller.show_frame("PageTwo")

        button1 = tk.Button(self, text="30º",
                            command=lambda *args: chooseDeg('a'))
        button2 = tk.Button(self, text="40º",
                            command=lambda *args: chooseDeg('b'))
        button3 = tk.Button(self, text="50º",
                            command=lambda *args: chooseDeg('c'))
        button1.pack()
        button2.pack()
        button3.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hasil", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Tampilkan hasil gambar",
                           command=lambda *args: rotation3dMaker())
        button2 = tk.Button(self, text="Kembali ke laman awal",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()