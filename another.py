# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:57:58 2022

@author: apmel
"""

from tkinter import *

class MyApp():
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root, bg='green', relief=SUNKEN) #        
                
        #self.frame['padding'] = (5, 10)  # padding
        #self.frame['borderwidth'] = 10  # border
        #self.frame['relief'] = 'sunken'  # style: panel or gropubox
        
        
        
        #row=0
        self.label_title = Label(self.frame, text='ICET Student Survey', bg='green', width=30, height=1, font='Arial 16')
        self.label_title.grid(row=0, column=0, sticky="NESW")
          

        #row=1             
        self.label_name = Label(self.frame, text='Full name: ', bg='green', width=60, height=1)
        self.label_name.grid(row=1, column=0, sticky=E, padx=25)
        
        self.name = StringVar()
        self.entry_name = Entry(self.frame, textvariable=self.name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=(W, E), pady=15)
        
        #row=2
        self.residency = StringVar()
        self.label_residency = Label(self.frame, text='Residency: ', bg='green', width=60, height=1)
        self.label_residency.grid(row=2, column=0, pady=5, sticky=(W, E))
        
        #self.panel = ttk.Frame(frame)  # this will be the container for the widget below
        #self.frame = Frame()
        self.panel = Frame(self.frame , bg='green')
        self.panel.grid(row=1, column=1, sticky=(W, E))
        self.panel.grid(column=1, row=2, sticky=(W, E))
        self.panel['borderwidth'] = 3
        #self.panel['relief'] = 'ridge'
                        
        self.residency = StringVar()
        
        self.radio_dom = Radiobutton(self.panel, text='Domestic', variable=self.residency, value='dom', bg='green')
        self.radio_dom.grid(column=0, row=0, sticky=(W))  # grid coordinate is for its immediate parent
        self.radio_intl = Radiobutton(self.panel, text='International', variable=self.residency, value='intl', bg='green')
        self.radio_intl.grid(column=0, row=1, sticky=(W))
                
        
        
        # # row 2
        # #ttk.Label(frame, text='Residency:').grid(column=0, row=2, sticky=(W, E))
        
        # panel = ttk.Frame(frame)  # this will be the container for the widget below
        # panel.grid(column=1, row=2, sticky=(W, E))
        # panel['borderwidth'] = 3
        # panel['relief'] = 'ridge'
        
        # #residency = StringVar()
        
        # ttk.Radiobutton(panel, text='Domestic', variable=residency, value='dom').grid(column=0, row=0, sticky=(W))  # grid coordinate is for its immediate parent
        # ttk.Radiobutton(panel, text='International', variable=residency, value='intl').grid(column=0, row=1, sticky=(W))
        
        
        
        
        
        
        
        
        
        self.frame.grid()
        
        self.root.mainloop()
        

start = MyApp()


#################### delete below
       # username = StringVar()  # variable that will be used to communicate
        
        #Creating an entry
        #name = ttk.Entry(frame, textvariable=username).grid(column=1, row=1, sticky=(W))  