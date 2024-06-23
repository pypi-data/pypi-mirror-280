import duckdb
import pandas as pd

class DuckDB:
    def __init__(self):
        # we have option of a in-memory db or a file-
        self.con = duckdb.connect(database=":memory:")

    def create_table(self, expr):
        self.con.execute(expr)

    def add_row(self, row):
        self.con.execute(row)

    def query(self, query_str):
        result = self.con.execute(query_str)
        return result

    def query_to_pd(self, query_str):
        df = self.con.execute(query_str).df()
        return df

    def __exit__(self):
        # we need to safely close the connection
        self.con.close()
