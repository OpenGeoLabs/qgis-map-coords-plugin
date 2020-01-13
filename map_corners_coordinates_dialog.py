# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Map_Corners_CoordinatesDialog
                                 A QGIS plugin
 This plugin saves coordinates of corners of the selected map area.
                             -------------------
        begin                : 2016-10-12
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Kala_Kulovana
        email                : michael.kala193@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, QtWidgets, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'map_corners_coordinates_qdockwidget.ui'))


class MapCornersCoordinatesDialog(QtWidgets.QDockWidget, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MapCornersCoordinatesDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
