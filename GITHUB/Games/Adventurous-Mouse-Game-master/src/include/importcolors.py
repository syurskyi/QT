# -*- coding: utf-8 -*-
from xml.dom import minidom


def importColors(path):
    """
    Import colors and their min/max thresholds in the HSV system from "colors.xml"

    Parameters:
        path (str): Path to the "colors.xml" file.

    Returns:
        colorList (list of dict): List of colors, defined by their "name", "min" (list of 3 integers) and "max" (list of 3 integers).
    """

    colors = minidom.parse(path).getElementsByTagName('color')

    valTypeDict = {'min': {'h': 0, 's': 0, 'v': 0},
                     'max': {'h': 179, 's': 254, 'v': 254}}

    colorList = []

    for color in colors:
        currColor = {'name': color.getAttribute('name').capitalize()}

        for valType, typeThresholds in valTypeDict.items():
            minimum = color.getElementsByTagName(valType)[0]
            currType = []

            for component, value in typeThresholds.items():
                currentComponent = minimum.getElementsByTagName(component)
                currType.append(int(currentComponent[0].getAttribute('value')) if len(currentComponent) else value)

            currColor[valType] = currType

        colorList.append(currColor)

    return colorList
