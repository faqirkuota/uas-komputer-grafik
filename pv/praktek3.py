print('====================Praktikum#2====================')
print('====Mengambil Data dan Menampilkan Data (Part2)====')
from tkinter import *
import tkinter.messagebox

class DataInOut:

    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
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

        self.lblFirstNum = Label(frame2,text='Masukan Angka Pertama')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2,textvariable=first_Num)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2,text='Masukan Angka Kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2,textvariable=second_Num)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2,text='Hasilnya..')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2,textvariable=hasil_penjumlahan)
        self.txtHasil.grid(row=2, column=1)

        def jumlahkan():
            pertama=float(first_Num.get())
            kedua=float(second_Num.get())
            hasil = pertama+kedua
            hasil_penjumlahan.set(hasil)

        self.btnJumlahkan = Button(frame3,text='Jumlahkan!',command=jumlahkan).grid(row=2,column=0)
        self.btnReset= Button(frame3,text='Reset').grid(row=2,column=1)
        self.btnKeluar= Button(frame3,text='Keluar',command=root.destroy).grid(row=2,column=2)

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
