from enum import Enum
from dataclasses import dataclass, field

class DimensionType(Enum):
  TEXT = 'text'
  NUMBER = 'number'
  DATE = 'date'
  DATETIME = 'datetime'
  TRUEFALSE = 'truefalse'
  JSON = 'json'
  UNKNOWN = 'unknown'

class DefinitionType(Enum):
  SQL = 'sql'
  AML = 'aml'
  AQL = 'aql'

@dataclass
class DimensionDefinition:
  type: DefinitionType = None
  content: str = ''

  def to_s(self) -> str:
    return f'@{self.type} {{{{ {self.content} }}}};; '

@dataclass
class AmlDimension:
  label: str = ''
  name: str = ''
  hidden: bool = False
  description: str = ''
  type: DimensionType = None
  definition: DimensionDefinition = None
  format: str = None

  def to_s(self) -> str:
    str = f"""  dimension {self.name} {{
    type: '{self.type}'
    hidden: { 'true' if self.hidden else 'false'}
    definition: {self.definition.to_s()}"""

    if self.description:
      str += f"""
    description: '{self.description}'"""
    
    if self.label:
      str += f"""
    label: '{self.label}'"""
    
    if self.format:
      str += f"""
    format: '{self.format}'"""

    str += """
  }"""

    return str