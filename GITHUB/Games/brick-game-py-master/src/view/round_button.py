from PyQt5.QtWidgets import QPushButton


class RoundButton(QPushButton):
    
    def __init__(self, parent, x, y, radius, color='#ffa500', text=''):
        QPushButton.__init__(self, parent)
        self.parent = parent
        self.setStyleSheet(f"""
            background-color:{color};
            border-style: outset;
            border-width: 0;
            border-radius: {radius // 2};
        """)
        self.resize(radius, radius)
        self.setText(text)
        self.move(x, y)
        self.setText('')


def create_buttons(parent, ref_x, ref_y):
    h = parent.height()
    buttons = {}
    
    menu_button_radius = h // 25
    
    def create_menu_button(x, color='#ffa500'):
        return RoundButton(parent, x=x, y=ref_y, radius=h // 25, color=color)
    
    def create_arrow_buttons():
        nonlocal buttons
        r = h // 15
        up_y = ref_y + ref_y // 8
        up_x = ref_x - ref_x // 1.7
        buttons['up'] = RoundButton(parent, x=up_x, y=up_y, radius=r)
        buttons['left'] = RoundButton(parent, x=up_x - r, y=up_y + r, radius=r)
        buttons['right'] = RoundButton(parent, x=up_x + r, y=up_y + r, radius=r)
        buttons['down'] = RoundButton(parent, x=up_x, y=up_y + 2 * r, radius=r)

    buttons['pause'] = create_menu_button(x=ref_x)
    buttons['escape'] = create_menu_button(x=ref_x + 1 * (menu_button_radius + 10))
    buttons['help'] = create_menu_button(x=ref_x + 2 * (menu_button_radius + 10))
    buttons['power'] = create_menu_button(
        x=ref_x + 3 * (menu_button_radius + 10),
        color='#ff4444'
    )

    buttons['action'] = RoundButton(parent, x=ref_x + ref_x // 3, y=ref_y + ref_y // 4, radius=h // 10)
    create_arrow_buttons()
    return buttons
