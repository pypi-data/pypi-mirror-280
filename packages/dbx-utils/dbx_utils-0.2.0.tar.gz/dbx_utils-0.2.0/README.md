# dbx_utils

`dbx_utils` is a Python package for managing folders and permissions in Databricks workspaces.

## Installation

```bash
pip install dbx_utils
```
# Usage
## Creating a Folder
```python
from dbx_utils import create_databricks_folder

url = 'https://your-databricks-url'
token = 'your-databricks-token'
folder_path = '/example-folder'

folder_id = create_databricks_folder(url, token, folder_path)
print(f"Created folder ID: {folder_id}")
```
## Setting Folder Permissions
```python
from dbx_utils import set_folder_permissions

url = 'https://your-databricks-url'
token = 'your-databricks-token'
folder_id = 'your-folder-id'

set_folder_permissions(url, token, folder_id)
```
Getting a Folder ID
```python
from dbx_utils import get_databricks_folder_id

url = 'https://your-databricks-url'
token = 'your-databricks-token'
folder_path = '/example-folder'

folder_id = get_databricks_folder_id(url, token, folder_path)
print(f"Folder ID: {folder_id}")
```
### List of dependencies.
- requests
- databricks-api