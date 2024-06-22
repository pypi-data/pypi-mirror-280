#     _   __     __        ___    ____  ____
#    / | / /__  / /_____  /   |  / __ \/  _/
#   /  |/ / _ \/ __/ __ \/ /| | / /_/ // /
#  / /|  /  __/ /_/ /_/ / ___ |/ ____// /
# /_/ |_/\___/\__/\____/_/  |_/_/   /___/

"""
NetoAPI Library
----------------------

A Python3 API Client for the Neto (Maropost) Ecommerce platform

Basic Get usage:

    >>> api = netoapi.NetoAPIClient(
    >>>     endpoint,
    >>>     username,
    >>>     apikey
    >>> )
    >>> payload = {
    >>>     "Filter": {
    >>>         "SKU": "LSD",
    >>>         "OutputSelector": [
    >>>             "Name",
    >>>             "RRP"
    >>>         ] 
    >>>     }
    >>> }
    >>> response = api.execute_api_call("GetItem", payload)
    >>> print(response)
    {
      'Item': [{'RRP': '150.00', 'InventoryID': '31673', 'Name': 'Luke Skywalker Doll', 'SKU': 'LSD'}],
      'CurrentTime': '2021-02-06 10:49:40',
      'Ack': 'Success'
    }
"""

import sys

if sys.version_info < (3, 7):
    raise Warning(
        f"NetoAPI supports Python3.7 or greater. You are using V{sys.version_info.major}.{sys.version_info.minor}"
    )

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

from netoapi.errors import DependencyNotFoundError, NetoAPIRequestError

try:
    import requests
except:
    raise DependencyNotFoundError(
        "NetoAPI requires the requests library. Use >>> pip install --upgrade requests"
    ) from None

from .api_client import NetoAPIClient

__all__ = [NetoAPIClient, NetoAPIRequestError]
