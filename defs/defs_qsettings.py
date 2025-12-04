# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, '..'))

QSETTINGS_TAG_LAST_PATH = "last_path"
QSETTINGS_TAG_GIS_SERVER_API_URL = "gis_server_api_url"
QSETTINGS_TAG_GIS_SERVER_API_EMAIL = "gis_server_api_email"
QSETTINGS_TAG_GIS_SERVER_API_PASSWORD = "gis_server_api_password"
QSETTINGS_TAG_GIS_SERVER_API_TOKEN = "gis_server_api_token"

