from math import radians

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QTransform, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget


def create_label(screen: QWidget, r: float) -> QLabel:
    label = QLabel(screen)

    # for testing purposes
    # label.setStyleSheet(f"background-color: white;")
    # label.setLineWidth(3)

    label.setAlignment(Qt.AlignCenter)
    label.setMinimumSize(1, 1)
    label.resize(r * 2, r * 2)
    return label


def create_pixmap(label: QLabel, image: QImage) -> QPixmap:
    return QPixmap.fromImage(image) \
        .scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)


def rotate_pixmap(pixmap: QPixmap, angle: float) -> QPixmap:
    trans = QTransform()
    trans.rotate(angle)
    return pixmap.transformed(trans)


def convert_to_grayscale(pixmap: QPixmap) -> QPixmap:
    image = QtGui.QPixmap.toImage(pixmap)
    grayscale = image.convertToFormat(QtGui.QImage.Format_Grayscale8)
    return QtGui.QPixmap.fromImage(grayscale)
