from shibamysql.missing_data_error import MissingDataError


class QueryBuilder:
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name
        self.query = None
        self.where_conditions = []
        self.selected_columns = []
        self.join_clauses = []

    def _execute_query(self, params=None, many=False):
        result = self.db.execute_query(self.query, params, many)
        return result

    def join(self, table_name, column1, operator, column2):
        if not table_name or not column1 or not operator or not column2:
            raise MissingDataError(
                "Falta uno o más parámetros requeridos para la operación JOIN.")

        join_clause = f"JOIN {table_name} ON ({column1} {operator} {column2})"
        self.join_clauses.append(join_clause)
        return self

    def left_join(self, table_name, column1, operator, column2):
        if not table_name or not column1 or not operator or not column2:
            raise MissingDataError(
                "Falta uno o más parámetros requeridos para la operación LEFT JOIN.")

        join_clause = f"LEFT JOIN {table_name} ON {column1} {operator} {column2}"
        self.join_clauses.append(join_clause)
        return self

    def right_join(self, table_name, column1, operator, column2):
        if not table_name or not column1 or not operator or not column2:
            raise MissingDataError(
                "Falta uno o más parámetros requeridos para la operación RIGHT JOIN.")

        join_clause = f"RIGHT JOIN {table_name} ON {column1} {operator} {column2}"
        self.join_clauses.append(join_clause)
        return self

    def cross_join(self, table_name):
        if not table_name:
            raise MissingDataError(
                "Falta uno o más parámetros requeridos para la operación CROSS JOIN.")

        join_clause = f"CROSS JOIN {table_name}"
        self.join_clauses.append(join_clause)
        return self

    def inner_join(self, table_name, column1, operator, column2):
        if not table_name or not column1 or not operator or not column2:
            raise MissingDataError(
                "Falta uno o más parámetros requeridos para la operación INNER JOIN.")

        join_clause = f"INNER JOIN {table_name} ON {column1} {operator} {column2}"
        self.join_clauses.append(join_clause)
        return self

    def select(self, *columns):
        if not columns:
            raise MissingDataError(
                "Debe especificar al menos una columna para la operación SELECT.")

        self.selected_columns.extend(columns)
        return self

    def where(self, *args):
        if isinstance(args, list):
            return self._whereArray(args)

        if len(args) == 2:
            column, value = args
            operator = '='
        elif len(args) == 3:
            column, operator, value = args
        else:
            raise ValueError("Invalid number of arguments for 'where' method")

        self.where_conditions.append(f"{column} {operator} '{value}'")

        return self

    def _whereArray(self, array, boolean='AND'):
        for condition in array:
            if isinstance(condition, list):
                if len(condition) == 2:
                    column, value = condition
                    operator = '='
                elif len(condition) == 3:
                    column, operator, value = condition
                else:
                    raise MissingDataError("Invalid number of arguments for 'where' method")

            if isinstance(value, str):
                value = f"{value}"
            
            a =  self.where(column, operator, value)
        return self

    def get(self):
        select_clause = "*"
        if self.selected_columns:
            select_clause = ", ".join(self.selected_columns)

        join_clause = " ".join(self.join_clauses)

        where = ""
        if self.where_conditions:
            where = "WHERE "
            where_conditions = " AND ".join(self.where_conditions)
            where += where_conditions

            print (where)

        query = f"SELECT {select_clause} FROM {self.table_name} {join_clause} {where}"
        result = self.db.execute_query(query)

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
