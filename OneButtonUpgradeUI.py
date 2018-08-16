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
        self.master = master
        self.init_window()
        self._setup_widgets()
        self._build_tree()
       
        
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
        self.tree = ttk.Treeview(columns=Insp_header, show="headings")
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
        for col in Insp_header:
            self.tree.heading(col, text=col.title())
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        
        for item in data_list:
            self.tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(Insp_header[ix],width=None)<col_w:
                    self.tree.column(Insp_header[ix], width=col_w)
        
Insp_header = ['Component', 'Disk Version']

tree = ET.ElementTree(file=r'C:\Users\Sgavari\Desktop\one Button upgrade\WINInstaller\Data\ReleaseInfo.xml')
root = tree.getroot() 
        
Inspector_list1=[]
Inspector_list2=[]
        
for node in tree.findall('.//Name'):
            Inspector_list1.append(node.text)
            
for node in tree.findall('.//Version'):
            Inspector_list2.append(node.text)
            
data = dict(zip(Inspector_list1, Inspector_list2))

data_list =[(Inspector_list1,Inspector_list2) for (Inspector_list1,Inspector_list2) in data.items()]


root = Tk()
root.state('zoomed')
app = Window(root)

root.mainloop()  