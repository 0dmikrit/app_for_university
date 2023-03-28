from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('My app')
        self.geometry('400x400')
        self.resizable(width=False, height=False)
        self.put_frames()

    def put_frames(self):
        self.frame_main = MainWindow(self)
        self.frame_main.place(relwidth=1, relheight=1)


class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg='grey')
        self.__x = StringVar()
        self.__y = StringVar()
        self.entry_res = Label(self)
        self.entry_res.place(relx=0.55, rely=0.1,relwidth=0.45)
        self.put_widgets()


    def press(self):
        res = int(self.__x.get()) + int(self.__y.get()) 
        self.entry_res.config(text=f'{res}')


    def put_widgets(self):
      self.text_x = Label(self, text='Первое число').place(relx=0.04, rely=0,relwidth=0.5)
      self.entry_x = Entry(self, textvariable=self.__x).place(relx=0.55, rely=0,relwidth=0.45)
      self.text_y = Label(self, text='Второе число').place(relx=0.04, rely=0.05,relwidth=0.5)
      self.entry_y = Entry(self, textvariable=self.__y).place(relx=0.55, rely=0.05,relwidth=0.45)
      self.text_res = Label(self, text='Результат').place(relx=0.04, rely=0.1,relwidth=0.5)
      self.but = Button(self, text='Вычислить', command=self.press).place(relx=0.3, rely=0.15,relwidth=0.4)
    
       
if __name__ == '__main__':
    app = App()
    app.mainloop()