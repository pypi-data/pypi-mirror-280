import json
import os

from rich import print_json

__version__ = "0.17.1"
# Until DNS is fixed
API_HOST = os.environ.get("GIZA_API_HOST", "https://api.gizatech.xyz")

print_json(json.dumps({"API_HOST": API_HOST}))
