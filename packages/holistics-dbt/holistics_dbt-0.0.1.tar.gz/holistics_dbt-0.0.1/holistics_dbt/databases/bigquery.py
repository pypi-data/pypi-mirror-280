from holistics_dbt.databases.base_database import BaseDatabase

class BigQuery(BaseDatabase):
  def quote(self) -> str:
    return '`'
  
  def db_type_to_aml_type(self, db_type: str) -> str:
      if db_type == 'INT64' or db_type == 'FLOAT64':
        return 'number'
      elif db_type == 'BOOL':
        return 'truefalse'
      elif db_type == 'STRING':
        return 'text'
      elif db_type == 'DATE':
        return 'date'
      elif db_type == 'DATETIME':
        return 'datetime'
      else:
        return 'text'