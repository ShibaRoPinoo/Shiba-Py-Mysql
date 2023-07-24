from shibamysql.database import Database
from shibamysql.table_builder import TableBuilder
from shibamysql.query_builder import QueryBuilder

class ShibaConnection:

    def __init__(self, host, port, user, password) -> None:
        self.db = Database(host, port, user, password)
    
    def create_database(self, database):
        return self.db.create_database(database)
        
    def use_database(self, database):
        return self.db.selected_database(database)
    
    def create_table(self, table_name):
        return TableBuilder(self.db, table_name)
    
    def table(self, table_name):
        return QueryBuilder(self.db, table_name)    