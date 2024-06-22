"""Custom exceptions for the netoapi library"""


class DependencyNotFoundError(Exception):
    """Custom exception for missing dependency"""


class NetoAPIRequestError(Exception):
    """Custom exception for request errors raised by the NetoAPIClient"""
