# The `TableBuilder` class is a Python class that helps in building SQL table creation queries by
# providing methods to add columns with different data types and constraints.
class TableBuilder:

    """
    The function initializes an object with a database, table name, and an empty list of columns.
    
    :param database: The `database` parameter is used to specify the name or connection object of
    the database that you want to work with. It can be a string representing the name of the
    database or an object representing a connection to the database
    :param table_name: The `table_name` parameter is a string that represents the name of the table
    in the database. It is used to specify which table the code will be interacting with
    """
    def __init__(self, database, table_name) -> None:
        self.db = database
        self.table_name = table_name
        self.columns = []

    """
    The function increments adds a new column to a table with an auto-incrementing primary key.
    
    :param column_name: The parameter `column_name` is a string that represents the name of the
    column that you want to add to your table. By default, it is set to 'id', defaults to id
    (optional)
    :return: The method is returning the instance of the class itself, allowing for method chaining.
    """
    def increments(self, column_name='id'):
        self.columns.append(f"f{column_name} INT AUTO_INCREMENT PRIMARY KEY")
        return self

    def unique(self):
        self.columns[-1] += " UNIQUE"

    """ TYPE  """
    def integer(self, column_name, length=None):
        self.columns.append(
            f"{column_name} {'INT' if length is None else f'INT({length})'}")
        return self

    def string(self, column_name, length=255):
        self.columns.append(f"{column_name} VARCHAR({length})")
        return self

    def text(self, column_name):
        self.columns.append(f"{column_name} TEXT")
        return self

    def date(self, column_name):
        self.columns.append(f"{column_name} DATE")
        return self

    def timestamp(self, column_name):
        self.columns.append(f"{column_name} TIMESTAMP")
        return self

    """ NULL / NOT NULL """

    def nullable(self):
        self.columns[-1] += " NULL"
        return self

    def not_nullable(self):
        self.columns[-1] += " NOT NULL"
        return self

    def build(self):
        query = f"CREATE TABLE IF NOT EXISTS {str(self.table_name)} ("
        query += ", ".join(self.columns)
        query += ");"
        print(query)
        result = self.db.execute_query(query)
        if result is not None:
            print(f"Table Created {self.table_name} Successfully")
        else:
            return False
