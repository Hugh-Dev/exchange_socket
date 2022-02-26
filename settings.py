"""
Flask settings for config project.
"""

from decouple import config
# SECURITY: secret host used in production!
SOCKET_HOST = config('SOCKET_HOST')
PORT = config('PORT')
DEBUG = config('DEBUG')
MSG = config('MSG')