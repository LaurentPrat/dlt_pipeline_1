# readvolskd_1.py
# - read a file from a volume

from databricks.sdk import WorkspaceClient

# Initialize the Databricks workspace client
client = WorkspaceClient()

# Specify the volume path in Unity Catalog
volume_path = "/Volumes/your_volume_name"

# List files in the specified volume
files = client.files.list(volume_path)

# Print the file names
for file in files:
    print(file.name)