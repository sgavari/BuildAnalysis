import requests
from tkinter import *

import tkinter.font as tkFont
import tkinter.ttk as ttk

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from PIL import Image, ImageTk

class Window(Frame):

    
    def __init__(self, master,*args, **kwargs):
         
        Frame.__init__(self, master,*args, **kwargs)
        
#        table = Frame(self)
#        table.pack(side="top", fill="both", expand=True, ipadx=2, ipady=2)
#        table.grid_rowconfigure(1, weight=1)
#        table.grid_columnconfigure(1, weight=1)
        self.master = master
        self.init_window()
        self._setup_widgets()
        self._build_tree()
        
#        tree = ET.ElementTree(file=r'C:\Users\Sgavari\Desktop\one Button upgrade\WINInstaller\Data\ReleaseInfo.xml')
#        root = tree.getroot() 
#        self.widgets = {}
#        row = 1
         
#        Label(table, text="Component", relief=RIDGE, font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="nsew")
#        Label(table, text="Disk Version", relief=RIDGE, font=("Helvetica", 10, "bold")).grid(row=1, column=1, sticky="nsew")
        
        
    def init_window(self):

        self.master.title("Wafer Inspector Upgrade")

        self.pack(fill=BOTH, expand=1)

        self.showImg()
        self.showText()

    def showImg(self):
        load = Image.open(r"C:\Users\Sgavari\Desktop\one Button upgrade\WINInstaller\Resources\ktwall81.png")
        load = load.resize((2500, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="New Software Version", font=("-weight bold",26))
        text.place(x=700,y=130)
        

    def client_exit(self):
        exit()
        
    def _setup_widgets(self):
        container = Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=car_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
    def _build_tree(self):
        for col in car_header:
            self.tree.heading(col, text=col.title())
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        
        for item in car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)
        
car_header = ['Component', 'Disk Version']
car_list =[('Wafer Inspector', '9.7.073'), ('KTCS (KT Component Suite)', '6.0.0.30802'), ('EAS (Embedded Analysis Software)', '9.7.0.14'), ('DBB (Design Services)', '9.7.073'), ('IMPACT', '4.5.0.22'), ('RDS (Recipe Distribution System)', '2.8.2.4')]


root = Tk()
root.state('zoomed')
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#
#root.geometry("%dx%d+0+0" % (w, h))

#root.geometry("1927x1200")

app = Window(root)

root.mainloop()  