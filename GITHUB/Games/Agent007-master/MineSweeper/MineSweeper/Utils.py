"""
Здесь расположены функции,
которые помогают в реализации
игры
"""


def is_border_of_field(diff_row, diff_column, cell, game) -> bool:
    """функция определяет, является ли клетка границей поля"""
    if ((-1 <= diff_column <= 1 and ((diff_row == -1 and cell.i == game.height - 1) or
                                     (cell.i == 0 and diff_row == 1))) or (
            -1 <= diff_row <= 1 and ((diff_column == 1 and cell.j == 0) or
                                     (diff_column == -1 and cell.j == game.width - 1)))):
        return True
    return False
