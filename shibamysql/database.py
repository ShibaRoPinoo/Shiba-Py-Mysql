import pymysql

class Database:

    """
    The above function is a constructor that initializes the host, port, user, and password
    attributes of an object, and establishes a connection to a database.
    
    :param host: The `host` parameter represents the hostname or IP address of the database server
    you want to connect to. It is used to specify the location of the database server
    :param port: The `port` parameter is used to specify the port number for the database
    connection. It is typically a number that corresponds to a specific service or protocol on the
    host machine. For example, the default port for MySQL is 3306, while the default port for
    PostgreSQL is 5432
    :param user: The "user" parameter in the above code represents the username used to authenticate
    the connection to a database server. It is typically used in combination with the "password"
    parameter to establish a secure connection
    :param password: The `password` parameter is used to store the password for the user to connect
    to the database. It is a string that represents the password
    """
    def __init__(self, host, port, user, password) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.database = None
        self.query = ""
        self.connect()
    
    """
    The function `connect` establishes a connection to a database using the provided host, port,
    user, and password.
    """
    def connect (self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            print (f"Error connecting to the database: {str(e)}")
    
    """
    The function creates a database with the given name, handling exceptions for existing databases
    and other errors.
    
    :param database: The `database` parameter is a string that represents the name of the database
    that you want to create
    :return: The method is returning the instance of the class itself (self) after creating the
    database.
    """
    def create_database(self, database):
        
        try:
            self.cursor.execute(f"CREATE DATABASE {database}")
            self.database = database
            return self
        except pymysql.err.ProgrammingError as e:
            if "database exists" in str(e):
                print(f"The database '{database}' already exists.")
            else:
                print(f"Error creating database: {str(e)}")
        except Exception as e:
            print(f"Error creating database: {str(e)}")

    """
    The function `selected_database` sets the current database to the specified database.
    
    :param database: The `database` parameter is the name of the database that you want to select
    and use
    :return: The method is returning the instance of the class itself (self) after setting the
    selected database.
    """
    def selected_database(self, database):
        try:
            self.database = self.cursor.execute(f"USE {database}")
            return self
        except Exception as e:
            print (f"Error using database {database}: {str(e)}")

    """
    The function executes a SQL query with optional parameters and returns the result.
    
    :param query: The query parameter is a string that represents the SQL query you want to execute.
    It can be any valid SQL statement, such as SELECT, INSERT, UPDATE, DELETE, etc
    :param params: The `params` parameter is used to pass values to the query as parameters. It is
    an optional parameter and can be used when the query contains placeholders for values that need
    to be dynamically provided
    :param many: The "many" parameter is a boolean flag that indicates whether the query should be
    executed multiple times with different sets of parameters. If set to True, the "params" argument
    should be a list of tuples, where each tuple contains the parameters for a single execution of
    the query. If set to False, defaults to False (optional)
    :return: the result of the query execution, which is stored in the variable "result".
    """
    def execute_query(self, query, params=None, many=False):
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                if many:
                    self.cursor.executemany(query, params)
                else:
                    self.cursor.execute(query, params)
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error Query: {str(e)}")
            self.connection.rollback()
            return None