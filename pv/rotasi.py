try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

inputNamaFile = ''
inputDerajat = ''

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
        label = tk.Label(self, text="Hasil Gambar", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)
        button = tk.Button(self, text="Kembali ke laman awal",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()