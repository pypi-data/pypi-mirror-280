import json

class Dbt:
  def __init__(self, manifest_path: str, catalog_path: str) -> None:
    self.manifest = dict()
    self.catalogs = dict()

    with open(manifest_path, 'r') as f:
      manifest = json.load(f)
      self.manifest['metadata'] = manifest.get('metadata')
      self.manifest['nodes'] = manifest.get('nodes')

    with open(catalog_path, 'r') as f:
      catalogs = json.load(f)
      self.catalogs['metadata'] = catalogs.get('metadata')
      self.catalogs['nodes'] = catalogs.get('nodes')

  def manifest_nodes(self) -> dict:
    return self.manifest.get('nodes')
  
  def catalog_nodes(self) -> dict:
    return self.catalogs.get('nodes')

  def adapter_type(self) -> str:
    return self.manifest['metadata']['adapter_type']
