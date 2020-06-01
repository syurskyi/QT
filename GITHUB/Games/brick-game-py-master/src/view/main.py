import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from src.view.round_button import create_buttons
from src.view.game_screen import GameScreen
from src.game_logic.game_os import GameOS


def _create_divider(parent, x=0, y=0, w=0, h=0):
    divider = QWidget(parent)
    divider.resize(w, h)
    divider.move(x, y)
    divider.setStyleSheet("""
        background-color:transparent;
        border-bottom: 3px solid gray;
        border-top: 3px solid #e1b74c;
    """)


def _create_game_title(parent):
    label = QLabel(parent)
    label.setText('BRICK GAME')
    label.show()
    label.move(
        (parent.width() / 2) - (label.width() // 2),
        parent.height() // 2 - 30
    )


def init_app():
    global game_screen
    app = QApplication([])
    screen_size = app.primaryScreen().size()
    
    view_height = screen_size.height() * 0.8
    view_width = view_height // 2
    view = QWidget()
    view.setStyleSheet('background-color: #f2f2f2')
    view.resize(view_width, view_height)
    
    _create_divider(
        parent=view,
        y=view_height//2,
        w=view_width,
        h=50
    )
    buttons = create_buttons(parent=view, ref_x=view_width // 2, ref_y=view_height//2 + 70)
    _create_game_title(parent=view)
    game_screen = GameScreen(parent=view)
    
    def draw_game_atoms(*coordinates, value=True):
        game_screen.draw_game_atoms(*coordinates, value=value)
    
    def draw_option_atoms(*coordinates, value=True):
        game_screen.draw_option_atoms(*coordinates, value=value)
    
    def show_labels():
        game_screen.show_labels()
    
    def hide_labels():
        game_screen.hide_labels()
    
    def show_music_icon():
        game_screen.show_music_icon()
    
    def hide_music_icon():
        game_screen.hide_music_icon()

    def show_pause_icon():
        game_screen.show_pause_icon()

    def hide_pause_icon():
        game_screen.hide_pause_icon()
    
    def set_key_event_handler(func):
        view.keyReleaseEvent = func
    
    view.show()
    app = {
        'run': app.exec_,
        'buttons': buttons,
        'screen_controller': {
            'set_key_event_handler': set_key_event_handler,
            'draw_game_atoms': draw_game_atoms,
            'draw_option_atoms': draw_option_atoms,
            'hide_labels': hide_labels,
            'show_labels': show_labels,
            'show_music_icon': show_music_icon,
            'hide_music_icon': hide_music_icon,
            'show_pause_icon': show_pause_icon,
            'hide_pause_icon': hide_pause_icon,
        }
    }
    buttons = app['buttons']
    screen_controller = app['screen_controller']
    game_os = GameOS(screen_controller, buttons)
    game_os.start()
    app['run']()
    
    game_os.kill()
    sys.exit()
