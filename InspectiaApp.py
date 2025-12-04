# authors:
# David Hernandez Lopez, david.hernandez@uclm.es

import sys, os
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, '..'))

from Inspectia.defs import defs_paths
common_libs_absolute_path = os.path.join(current_path, defs_paths.COMMON_LIBS_RELATIVE_PATH)
sys.path.append(common_libs_absolute_path)

from Inspectia.gui.InspectiaDialog import InspectiaDialog
from Inspectia.defs import defs_main


def main():
    app = QApplication(sys.argv)
    current_path = os.path.dirname(os.path.realpath(__file__))
    path_file_qsettings = current_path + "/" + defs_main.SETTINGS_FILE
    settings = QSettings(path_file_qsettings, QSettings.IniFormat)
    dialog = InspectiaDialog(settings, current_path)
    icon_path = current_path + "/" + defs_main.IMAGES_PATH + "/" + defs_main.LOGO_ICON_FILE
    dialog.setWindowIcon(QIcon(icon_path))
    dialog.show()
    app.exec()


if __name__ == '__main__':
    main()
