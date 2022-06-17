import tkinter as tk
from tkinter import font as tkfont
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

inputNamaFile = ''
inputDerajat = ''

def rotation3dMaker():
    class Loader:
        def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
            """
            A loader-like context manager

            Args:
                desc (str, optional): The loader's description. Defaults to "Loading...".
                end (str, optional): Final print. Defaults to "Done!".
                timeout (float, optional): Sleep time between prints. Defaults to 0.1.
            """
            self.desc = desc
            self.end = end
            self.timeout = timeout

            self._thread = Thread(target=self._animate, daemon=True)
            self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
            self.done = False

        def start(self):
            self._thread.start()
            return self

        def _animate(self):
            for c in cycle(self.steps):
                if self.done:
                    break
                print(f"\r{self.desc} {c}", flush=True, end="")
                sleep(self.timeout)

        def __enter__(self):
            self.start()

        def stop(self):
            self.done = True
            cols = get_terminal_size((80, 20)).columns
            print("\r" + " " * cols, end="", flush=True)
            print(f"\r{self.end}", flush=True)

        def __exit__(self, exc_type, exc_value, tb):
            # handle exceptions with those variables ^
            self.stop()

    def modelMaker(nama_file, degree):
        threshold = 15
        no_of_rotations = 1
        pic = plt.imread(nama_file + ".jpg")
        pic = pic.astype(int)

        # Creatin 3D from 2D Picture #
        print("Creating a 3D Model");


        # User Decide The Size 3D Room and 2D Screen #`
        ROW, COL, DEPTH = pic.shape
        LENGTH = COL
        row = ROW - 1;
        col = COL - 1;
        length = LENGTH - 1;
        depth = DEPTH - 1
        half_length = round(length / 2)

        # Creating the template matrix for 3D Model #
        voxel = np.zeros(shape=(row, col, length, 3), dtype=np.uint8)  # Template for 3D Model
        buffer = np.zeros(shape=(row, col, length, 3), dtype=np.uint8)  # Template for 3D Buffer
        slice = np.zeros(shape=(row, col, 3), dtype=np.uint8)  # Template for Slice cut

        # Photocopying #
        voxel[0:row, 0:col, 200, :] = pic[0:row, 0:col, :]
        for k in range(190, 210):
            voxel[0:row, 0:col, k, 0:] = voxel[0:row, 0:col, 200, 0:]

        # Visualizing the cross slice at the half length #
        slice[:, :, :] = voxel[half_length, :, :, :]

        # Visualizing the cross slice at the half length #
        slice[:, :, :] = voxel[:, half_length, :, :]

        # Visualizing the cross slice at the half length #
        slice[:, :, :] = voxel[:, :, half_length, :]

        plt.ion()
        plt.pause(2)
        np.save(nama_file + ".npy", voxel)
        np.save(nama_file + "_0_0.npy", voxel)

        # ===Defining Function For Degree conversion and rotation===#
        # Converting degree unit of alfa and beta radiant unit#
        def degree_to_rad(alfa, beta):
            alfa_rad = (alfa / 100) * np.pi
            beta_rad = (beta / 100) * np.pi
            return alfa_rad, beta_rad

        # Function to rotate voxel (xx,xv,vz) about a defined center (cx,cy,cz) as much as alfa rad
        # Around Z-Axis then as much as beta rad around X-Axis
        def rotate(vx, vy, vz, cx, cy, cz, alfa_rad, beta_rad):
            # Converting point's coordinate to be relative to the rotation center
            # So that the rotation matrix can be applied correctly.
            vx = vx - cx;
            vy = vy - cy;
            vz = vz - cz

            k = 0.6  # Correction Factor
            # Rotation 1 - Rotating the point as much as alfa around Z-Axis
            vx = int(np.cos(alfa_rad * k) * vx + np.sin(alfa_rad * k) * vy)
            vz = int(-np.sin(alfa_rad * k) * vx + np.cos(alfa_rad * k) * vy)
            vz = vz  # The Z-Coordinate of the voxel does not change

            # Rtation 2 - Rotating the point as much as beta around X-Axis
            vz = int(np.cos(beta_rad * k) * vz + np.sin(beta_rad * k) * vy)
            vz = int(-np.sin(beta_rad * k) * vz + np.cos(beta_rad * k) * vy)
            vz = vz  # The X-Coordinate of the voxel does not change

            # Converting point's coordinate back, relative to(8,0,8)
            vx = vx + cx;
            vy = vy + cy;
            vz = vz + cz
            return vx, vy, vz

        # ===Main Program To Rotate The 3D Object===#
        # The object is rotated with the same angle over and over again acc. to number of rotations#
        cx = round(col / 2);
        cy = round(row / 2);
        cz = round(length / 2)  # Center of 3D Object rotation

        alfa = degree
        beta = degree

        for r in range(1, no_of_rotations + 1):
            alfa_rad, beta_rad = degree_to_rad(alfa, beta)  # Convert degree to rad
            voxel = np.load(nama_file + ".npy")  # always read original model
            loader = Loader("Please wait... Creating model in the process", "Finished").start()
            for i in range(0, col):
                for j in range(0, row):
                    for k in range(0, length):
                        cek1 = int(voxel[i, j, k, 0])
                        cek2 = int(voxel[i, j, k, 1])
                        cek3 = int(voxel[i, j, k, 2])
                        if (cek1 + cek2 + cek3) > threshold:
                            u, v, w = rotate(i, j, k, cx, cy, cz, alfa_rad, beta_rad)  # Rotate every voxel
                            buffer[u, v, w, :] = voxel[i, j, k, :]
                            voxel[i, j, k, :] = 0
            loader.stop()
            # Result of one time rotation of object is ready for next rotation
            np.save(nama_file + "_" + str(alfa) + "_" + str(beta) + ".npy", buffer)
            voxel[:, :, :] = 0  # Must be put back to black
            buffer[:, :, :] = 0  # Must be put back to black
            alfa = alfa + degree
            beta = beta + degree

    def pictureRotateMaker(nama_file, degree):
        threshold = 15
        no_of_rotations = 1
        cam_focal = 400

        # User decides the cam positions considering that 3D room Border
        # Z = 8 and at the leftmost 3D Voxel, Z = Lengthe
        # E.G CAM_z = -5 * LENGTH mean that the Cam resides far behind The 3D Room border
        cam_z = -120

        # ===Preparation===#
        voxel = np.load(nama_file + "_0_0.npy")
        maks = max(voxel.shape)
        col, row, length = maks, maks, maks  # Be ensure making a cubic 3D Space and a square 2D Screen

        # Preparing the template for 2D Screen (Black) #
        pixel = np.zeros(shape=(row, col, 3), dtype=np.uint8)

        cx = round(0.5 * col);
        cy = round(0.5 * row)

        # The 2D Screen positions is fixed, that is, analogous the real sensor residing at the cam's focal #
        room_border_z = 0  # The z positions of the 3D room's border its 0.

        # Deciding the size of the 2D Screen
        col = col;
        row = row

        # ===Defining the function for backward projection===#
        def projection(cx, cy, cam_z, screen_z, px, py, vz):
            pz = screen_z
            vx = round(cx + (cx - px) * ((vz - cam_z) / (cam_z - pz)))
            vy = round(cy + (cy - py) * ((vz - cam_z) / (cam_z - pz)))
            return vx, vy

        # ===Main Program===#
        cam_z = -280  # -420
        alfa = degree
        beta = degree
        for i in range(1, no_of_rotations + 1):
            pixel[:, :, :] = 0  # Put the 2D Screen back to black
            voxel = np.load(nama_file + "_" + str(alfa) + "_" + str(beta) + ".npy")
            screen_z = cam_z - cam_focal
            loader = Loader("Please wait... Processing image", "Finished!").start()
            for px in range(0, col):  # x of a pixel of the 2D Screen
                for py in range(0, row):  # y of that pixel
                    for vz in range(0, length):  # z of voxel of the corelating 3D object
                        # Starting from 3D room's border(right to left)
                        vx, vy = projection(cx, cy, cam_z, screen_z, px, py, vz)  # Projection
                        if (vy >= 0 and vy < row and vx >= 0 and vx < col) and \
                                (int(voxel[vy, vx, vz, 0]) + int(voxel[vy, vx, vz, 1]) + int(
                                    voxel[vy, vx, vz, 2]) > threshold):
                            pixel[row - py - 1, col - px - 1, :] = voxel[vy, vx, vz, :]
                            break
            loader.stop()
            plt.imsave(nama_file + "Rotate" + str(degree) + "Derajat" + ".jpg", pixel)
            alfa = alfa + degree
            beta = beta + degree

    def showPicture(nama_file, degree):
        img = mpimg.imread(nama_file + "Rotate" + str(degree) + "Derajat" + ".jpg")
        plt.imshow(img)
        plt.show()

    nama_file = ''
    if inputNamaFile.lower() == 'a':
        nama_file = 'gambarAlien'
    elif inputNamaFile.lower() == 'b':
        nama_file = 'gambarKupukupu'
    elif inputNamaFile.lower() == 'c':
        nama_file = 'gambarHellboy'

    degree = 0
    if inputDerajat.lower() == 'a':
        degree = 30
    elif inputDerajat.lower() == 'b':
        degree = 40
    elif inputDerajat.lower() == 'c':
        degree = 50

    modelMaker(nama_file, degree)
    pictureRotateMaker(nama_file, degree)
    showPicture(nama_file, degree)

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
        for F in (StartPage, PageOne, PageTwo):
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