#!/usr/bin/env python3
import os
import sys

profiles_content = """climabr:
  target: prod
  outputs:
    prod:
      type: athena
      database: awsdatacatalog
      region_name: us-east-1
      schema: landing
      s3_staging_dir: s3://proj-clima-dbt-hp/dbt/metadados/
      s3_data_dir: s3://proj-clima-dbt-hp/dbt/table/
      threads: 4
"""

dbt_dir = os.path.expanduser("~/.dbt")
profiles_file = os.path.join(dbt_dir, "profiles.yml")

try:
    os.makedirs(dbt_dir, exist_ok=True)
    with open(profiles_file, "w") as f:
        f.write(profiles_content)
    print(f"Success: profiles.yml created at {profiles_file}")
    sys.exit(0)
except Exception as e:
    print(f"Error: Failed to create profiles.yml - {str(e)}")
    sys.exit(1)
