import sys
from holistics_dbt.aml_gen import AmlGen
from holistics_dbt.dbt import Dbt

dbt = Dbt(
  manifest_path='tests/manifest.json',
  catalog_path='tests/catalog.json'
)

aml_gen = AmlGen(dbt_artifact=dbt)

table_models = aml_gen.gen_table_models()

for table_model in table_models:
  print(table_model.to_s())