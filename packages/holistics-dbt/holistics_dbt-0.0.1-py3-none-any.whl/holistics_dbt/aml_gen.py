from holistics_dbt.dbt import Dbt
from holistics_dbt.aml_table_model import AmlTableModel
from holistics_dbt.aml_dimension import AmlDimension, DimensionDefinition
from typing import List
import re
# TODO: improve this
from holistics_dbt.databases import BigQuery, BaseDatabase

def database_for(dbname: str) -> BaseDatabase:
  if dbname == 'bigquery':
    return BigQuery()
  else:
    raise ValueError(f'Unsupported database: {dbname}')

def fqname_for(schema: str, table: str, dbname: str) -> str:
  # TODO: empty schema?
  quote = database_for(dbname).quote()
  return f'{quote}{schema}{quote}.{quote}{table}{quote}'

pattern = re.compile(r'(?<!^)(?=[A-Z])')
def snake_case(s: str) -> str:
  lower_case = pattern.sub('_', s).lower()
  removed_dot = lower_case.replace('.', '_')
  return removed_dot

class AmlGen:
  def __init__(
      self,
      dbt_artifact: Dbt,
    ) -> None:
    self.dbt_artifact = dbt_artifact

  def gen_table_models(self) -> List[AmlTableModel]:
    nodes = self.dbt_artifact.catalog_nodes()
    table_models = []

    dbtype = self.dbt_artifact.adapter_type()

    for key in nodes:
      node = nodes[key]
      table_models.append(self.to_table_model(dbtype, node))

    return table_models
    
  def to_table_model(self, dbtype: str, catalog_node: dict) -> AmlTableModel:
    metadata = catalog_node['metadata']
    fqname = fqname_for(metadata['schema'], metadata['name'], dbtype)
    model_name = snake_case(catalog_node['unique_id'])

    database = database_for(dbtype)

    dimensions = map(
      lambda kv: self.to_dimension(kv[1], database),
      catalog_node['columns'].items()
    )

    return AmlTableModel(
      name=model_name,
      data_source_name=metadata['database'],
      table_name=fqname,
      description='', # TODO: search in manifest
      dimensions=dimensions,
      owner='',
    )
  
  def to_dimension(self, column: dict, database: BaseDatabase) -> AmlDimension:
    definition = DimensionDefinition(
      type='sql',
      content=f'#SOURCE.{column["name"]}'
    )

    return AmlDimension(
      label=column['name'],
      name=snake_case(column['name']),
      hidden=False, # TODO: sync with current existing file?
      description=column['comment'], # TODO: escape quotes
      definition=definition,
      format=None, # TODO: sync with current existing file?
      type=database.db_type_to_aml_type(column['type']),
    )
