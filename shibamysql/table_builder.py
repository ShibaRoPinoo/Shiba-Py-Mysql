
from shibamysql.missing_data_error import MissingDataError

class TableBuilder:
    def __init__(self, database, table_name) -> None:
        self.db = database
        self.table_name = table_name
        self.columns = []

    def increments(self, column_name='id', primary_key=False):
        if not column_name:
            raise MissingDataError("El nombre de la columna no puede estar vacío.")
        
        self.columns.append(
            f"{column_name} INT AUTO_INCREMENT {'' if not primary_key else 'PRIMARY KEY'}"
        )
        return self

    def primary(self):
        if not self.columns:
            raise MissingDataError("No se ha agregado ninguna columna.")
        
        current_column = self.columns[-1]
        if 'PRIMARY KEY' not in current_column:
            self.columns[-1] += " PRIMARY KEY"
        return self

    def unique(self):
        if not self.columns:
            raise MissingDataError("No se ha agregado ninguna columna.")
        
        self.columns[-1] += " UNIQUE"

    def foreign(self, foreign_name=None, table_name=None, column_name=None):
        if not self.columns:
            raise MissingDataError("No se ha agregado ninguna columna.")
        if not foreign_name or not table_name or not column_name:
            raise MissingDataError("Falta uno o más parámetros requeridos para la restricción FOREIGN KEY.")

        current_column = self.columns[-1]
        current_column_name = current_column.split()[0]  # Obtener la posición de la columna
        self.columns[-1] += f", CONSTRAINT {foreign_name} FOREIGN KEY ({current_column_name}) REFERENCES {table_name}({column_name})"
        return self
    
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

    def char(self, column_name, length=1):
        self.columns.append(f"{column_name} CHAR({length})")
        return self

    def date(self, column_name):
        self.columns.append(f"{column_name} DATE")
        return self

    def datetime(self, column_name):
        self.columns.append(f"{column_name} DATETIME")
        return self

    def time(self, column_name):
        self.columns.append(f"{column_name} TIME")
        return self

    def timestamp(self, column_name):
        self.columns.append(f"{column_name} TIMESTAMP")
        return self

    def decimal(self, column_name, precision=10, scale=2):
        self.columns.append(f"{column_name} DECIMAL({precision}, {scale})")
        return self

    def floats(self, column_name, precision=10, scale=2):
        self.columns.append(f"{column_name} FLOAT({precision}, {scale})")
        return self

    def boolean(self, column_name):
        self.columns.append(f"{column_name} BOOLEAN")
        return self

    def binary(self, column_name, length=None):
        self.columns.append(f"{column_name} {'BLOB' if length is None else f'BLOB({length})'}")
        return self
    
    def enum(self, column_name, choices):
        choices_str = ', '.join(f"'{choice}'" for choice in choices)
        self.columns.append(f"{column_name} ENUM({choices_str})")
        return self
    
    """ NULL / NOT NULL """

    def nullable(self):
        self.columns[-1] += " NULL"
        return self

    def not_nullable(self):
        self.columns[-1] += " NOT NULL"
        return self

    def build(self):
        if not self.columns:
            raise MissingDataError("No se ha agregado ninguna columna.")
        
        query = f"CREATE TABLE IF NOT EXISTS {str(self.table_name)} ("
        query += ", ".join(self.columns)
        query += ");"
        print(query)
        result = self.db.execute_query(query)
        if result is not None:
            print(f"Table Created {self.table_name} Successfully")
        else:
            return False