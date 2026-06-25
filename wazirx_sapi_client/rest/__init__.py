import sys

if sys.version_info < (3, 7):
    raise RuntimeError("Python >= 3.7 required")

from wazirx_sapi_client.rest.client import Client
from wazirx_sapi_client.rest.exceptions import WazirxAPIError
