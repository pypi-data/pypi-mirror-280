import pymysql
from .exporter import Exporter
from ..utils.read_yaml import get_data


class DBExporter(Exporter):
    def __init__(self, table_name, module_name):
        self.table_name = table_name
        self.module_name = module_name

    def export(self, data, filename=None):
        config = get_data(module=self.module_name)
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        # Assumes data is a list of dictionaries
        if isinstance(data, dict):
            data = [data]
        for entry in data:
            keys = ", ".join(entry.keys())
            values = ", ".join(['%s'] * len(entry))
            sql = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})"
            cursor.execute(sql, tuple(entry.values()))
        conn.commit()
        cursor.close()
        conn.close()
