import tkinter as tk
from tkinter import font as tkfont
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


bars_Num = 0
first_Num = 0
second_Num = 0
third_Num = 0
fourth_Num = 0
five_Num = 0
sixth_Num = 0
seven_Num = 0
eight_Num = 0
nine_Num = 0
ten_Num = 0

var_list = [first_Num, second_Num, third_Num, fourth_Num, five_Num, sixth_Num, seven_Num, eight_Num, nine_Num,
            ten_Num]

def create3dMapping():
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    xpos = []
    ypos = []
    zpos = []
    dx = []
    dy = []
    dz = [first_Num, second_Num, third_Num, fourth_Num, five_Num, sixth_Num,
          seven_Num, eight_Num, nine_Num, ten_Num]
    increment = 2
    print(bars_Num)
    for i in range(0, bars_Num):
        if i == 0:
            xpos.append(increment)
        elif i % 2 != 0:
            xpos.append(xpos[i - 1])
        else:
            xpos.append(xpos[i - 1] + 2)

    for i in range(0, bars_Num):
        if i % 2 != 0:
            ypos.append(2)
        else:
            ypos.append(4)

    for i in range(0, bars_Num):
        zpos.append(0)
        dx.append(1)
        dy.append(1)

    # add bars
    bars = []
    for i in range(bars_Num):
        if 0 <= dz[i] <= 5:
            bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='r'))
        elif 5 <= dz[i] <= 7:
            bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='b'))
        elif 7 <= dz[i] <= 10:
            bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='g'))
    ax.set_title("Matrix Penilaian Siswa")
    plt.show()

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
        label = tk.Label(self, text="Jumlah Siswa ? ")
        bars_NumInternal = tk.IntVar()

        entry = tk.Entry(self,textvariable=bars_NumInternal,justify='center')
        label.pack(side="top", fill="x", pady=20)
        entry.pack()
        label1 = tk.Label(self, text="")
        label1.pack()

        def insertBars(value):
            global bars_Num
            bars_Num = value
            controller.show_frame("PageOne")

        button1 = tk.Button(self, text="Buat",
                            command=lambda *args: insertBars(bars_NumInternal.get()))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        def tampilkanInput(self):
            first_Num_Input = tk.IntVar()
            second_Num_Input = tk.IntVar()
            third_Num_Input = tk.IntVar()
            fourth_Num_Input = tk.IntVar()
            five_Num_Input = tk.IntVar()
            sixth_Num_Input = tk.IntVar()
            seven_Num_Input = tk.IntVar()
            eight_Num_Input = tk.IntVar()
            nine_Num_Input = tk.IntVar()
            ten_Num_Input = tk.IntVar()
            var_list_Input = [first_Num_Input, second_Num_Input, third_Num_Input, fourth_Num_Input, five_Num_Input,
                              sixth_Num_Input,
                              seven_Num_Input, eight_Num_Input, nine_Num_Input,
                              ten_Num_Input]
            for i in range(0, bars_Num):
                label = tk.Label(self, text='Nilai Siswa Ke-' + str(i + 1))
                entry = tk.Entry(self, textvariable=var_list_Input[i], justify='center')
                label.pack()
                entry.pack()

            def assignValue():
                global first_Num
                first_Num = int(first_Num_Input.get())

                global second_Num
                second_Num = int(second_Num_Input.get())

                global third_Num
                third_Num = int(third_Num_Input.get())

                global fourth_Num
                fourth_Num = int(fourth_Num_Input.get())

                global five_Num
                five_Num = int(five_Num_Input.get())

                global sixth_Num
                sixth_Num = int(sixth_Num_Input.get())

                global seven_Num
                seven_Num = int(seven_Num_Input.get())

                global eight_Num
                eight_Num = int(eight_Num_Input.get())

                global nine_Num
                nine_Num = int(nine_Num_Input.get())

                global ten_Num
                ten_Num = int(ten_Num_Input.get())
                print("Assign Nilai Berhasil")

            buttonAssign = tk.Button(self, text="Assign Nilai!",
                                     command=lambda *args: assignValue())
            buttonAssign.pack()
            button1 = tk.Button(self, text="Proses",
                                command=lambda: controller.show_frame("PageTwo"))

            button1.pack()

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Input Nilai", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)
        buttonT = tk.Button(self, text="Tampilkan Kolom Assign Nilai",
                            command=lambda *args: tampilkanInput(self))
        buttonT.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hasil", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Tampilkan hasil 3D Mapping",
                           command=lambda *args: create3dMapping())
        button2 = tk.Button(self, text="Kembali ke laman awal",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()