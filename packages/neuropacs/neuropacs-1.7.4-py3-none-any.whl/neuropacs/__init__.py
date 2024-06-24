# __init__.py
from .sdk import Neuropacs

PACKAGE_VERSION = "1.7.4"

def init(server_url, api_key):
    return Neuropacs(server_url=server_url, api_key=api_key)


