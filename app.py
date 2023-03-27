from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('My app')
        self.put_frames()

    def put_frames(self):
        self.frame_add_form = AddForm(self).grid(row=0, column=0)
        self.frame_statistic = TextForm(self).grid(row=0, column=1)
        self.frame_list = TableFrame(self).grid(row=1, column=0, columnspan=2)


class AddForm(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.put_widgets()
        self.c = 0

  
    def successful(self):
        if self.c % 2 == 0:
            self.config(bg='red')
            self.c+=1
        else:
            self.config(bg='blue')
            self.c+=1
        print('Nice')


    def put_widgets(self):
        global item
        e1 = Label(self, text='Chose an item')
        #e2 = ttk.Combobox(self, values=self.items['names'])
        e3 = Label(self, text='What is you name?')
        e4 = Entry(self, text='Chose an item')
        e5 = Button(self, text='Press', command=self.successful)

        e1.grid(row=0, column=0)
        #e2.grid(row=0, column=1)
        e3.grid(row=1, column=0)
        e4.grid(row=1, column=1)
        e5.grid(row=2, column=0, columnspan=2)


class TextForm(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.put_widgets()

    def put_widgets(self):
        l1 = Label(self, text='Hi')
        l2 = Label(self, text='How are you?')
        l3 = Label(self, text='Nice day')
        l4 = Label(self, text='You see ara beautiful')
        l5 = Label(self, text='Goodluck')
        l6 = Label(self, text='Kiss')
        l7 = Label(self, text='Goodbye')

        l1.grid(column=0, row=0)
        l2.grid(column=1, row=0)
        l3.grid(column=0, row=1)
        l4.grid(column=1, row=1)
        l5.grid(column=0, row=2)
        l6.grid(column=1, row=2)
        l7.grid(column=0, row=3)


class TableFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.put_widgets()

    def put_widgets(self):
        heads = ['id', 'name_product', 'count', 'price', 'sum', 'id_user', 'name_user']
        lst = [
            (1, 'Milk', 10, 2, 20, 1, 'Max'),
            (2, 'Juice', 15, 3, 45, 2, 'Alex'),
            (3, 'Apple', 100, 0.1, 10, 1, 'Max'),
            (4, 'Orange', 70, 0.15, 10.5, 2, 'Alex'),
            (5, 'Carrot', 150, 0.07, 10.5, 3, 'Mike'),
            (6, 'Chocolate', 7, 1.5, 4.6, 1, 'Max'),
            (7, 'Beer', 30, 1, 30, 3, 'Mike')]

        table = ttk.Treeview(self)
        table['columns'] = heads


        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header,anchor='center')

        for row in lst:
            table.insert('', 'end', values=row)
        table.pack(expand=YES, fill=BOTH)


app = App()
app.mainloop()
