
from tkinter import *
import tkinter.messagebox
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3

class Translation(tk.Tk):

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
        for F in (Gambar, Rotasi):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Gambar")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Gambar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.root.title('Gambar')
        self.root.geometry('400x200+0+0')

        frame1 =Frame(self.root)
        frame1.grid()

        frame2 =Frame(frame1)
        frame2.grid(row=0,column=0)

        frame3 =Frame(frame1)
        frame3.grid(row=1,column=0)

        frame4 =Frame(frame1)
        frame4.grid(row=2,column=1)

        self.lblFirstNum = Label(frame2,text='Pilih Gambar')
        self.lblFirstNum.grid(row=0, column=0)

        def jumlahkan():
            pertama=float(first_Num.get())
            kedua=float(second_Num.get())
            hasil = pertama+kedua
            hasil_penjumlahan.set(hasil)

        self.btnRotasi30 = Button(frame3,text='Alien', command = lambda: controller.show_frame("PageOne")).grid(row=2,column=0)
        self.btnRotasi40 = Button(frame3, text='Kupu-Kupu', command = jumlahkan).grid(row=2, column=1)
        self.btnRotasi50 = Button(frame3, text='Hellboy', command = jumlahkan).grid(row=2, column=2)
        self.btnKeluar= Button(frame3,text='Keluar',command = root.destroy).grid(row=3,column=1)


class Rotasi(tk.Frame):

    def __init__(self, root):
        self.root = root
        self.root.title('Rotasi')
        self.root.geometry('400x200+0+0')

        frame1 =Frame(self.root)
        frame1.grid()

        frame2 =Frame(frame1)
        frame2.grid(row=0,column=0)

        frame3 =Frame(frame1)
        frame3.grid(row=1,column=0)

        frame4 =Frame(frame1)
        frame4.grid(row=2,column=1)

        first_Num = StringVar()
        second_Num = StringVar()
        hasil_penjumlahan = StringVar()

        self.lblFirstNum = Label(frame2,text='Pilih Derajat Rotasi')
        self.lblFirstNum.grid(row=0, column=0)

        def jumlahkan():
            pertama=float(first_Num.get())
            kedua=float(second_Num.get())
            hasil = pertama+kedua
            hasil_penjumlahan.set(hasil)

        self.btnRotasi30 = Button(frame3,text='30º',command=jumlahkan).grid(row=2,column=0)
        self.btnRotasi40 = Button(frame3, text='40º', command=jumlahkan).grid(row=2, column=1)
        self.btnRotasi50 = Button(frame3, text='50º', command=jumlahkan).grid(row=2, column=2)
        self.btnKeluar= Button(frame3,text='Keluar',command=root.destroy).grid(row=3,column=1)


if __name__ == '__main__':
    root = Tk()
    application = Gambar(root)
    root.mainloop()
