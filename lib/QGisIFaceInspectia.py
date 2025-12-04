# authors:
# David Hernandez Lopez, david.hernandez@uclm.es

import os, sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, '..'))

from Inspectia.defs import defs_paths
common_libs_absolute_path = os.path.join(current_path, defs_paths.COMMON_LIBS_RELATIVE_PATH)
sys.path.append(common_libs_absolute_path)

from pyLibQGIS.QGisIFace import QGisIFace

class QGisIFaceInspectia(QGisIFace):
    def __init__(self, iface, plugin_path):
        super().__init__(iface, plugin_path)

