
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import random

class UICememew:

    def __init__(self, root):
        self.root = root
        self.root.title('Translasi')
        self.root.geometry('400x200+0+0')

        frame1 =Frame(self.root)
        frame1.grid()

        frame2 =Frame(frame1)
        frame2.grid(row=0,column=0)

        frame3 =Frame(frame1)
        frame3.grid(row=1,column=0)

        frame4 =Frame(frame1)
        frame4.grid(row=2,column=1)

        bars_Num = IntVar()
        first_Num = IntVar()
        second_Num = IntVar()
        third_Num = IntVar()
        fourth_Num = IntVar()
        five_Num = IntVar()
        sixth_Num = IntVar()
        seven_Num = IntVar()
        eight_Num = IntVar()
        nine_Num = IntVar()
        ten_Num = IntVar()

        var_list = [first_Num, second_Num, third_Num, fourth_Num, five_Num, sixth_Num, seven_Num, eight_Num, nine_Num,
                    ten_Num]

        self.lblFirstNum = Label(frame2,text='Banyak bar yang ingin dibuat')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2,textvariable=bars_Num)
        self.txtFirstNum.grid(row=0, column=1)


        def buatInputText():
            for i in range(0, bars_Num.get()):
                self.lblSecondNum = Label(frame2, text='Value Bar ' + str(i + 1))
                self.lblSecondNum.grid(row=i+1, column=0)
                self.txtSecondNum = Entry(frame2, textvariable=var_list[i])
                self.txtSecondNum.grid(row=i+1, column=1)


        def jumlahkan():
            def update_bars(num, bars):
                i = random.randint(0, 3)
                dz[i] = 0.1
                bars[i] = ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color=random.choice(['r', 'g', 'b']))
                return bars

            fig = plt.figure()
            ax = p3.Axes3D(fig)
            xpos = []
            ypos = []
            zpos = []
            dx = []
            dy = []
            dz = [first_Num.get(), second_Num.get(), third_Num.get(), fourth_Num.get(), five_Num.get(), sixth_Num.get(), seven_Num.get(), eight_Num.get(), nine_Num.get(), ten_Num.get()]
            increment = 2
            for i in range(0, bars_Num.get()):
                if i == 0:
                    xpos.append(increment)
                elif i % 2 != 0:
                    xpos.append(xpos[i-1])
                else:
                    xpos.append(xpos[i-1]+2)

            for i in range(0, bars_Num.get()):
                if i % 2 != 0:
                    ypos.append(2)
                else:
                    ypos.append(4)

            for i in range(0, bars_Num.get()):
                zpos.append(0)
                dx.append(1)
                dy.append(1)

            # add bars
            bars = []
            for i in range(bars_Num.get()):
                if 0 <= dz[i] <= 5:
                    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='r'))
                elif 5 <= dz[i] <= 7:
                    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='b'))
                elif 7 <= dz[i] <= 10:
                    bars.append(ax.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i], color='g'))
            ax.set_title('Matrix Penilaian Siswa')

            plt.show()

        self.btnTranslation = Button(frame3,text='Jalankan!',command=jumlahkan).grid(row=3,column=0)
        self.btnCreateInput = Button(frame3,text='buat!',command=buatInputText).grid(row=0,column=2)
        self.btnKeluar= Button(frame3,text='Keluar',command=root.destroy).grid(row=3,column=2)

if __name__ == '__main__':
    root = Tk()
    application = UICememew(root)
    root.mainloop()
