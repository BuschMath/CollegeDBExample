import sqlDB
from sqlGUI import GUI
import tkinter as tk

#def printTable(tableName):
#    print('Table: ', tableName)
#    columns = college_db.get_table_columns(tableName)
#    print(columns)

#    rows = college_db.query_table(tableName)
#    for row in rows:
#        print(row)

# create an instance of the GUI class and run it
root = tk.Tk()
root.geometry("1200x800")
root.title("SQL DB GUI")
gui = GUI('MSI\SQLEXPRESS', 'college', master=root)
gui.run()

#college_db = sqlDB.sqlDB('MSI\SQLEXPRESS', 'college')
#college_db.connect()

#printTable('building')

# Add data to a table
#values = {'first_name': 'John', 'last_name': 'Doe', 'email': 'johndoe@example.com'}
#college_db.add_data('students', values)

#college_db.close()
