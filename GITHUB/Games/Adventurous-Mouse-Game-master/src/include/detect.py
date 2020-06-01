# -*- coding: utf-8 -*-
from math import degrees, atan

from cv2 import COLOR_BGR2HSV, COLOR_HSV2RGB, cvtColor, resize
from cv2 import arrowedLine, circle, FONT_HERSHEY_SIMPLEX, LINE_AA, putText, rectangle
from numpy import where


def detect(capture, color1, color2):
    """
    Detect the arrow's direction, defined by two colors (begin & end).

    Parameters:
        capture (cv2 VideoCapture object): Video's stream source.
        color1 (list of 2 tuples [min/max threshold] of 3 integers [colored pixel]): Arrow's begin HSV color thresholds (min/max).
        color2 (list of 2 tuples [min/max threshold] of 3 integers [colored pixel]): Arrow's end HSV color thresholds (min/max).

    Returns:
        src (Numpy array with shape (331, 311, 3)): Captured RGB image with information written on it (colors framing, arrow, angle and the direction)
        direction (int): Arrow's direction (8 geographic directions).
    """

    _, src = capture.read()
    src = resize(src, (331, 311)) # Resize the image to fit in the game's frame

    src = cvtColor(src, COLOR_BGR2HSV)

    color1 = [*zip(*where((src >= color1[0]).all(-1) & (src <= color1[1]).all(-1)))] # Get the pixel's positions that match the color1 min/max thresholds (list of tuples of 2 integers [lign & column])
    color2 = [*zip(*where((src >= color2[0]).all(-1) & (src <= color2[1]).all(-1)))] # Get the pixel's positions that match the color2 min/max thresholds (list of tuples of 2 integers [lign & column])

    showText = 'No matching'
    direction = -1

    if len(color1) >= 500 and len(color2) >= 500: # If more than 500 pixels of each color have been detected (do not consider the outliers)
        # Find the minimal point of color1
        minX = min(color1, key=lambda val: val[1])[1] # Find the minimal X, represented by the pixel in the minimal column
        minY = min(color1, key=lambda val: val[0])[0] # Find the minimal Y, represented by the pixel in the minimal lign
        # Find the maximal point of color1
        maxX = max(color1, key=lambda val: val[1])[1] # Find the maximal X, represented by the pixel in the maximal column
        maxY = max(color1, key=lambda val: val[0])[0] # Find the maximal Y, represented by the pixel in the maximal lign
        rectangle(src, (minX, minY), (maxX, maxY), (10, 198, 250), 2)
        centerPoint1 = (int((minX+maxX)/2), int((minY+maxY)/2)) # Find the center of "minimal container rectangle" of color1
        circle(src, centerPoint1, 2, (10, 198, 250), -1)

        # Find the minimal point of color2
        minX = min(color2, key=lambda val: val[1])[1] # Find the minimal X (pixel in minimal column)
        minY = min(color2, key=lambda val: val[0])[0] # Find the minimal Y (pixel in minimal lign)
        # Find the maximal point of color2
        maxX = max(color2, key=lambda val: val[1])[1] # Find the maximal X (pixel in maximal column)
        maxY = max(color2, key=lambda val: val[0])[0] # Find the maximal Y (pixel in minimal lign)
        rectangle(src, (minX, minY), (maxX, maxY), (10, 198, 250), 2)
        centerPoint2 = (int((minX+maxX)/2), int((minY+maxY)/2)) # Find the center of "minimal container rectangle" of color2
        circle(src, centerPoint2, 2, (10, 198, 250), -1)

        arrowedLine(src, centerPoint1, centerPoint2, (10, 198, 250), 2, LINE_AA)

        # Calculate the absolute angle formed by the two points (framed by a rectangle)
        nominator = centerPoint2[1] - centerPoint1[1]
        denominator = centerPoint2[0] - centerPoint1[0]
        angle = 90 if denominator == 0 else int(abs(degrees(atan(nominator/denominator))))

        # Find the position in the trigonometric circle
        if not (nominator <= 0 and denominator >= 0): # First quarter [0, 90]°
            if nominator <= 0 and denominator <= 0: # Second quarter [90, 180]°
                angle = 180 - angle
            elif nominator > 0 and denominator <= 0: # Third quarter [180, 270]°
                angle += 180
            elif nominator > 0 and denominator > 0: # Fourth quarter [270, 360]°
                angle = 360 - angle

        showText = 'Matching colors (no move)'

        if (0 <= angle <= 10) or (350 <= angle <= 360):
            showText = 'RIGHT (North)'
            direction = 0
        elif 35 <= angle <= 55:
            showText = 'RIGHT-UP (Northeast)'
            direction = 1
        elif 80 <= angle <= 100:
            showText = 'UP (East)'
            direction = 2
        elif 125 <= angle <= 145:
            showText = 'LEFT-UP (Southeast)'
            direction = 3
        elif 170 <= angle <= 190:
            showText = 'LEFT (South)'
            direction = 4
        elif 215 <= angle <= 235:
            showText = 'LEFT-DOWN (Southwest)'
            direction = 5
        elif 260 <= angle <= 280:
            showText = 'DOWN (West)'
            direction = 6
        elif 305 <= angle <= 325:
            showText = 'RIGHT-DOWN (Northwest)'
            direction = 7

        showText = 'Angle: ' + str(angle) + ' [' + showText + ']'

    putText(src, showText, (0, 15), FONT_HERSHEY_SIMPLEX, 0.5, (42, 178, 219), 1)

    src = cvtColor(src, COLOR_HSV2RGB)

    return src, direction
