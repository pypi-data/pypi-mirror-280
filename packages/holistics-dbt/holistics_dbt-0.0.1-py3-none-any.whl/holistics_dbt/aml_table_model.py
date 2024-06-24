from dataclasses import dataclass, field
from typing import List
from holistics_dbt.aml_dimension import AmlDimension

@dataclass
class AmlTableModel:
  type: str = 'table'
  name: str = ''
  label: str = ''
  description: str = ''
  data_source_name: str = ''
  owner: str = ''
  table_name: str = ''
  dimensions: List[AmlDimension] = field(default_factory=list)

  def to_s(self) -> str:
    str = f"""
Model {self.name} {{
  type: 'table'
  label: '{self.label}'
  description: '{self.description}'
  owner: '{self.owner}'
  data_source_name: '{self.data_source_name}'
  table_name: '{self.table_name}'
"""

    for dimension in self.dimensions:
      str += f"""\n{dimension.to_s()}\n"""
    
    str += '}'

    return str

