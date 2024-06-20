import importlib.metadata
import requests
import warnings
import os

# setup warnings
def custom_formatwarning(msg, *args, **kwargs):
    # ignore everything except the message
    return str(msg) + '\n'
warnings.formatwarning = custom_formatwarning


try:
    __version__ = importlib.metadata.version("quantagonia-api-client")
    warnings.warn("WARNING: The package 'quantagonia-api-client' is deprecated. Please 'pip install quantagonia'")
except:
    __version__ = "dev"
    # don't check for updates in this case
