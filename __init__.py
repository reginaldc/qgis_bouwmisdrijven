# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BouwMisdrijven
                                 A QGIS plugin
 Deze plugin laat toe om de geselecteerde percelen te koppelen aan een bouwmisdrijf.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-27
        copyright            : (C) 2021 by Reginald Carlier
        email                : reginald.carlier@ingelmunster.be
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BouwMisdrijven class from file BouwMisdrijven.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bouw_misdrijven import BouwMisdrijven
    return BouwMisdrijven(iface)
