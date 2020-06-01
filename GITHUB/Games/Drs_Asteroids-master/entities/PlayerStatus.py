from PyQt5 import QtWidgets


class PlayerStatus:
    def __init__(self, screen, x, y, padding=15, color="white"):
        self.x = x
        self.y = y
        self.padding = padding
        self.label = QtWidgets.QLabel(screen)
        self.label.setText("")
        self.label.setGeometry(x, y, 300, 20)
        self.label.setStyleSheet(f"color: {color};font-size: 12px; font-family: Arial Black; padding:{padding}px")

    def update(self, name, num_lives, num_points):
        text = f"ID: {name} | L: {num_lives} | PTS: {num_points}"
        # print(f"Status: {text}")  # For debugging purposes
        self.label.setText(text)
