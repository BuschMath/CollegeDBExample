import random
import tkinter as tk
from tkinter import ttk
from sqlDB import sqlDB
import nameGenerator
import dateGenerator
import ssnGenerator

class GUI(tk.Frame):
    def __init__(self, server, database, master=None,):
        # create the main window
        super().__init__(master)
        self.master = master
        self.pack()
        self.k = 0

        # create an instance of the sqlDB class
        self.db = sqlDB(server, database)
        self.db.connect()

        self.createMenu()
        self.createQueryFrame()
        self.createInsertDataFrame()
        self.createRandomStudentsFrame()

        self.show_menu()

    def onClick(self):
        # call a method from the sqlDB class
        data = self.db.query_table(self.selected_table.get())
        columnNames = self.db.get_table_columns(self.selected_table.get())
        self.queryFrame.columnResult.configure(text=columnNames)
        self.queryFrame.queryResult.configure(text=data)

    def onClickData(self):
        # call a method from the sqlDB class
        data = self.db.query_table(self.selected_table.get())
        columnNames = self.db.get_table_columns(self.selected_table.get())
        self.insertDataFrame.columnResult.configure(text=columnNames)
        self.insertDataFrame.queryResult.configure(text=data)

    def run(self):
        self.mainloop()

    def __del__(self):
        self.db.close()

    def createMenu(self):
        # Create main menu frame
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(side="top")

        # Create labels
        self.menu_frame.basicLabel = tk.Label(self.menu_frame, text="Basic SQL Queries").grid(row=0, column=0)

        # Create main menu buttons
        self.menu_frame.queryButton = tk.Button(self.menu_frame, text="Query", 
                                     command=self.open_queryFrame)
        self.menu_frame.queryButton.grid(row=1, column=0)
        self.menu_frame.insertDataButton = tk.Button(self.menu_frame, text="Insert Data",
                                          command=self.open_insertDataFrame)
        self.menu_frame.insertDataButton.grid(row=2, column=0)

    def show_menu(self):
        # show the main menu frame and hide the other frames
        self.menu_frame.pack(side="top")
        self.queryFrame.pack_forget()
        self.insertDataFrame.pack_forget()

    def createQueryFrame(self):
        # create the frame 1 widget
        self.queryFrame = tk.Frame(self.master)
        # create a label
        self.queryFrame.label = tk.Label(self.queryFrame, text="Query Table:")
        self.queryFrame.label.pack()

        # create a button
        self.queryFrame.button = tk.Button(self.queryFrame, text="Execute:", command=self.onClick)

        self.queryFrame.columnResult = tk.Label(self.queryFrame, text="Column names will be here.")
        self.queryFrame.queryResult = tk.Label(self.queryFrame, text="Results will be displayed here.")

        # create a variable to store the selected table name
        self.selected_table = tk.StringVar(self.queryFrame)

        # create the list of table names by calling the get_table_names() function
        table_names = self.db.get_table_names()
        # set the initial value of the variable
        self.selected_table.set(table_names[0])
        # create the OptionMenu widget
        option_menu = tk.OptionMenu(self.queryFrame, self.selected_table, *table_names)

        # pack the OptionMenu widget onto the window
        option_menu.pack()
        self.queryFrame.button.pack()
        self.queryFrame.columnResult.pack()
        self.queryFrame.queryResult.pack()

        tk.Button(self.queryFrame, text="Go Back to Menu", command=self.show_menu).pack()
       
    def createInsertDataFrame(self):
        # create the frame 1 widget
        self.insertDataFrame = tk.Frame(self.master)
        self.insertDataFrame.columnNames = self.db.get_table_columns(self.selected_table.get())

        table_names = self.db.get_table_names()
        option_menu = tk.OptionMenu(self.insertDataFrame, self.selected_table, *table_names)
        option_menu.grid(row=0, column=0)

        # create a button
        tk.Button(self.insertDataFrame, text="Get Attributes:", command=self.onClickData).grid(row=0, column=1)
        
        self.i=0
        self.insertDataFrame.entryList = []
        for att in self.insertDataFrame.columnNames:
            tk.Label(self.insertDataFrame, text=att).grid(row=1, column=self.i)
            entry = tk.Entry(self.insertDataFrame)
            entry.grid(row=2, column=self.i)
            self.insertDataFrame.entryList.append(entry)
            self.i = self.i + 1

        tk.Button(self.insertDataFrame, text="Go Back to Menu", command=self.show_menu).grid(row=3, column=0)
        tk.Button(self.insertDataFrame, text="Execute Data Entry:", command=self.onClickDataExe).grid(row=3, column=1)

        #########################################
        # query info
        # create a label
        self.insertDataFrame.label = tk.Label(self.insertDataFrame, text="Query Table:")
        ttk.Separator(self.insertDataFrame, orient="horizontal").grid(row=4, column=0)
        self.insertDataFrame.label.grid(row=5, column=0)

        # create a button
        self.insertDataFrame.button = tk.Button(self.insertDataFrame, text="Execute:", command=self.onClickData)

        self.insertDataFrame.columnResult = tk.Label(self.insertDataFrame, text="Column names will be here.")
        self.insertDataFrame.queryResult = tk.Label(self.insertDataFrame, text="Results will be displayed here.")

        # create a variable to store the selected table name
        self.insertDataFrame.selected_table = tk.StringVar(self.insertDataFrame)

        # create the list of table names by calling the get_table_names() function
        table_names = self.db.get_table_names()
        # set the initial value of the variable
        self.insertDataFrame.selected_table.set(table_names[0])
        # create the OptionMenu widget
        option_menu = tk.OptionMenu(self.insertDataFrame, self.insertDataFrame.selected_table, *table_names)

        # pack the OptionMenu widget onto the window
        option_menu.grid(row=6, column=0)
        self.insertDataFrame.button.grid(row=7, column=0)
        self.insertDataFrame.columnResult.grid(row=8, column=0)
        self.insertDataFrame.queryResult.grid(row=9, column=0)

    def open_queryFrame(self):
        # show queryFrame and hide the main menu and other frames
        self.menu_frame.pack_forget()
        self.queryFrame.pack(side="top")

    def open_insertDataFrame(self):
        self.menu_frame.pack_forget()
        self.insertDataFrame.pack(side="top")

    def onClickData(self):
        # call a method from the sqlDB class
        self.insertDataFrame.columnNames = self.db.get_table_columns(self.selected_table.get())
        
        self.insertDataFrame.pack_forget()
        self.createInsertDataFrame()
        self.open_insertDataFrame()

    def onClickDataExe(self):
        data = {}
        j = 0
        for names in self.insertDataFrame.columnNames:
            if self.insertDataFrame.entryList[j].get() != "":
                data[names] = self.insertDataFrame.entryList[j].get()
            j = j + 1

        self.db.add_data(self.selected_table.get(), data)

        tk.Label(self.insertDataFrame, text=f"If no errors, your data entry was successful {self.k}").grid(row=4, column=0)
        self.k = self.k + 1
    
    def createRandomStudentsFrame(self):
        self.randomStudentsFrame = tk.Frame(self.master)
        self.randomStudentsFrame.labelHowManyStudents = tk.Label(self.randomStudentsFrame, 
                                                                 text="Please enter how many random students you would like to create:").grid(row=0, column=0)
        self.randomStudentsFrame.entryInputNumberStudents = tk.Entry(self.randomStudentsFrame).grid(row=1, column=0)
        self.randomStudentsFrame.buttonExeCreateRandomStudents = tk.Button(self.randomStudentsFrame, 
                                                                           command=self.onClickRandomStudentCreation, text="Execute:").grid(row=2, column=0)
        tk.Button(self.insertDataFrame, text="Go Back to Menu", command=self.show_menu).grid(row=3, column=0)
        
    def onClickRandomStudentCreation(self):
        self.randomPersonCreation()
        
        
    def randomPersonCreation(self):
        data = {'fName': nameGenerator.generateRandomName(), 'lName': nameGenerator.generateRandomName(), 
                'DoB': dateGenerator.generateRandomDate(), 'genderID': random.randint(26000, 26001), 
                'ssn': ssnGenerator.generateRandomSSN()}
        self.db.add_data('person', data)