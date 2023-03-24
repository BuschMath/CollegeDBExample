import pyodbc

class sqlDB:
    def __init__(self, server, database):
        self.server = server
        self.database = database

    def connect(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=yes;')

    def query_table(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM " + table_name)
        rows = cursor.fetchall()
        return rows

    def add_data(self, table_name, values):
        cursor = self.conn.cursor()
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?' for _ in range(len(values))])
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        cursor.execute(query, list(values.values()))
        self.conn.commit()

    def get_table_columns(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?", (table_name,))
        columns = [column[0] for column in cursor.fetchall()]
        return columns

    def close(self):
        self.conn.close()

    # create a function to retrieve the list of tables from the database
    def get_table_names(self):
        
        cursor = self.conn.cursor()
        # execute a query to retrieve the table names
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
        table_names = [row[0] for row in cursor.fetchall()]
    
        # return the table names
        return table_names
    
