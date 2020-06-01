from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QIcon, QPixmap


class GameScreen(QWidget):
    
    def __init__(self, parent):
        super(GameScreen, self).__init__(parent)
        
        self._parent = parent
        self._music_on = False
        self._on_pause = False
        self._music_img_pixmap = QPixmap('assets/music.png')
        self._pause_img_pixmap = QPixmap('assets/coffee.png')
        self._game_grid_values = [[None for _ in range(10)] for __ in range(20)]
        self._option_grid_values = [[None for _ in range(4)] for __ in range(4)]
        self._init_view()

    def _init_view(self):
        padding_x = 50
        padding_y = 25
        width = self._parent.width() - 2 * padding_x
        height = self._parent.height() // 2 - 2 * padding_y
        height -= height % 20

        self.resize(width, height)
        self.move(padding_x, padding_y)
        self._init_game_grid()
        self._init_option_grid()
        self._init_labels()
    
    def _init_game_grid(self):
        height = self.height() - 20
        self._game_grid_dims = {
            'x': 10,
            'y': 10,
            'w': height // 2,
            'h': height
        }
        self._atom_dims = {
            'w': self._game_grid_dims['w'] // 10,
            'h': self._game_grid_dims['h'] // 20,
        }
    
    def _init_option_grid(self):
        width = self._atom_dims['w'] * 4 + 4
        self._option_grid_dims = {
            'x': self.width() * 0.8 - (width // 2),
            'y': self.height() // 2 - 20,
            'w': width,
            'h': self._atom_dims['h'] * 4 + 4
        }
        
    def _init_labels(self):
        def _create_label(y, text):
            x = self.width() * 0.8
            label = QLabel(self)
            label.setText(text)
            label.show()
            label.move(x - (label.width() // 2), y)
            label.setStyleSheet("background-color: Transparent")
            return label

        self._labels = []
        self._labels.append(_create_label(10, 'SCORE'))
        self._labels.append(_create_label(30, '0000'))
        self._labels.append(_create_label(50, 'HI-SCORE'))
        self._labels.append(_create_label(70, '0000'))
        
        lower_label_height_ref = self._option_grid_dims['y'] + self._option_grid_dims['h'] + 5
        self._labels.append(_create_label(lower_label_height_ref, '0/0'))
        self._labels.append(_create_label(lower_label_height_ref + 20, 'LEVEL 1'))
        self._labels.append(_create_label(lower_label_height_ref + 40, 'SPEED 1'))
        
        self.hide_labels()
    
    def show_labels(self):
        for label in self._labels:
            label.show()
    
    def hide_labels(self):
        for label in self._labels:
            label.hide()
            
    def _draw_atom(self, painter, dims, x, y, should_erase=False):
        gd = dims
        ad = self._atom_dims
        x = gd['x'] + x * ad['w']
        y = gd['y'] + y * ad['h']
        w = ad['w']
        h = ad['h']
        if not should_erase:
            painter.drawRect(x, y, w, h)
            color = QColor('#222')
        else:
            color = QColor('#c6d4cd')
        painter.fillRect(x + 2, y + 2, w - 3, h - 3, color)
    
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('#c6d4cd'))
        painter.drawRect(
            self._game_grid_dims['x'] - 5,
            self._game_grid_dims['y'] - 5,
            self._game_grid_dims['w'] + 10,
            self._game_grid_dims['h'] + 10,
        )
        painter.drawRect(
            self._option_grid_dims['x'] - 2,
            self._option_grid_dims['y'] - 2,
            self._option_grid_dims['w'],
            self._option_grid_dims['h'],
        )
        for h in range(20):
            for w in range(10):
                if self._game_grid_values[h][w]:
                    self._draw_atom(painter, self._game_grid_dims, w, h)
                
                elif self._game_grid_values[h][w] is False:
                    self._game_grid_values[h][w] = None
                    self._draw_atom(painter, self._game_grid_dims, w, h, True)
        
        for h in range(4):
            for w in range(4):
                if self._option_grid_values[h][w]:
                    self._draw_atom(painter, self._option_grid_dims, w, h)
                
                elif self._option_grid_values[h][w] is False:
                    self._option_grid_values[h][w] = None
                    self._draw_atom(painter, self._option_grid_dims, w, h, True)
        
        if self._music_on:
            painter.drawPixmap(
                self.width() * 0.67,
                self.height() - 25,
                17,
                17,
                self._music_img_pixmap
            )
        
        if self._on_pause:
            painter.drawPixmap(
                self.width() * 0.67 + 30,
                self.height() - 26,
                17,
                17,
                self._pause_img_pixmap
            )
    
    def draw_game_atoms(self, *coordinates, value=True):
        for x, y in coordinates:
            if x < 20 and y < 10 and x >= 0 and y >= 0:
                self._game_grid_values[x][y] = value
        self.update()
    
    def draw_option_atoms(self, *coordinates, value=True):
        for x, y in coordinates:
            if x < 20 and y < 10 and x >= 0 and y >= 0:
                self._option_grid_values[x][y] = value
        self.update()
    
    def show_music_icon(self):
        self._music_on = True
        self.update()
    
    def hide_music_icon(self):
        self._music_on = False
        self.update()

    def show_pause_icon(self):
        self._on_pause = True
        self.update()

    def hide_pause_icon(self):
        self._on_pause = False
        self.update()
