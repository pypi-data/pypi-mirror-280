from abc import ABC, abstractmethod

class BaseDatabase(ABC):
  @abstractmethod
  def quote(self) -> str:
    pass
  
  @abstractmethod
  def db_type_to_aml_type(self, db_type: str) -> str:
    pass

