# The QueryBuilder class is a Python class that provides methods for building and executing SQL
# queries on a database table.
class QueryBuilder:

    """
    The function initializes an object with database and table information, and sets default values
    for select columns, query, and conditions.
    
    :param db: The "db" parameter is used to specify the database connection or database object that
    will be used for executing queries. It could be an instance of a database connection class or an
    object that represents a connection to a specific database
    :param table_name: The `table_name` parameter is a string that represents the name of the table
    in the database that you want to interact with
    """
    def __init__(self, db, table_name) -> None:
        
        self.db = db
        self.table_name = table_name
        self.select_columns = "*"
        self.query = None
        self.conditions = []
    
    """
    The function executes a query on a database and returns the result.
    :param params: The `params` parameter is used to pass any parameters or values that need to be
    included in the query. These parameters can be used to dynamically generate the query or to
    provide values for placeholders in the query
    :param many: The "many" parameter is a boolean value that determines whether the query should
    return multiple rows or just a single row. If set to True, the query will return multiple rows
    as a list of tuples. If set to False, the query will return a single row as a tuple, defaults to
    False (optional)
    :return: The result of executing the query is being returned.
    """
    def _execute_query(self, params=None, many=False):
        result = self.db.execute_query(self.query, params, many)
        return result
    
    """
    The function "select" takes in a variable number of column names as arguments and returns a
    string of the selected columns separated by commas.
    :return: The method is returning the instance of the class itself.
    """
    def select (self, *columns):
        self.select_columns = ', '.join(columns)
        return self

    """
    The function retrieves data from a database table and returns it as a dictionary.
    :return: The code is returning a dictionary containing the result of the executed query. If the
    result is not None, it will be converted into a dictionary and returned. If the result is None,
    None will be returned.
    """
    def get(self):
        self.query = f"SELECT {self.select_columns} FROM {str(self.table_name)};"
        result = self._execute_query()
        return result if result is not None else None
    
    """
    The function `insert` checks the data format and calls the appropriate method for inserting
    either a single item or multiple items into a database.
    
    :param data: The `data` parameter is the data that you want to insert into the database. It can
    be either a single dictionary or a list of dictionaries
    :return: The method `insert` returns the result of either `_insert_many` or `_insert_single`
    depending on the type of `data` being passed in.
    """
    def insert(self, data):
        if isinstance(data, list):
            self.many = True
            return self._insert_many(data)
        elif isinstance(data, dict):
            self.many = False
            return self._insert_single(data)
        else:
            print("Invalid data format for insertion.")
            return None

    """
    The function inserts a single row of data into a database table.
    
    :param data: The `data` parameter is a dictionary that contains the column names as keys and the
    corresponding values that you want to insert into the table
    :return: The method is returning the result of executing the query with the provided values.
    """
    def _insert_single(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        self.query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        return self._execute_query(values)
    

    """
    The function inserts multiple rows of data into a table in a database.
    
    :param data_list: A list of dictionaries, where each dictionary represents a row of data to be
    inserted into the table. Each dictionary should have keys that correspond to the column names in
    the table, and the values should be the data to be inserted into those columns
    :return: the result of the `_execute_query` method with the `values` parameter set to the list
    of tuples created from the `data_list` argument. The `many` parameter is set to `True`,
    indicating that multiple rows will be inserted.
    """
    def _insert_many(self, data_list):
        if len(data_list) == 0:
            return None

        columns = ', '.join(data_list[0].keys())
        placeholders = ', '.join(['%s'] * len(data_list[0]))
        values = [tuple(data.values()) for data in data_list]
        self.query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        return self._execute_query(values, many=True)