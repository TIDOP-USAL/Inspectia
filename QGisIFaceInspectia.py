# authors:
# David Hernandez Lopez, david.hernandez@uclm.es

from defs import defs_qgis
from pyLibQGIS.QGisIFace import QGisIFace

class QGisIFaceInspectia(QGisIFace):
    def __init__(self, iface, plugin_path):
        super().__init__(iface, plugin_path)
        self.qml_path = self.plugin_path + defs_qgis.QML_PATH

    def close_project(self):
        super().close_project()

    def load_project(self):
        str_error = super().load_project(defs_qgis.PROJECT_LAYERS_GROUP_PREFIX)
        if str_error:
            return str_error

        return str_error

    def open_project(self,
                     project):
        super().open_project(project)
        self.load_project()

