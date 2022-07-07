# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:33:32 2022

@author: apmel
"""
from tkinter import *
from tkinter.ttk import *
#from tkinter import ttk
from tkinter import messagebox


class MyApp(Tk):
    
    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)
        self.create_ui()
        
    def create_ui(self, frame=None):
        if not frame: frame = self
        
        #row 0        
        #Creating a label
        lbl_title = Label(frame, text='ICET:').grid(column=0, row=0, sticky="NESW")
        
        #row 1        
        lbl_full_name = Label(frame,text='Full name:').grid(column=0,row=1, sticky=(W, E)) 
        self.user_name = StringVar()
        entry_name = Entry(frame, textvariable=self.user_name) 
        entry_name.grid(column=1, row=1, sticky=(W))
        
        #row 2
        Label(frame, text='Residency:').grid(column=0, row=2, sticky=(W, E))
        
        #Creating a panel for the radio buttons
        panel = Frame(frame) 
        panel.grid(column=1, row=2, sticky=(W, E))
        panel['borderwidth'] = 3
        panel['relief'] = 'ridge'
        
        self.residency = StringVar()

        radio_dom = Radiobutton(panel, text='Domestic', variable=self.residency, value='dom')
        radio_dom.grid(column=0, row=0, sticky=(W))  
        radio_intl = Radiobutton(panel, text='International', variable=self.residency, value='intl')
        radio_intl.grid(column=0, row=1, sticky=(W))


        #row 3
        Label(frame, text='Program').grid(row=3, column=0, sticky=(W))
        
        #Creating the combo box

        
        #Creating the variable
        self.program = StringVar()
        #Creating the combobox 
        combo_box = Combobox(frame,
                                 values=('Health', 'Science', 'Engineering', 'Math', 'Physics'), 
                                 textvariable=self.program, state='readonly')
        combo_box.grid(row=3, column=1)
        combo_box.current(0)
        

        
        #row 4
        Label(frame, text='Courses:').grid(row=4, column=0, sticky=(W, E))
        
        #Creating a panel for the checkbox below
        panel2 = Frame(frame) 
        panel2.grid(row=4, column=1,sticky=(W))
        panel['borderwidth'] = 3
        panel['relief'] = 'ridge'
        
        self.comp100 = StringVar()
        self.comp213 = StringVar()
        self.comp120 = StringVar()
        self.comp254 = StringVar()
        self.comp247 = StringVar()
        Checkbutton(panel2,text='Programming I',variable=self.comp100, onvalue='comp100').grid(row=5, column=1, sticky=(W)) 
        
        Checkbutton(panel2, text='Web Page Design', variable=self.comp213, onvalue='comp213').grid(row=6, column=1, sticky=(W))        
        Checkbutton(panel2, text='Software Engineering Fundamentals',variable=self.comp120, onvalue='comp129').grid(row=7, column=1, sticky=(W))
        Checkbutton(panel2, text='Data Structure and Algorithms',variable=self.comp254, onvalue='comp254').grid(row=8, column=1, sticky=(W))
        Checkbutton(panel2, text='Supervised learning',variable=self.comp247, onvalue='comp247').grid(row=9, column=1, sticky=(W))
        
        
        #Functions
        def reset():
            entry_name.delete(0, END)
            self.comp100.set(0)
            self.comp213.set(0)
            self.comp120.set(0)
            self.comp254.set(0)
            self.comp247.set(0)
            

        
        def read_form(*args):
            messagebox.showinfo(title='Form Information',
                                message=self.user_name.get() 
                                + '\n' + self.program.get()
                                + '\n' + self.residency.get() 
                                + '\n' + self.comp100.get() 
                                + '\n' + self.comp213.get() 
                                + '\n' + self.comp120.get() 
                                + '\n' + self.comp254.get() 
                                + '\n' + self.comp247.get() 
                                )
        
            #messagebox.showinfo(title='Form Information', message=f'Username: {self.username.get()} \nResidency: {residency.get()} \n Program: {program.get()} Courses: {comp100.get()} {comp120.get()} {comp213.get()}\nProgram: {program.get()}')
            #messagebox.showinfo(title='Information', message=f'')
                
        def quit():
            frame.destroy()
        
        # row 5  
        button = Button(frame, text='Reset', command=reset)
        button.grid(row=10, column=0, sticky=(W, E))
        
        
        Button(frame, text='Ok', command=read_form).grid(row=10, column=1, sticky=(W, E))      #the function that will be called        
        Button(frame, text='Exit', command=quit).grid(row=10, column=2, sticky=(W, E))  # the delegate that will be called
        


        
start = MyApp('Centennial College')
start.mainloop()
        