# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:33:32 2022

@author: apmel
"""
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        #frame=Frame(self)
        self.eval('tk::PlaceWindow . center')
        #self.title('Centennial College')
        # Canvas(self, width=400, height=600).pack()
        # container = Frame(self)
        # conta
        # container.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.create_ui()
        #self.create_styles()
        #self.set_variables()
    
    
    def create_ui(self, root=None):
        if not root: root = self      
                                
        root = Tk()  # similar to a windows form
        root.title('Centennial College')  # title of the window
        
        #Creating a frame
        frame = ttk.Frame()         
        frame.grid()  # row=0, column=0
        
        frame['padding'] = (5, 10)  # padding
        frame['borderwidth'] = 10  # border
        frame['relief'] = 'sunken'  # style: panel or gropubox
        
        
        # #row 0
        
        #Creating a label
        lbl_title = ttk.Label(frame, text='ICET:').grid(column=0, row=0, sticky="NESW")
        
        
        #lbl_title = ttk.Label(frame, text='ICET Student Survey').grid(row=0, column=0, sticky=(W, E))
        # #lbl_feather = ttk.Label(frame)         #the parent of this widget
        
        # #image = PhotoImage(file='feather.png') #create a PhotoImage
        
        # #lbl_feather['image'] = image           #put the above image on label
        
        # lbl_feather.grid(                      #positionsing the label
        
        #   column=1,                            #column=1
        
        #   row=0,                               #row=0
        
        #   sticky=(W, E))                       #where to anchor in the cell
        
        
        # row 1
        #Creating another label
        lbl_full_name = ttk.Label(frame,text='Full name:').grid(column=0,row=1, sticky=(W, E)) 
        
        username = StringVar()  # variable that will be used to communicate
        
        #Creating an entry
        name = ttk.Entry(frame, textvariable=username).grid(column=1, row=1, sticky=(W))  
        
        # row 2
        ttk.Label(frame, text='Residency:').grid(column=0, row=2, sticky=(W, E))
        
        panel = ttk.Frame(frame)  # this will be the container for the widget below
        panel.grid(column=1, row=2, sticky=(W, E))
        panel['borderwidth'] = 3
        panel['relief'] = 'ridge'
        
        residency = StringVar()
        
        ttk.Radiobutton(panel, text='Domestic', variable=residency, value='dom').grid(column=0, row=0, sticky=(W))  # grid coordinate is for its immediate parent
        ttk.Radiobutton(panel, text='International', variable=residency, value='intl').grid(column=0, row=1, sticky=(W))
        
        # row 4
        ttk.Label(frame, text='Courses:').grid(column=0, row=4, sticky=(W, E))
        
        panel = ttk.Frame(frame)
        panel.grid(column=1, row=4, columnspan=4, sticky=(W, E))
        panel['borderwidth'] = 3
        panel['relief'] = 'ridge'
        
        comp100 = StringVar()
        comp213 = StringVar()
        comp120 = StringVar()
        ttk.Checkbutton(panel,text='Programming I',variable=comp100, onvalue='comp100').grid(column=0, row=0, sticky=(W))        
        ttk.Checkbutton(panel, text='Web Page Design', variable=comp213, onvalue='comp213').grid(column=0, row=1, sticky=(W))        
        ttk.Checkbutton(panel, text='Software Engineering Fundamentals',variable=comp120, onvalue='comp129').grid(column=0, row=2, sticky=(W))
        
        # row 5
        button = ttk.Button(frame, text='Reset')
        button.grid(column=0, row=5, sticky=(W, E))
        
        # ttk.Button(frame, text='Ok', command=read_form).grid(column=1, row=5, sticky=(W, E))      #the function that will be called
        
        
        ttk.Button(frame, text='Exit', command=root.quit).grid(column=2, row=5, sticky=(W, E))  # the delegate that will be called


    def read_form(*args):
        messagebox.showinfo(title='Form Information', message=f'Username: {username.get()} \nResidency: {residency.get()}\nCourses: {comp100.get()} {comp120.get()} {comp213.get()}\nProgram: {program.get()}')
        
        
        
    def set_variables(self):
        pass
        #self.entry_name.set('Adriano Melquiades')
        #self.radio_residency.set('Domestic')
        
        
    def create_styles(self):
        pass
        #style = Style()
        #style.theme_use('alt')
        #style.configure('.', padding=(20, 10, 10, 10))#, ipadding=(5, 5, 30, 40))
        
        
start = MyApp()
start.mainloop()