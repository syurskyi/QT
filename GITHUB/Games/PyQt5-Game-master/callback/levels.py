# this code wroted by: Omar Othman
# What is this?
# ----------------------------------
# Q is question
# BR is Right button [Button Text, Show? False, True]
# BL Left button [Button Text, Show? False, True]
# first numbers is level second numbers is Question level at level
# ----------------------------------

QText = {
    0: {0: {"Q": "hi, i am Mariam", "BR": ["", False], "BL": ["Ok", True]},
        1: {"Q": "I have been placed in the forest", "BR": ["", False], "BL": ["Ok", True]},
        2: {"Q": "Can you help me? I want to find my house", "BR": ["No", True], "BL": ["Yes", True]},
        3: {"Q": "etc.................", "BR": ["", False], "BL": ["", False]}},
    1: {0: {"Q": "etc.................", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    2: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    3: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]},
        6: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    4: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]},
        6: {"Q": "", "BR": ["", False], "BL": ["", False]},
        7: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    5: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]},
        6: {"Q": "", "BR": ["", False], "BL": ["", False]},
        7: {"Q": "", "BR": ["", False], "BL": ["", False]},
        8: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    6: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]},
        6: {"Q": "", "BR": ["", False], "BL": ["", False]},
        7: {"Q": "", "BR": ["", False], "BL": ["", False]},
        8: {"Q": "", "BR": ["", False], "BL": ["", False]},
        9: {"Q": "", "BR": ["", False], "BL": ["", False]}},
    7: {0: {"Q": "", "BR": ["", False], "BL": ["", False]},
        1: {"Q": "", "BR": ["", False], "BL": ["", False]},
        2: {"Q": "", "BR": ["", False], "BL": ["", False]},
        3: {"Q": "", "BR": ["", False], "BL": ["", False]},
        4: {"Q": "", "BR": ["", False], "BL": ["", False]},
        5: {"Q": "", "BR": ["", False], "BL": ["", False]},
        6: {"Q": "", "BR": ["", False], "BL": ["", False]},
        7: {"Q": "", "BR": ["", False], "BL": ["", False]},
        8: {"Q": "", "BR": ["", False], "BL": ["", False]},
        9: {"Q": "", "BR": ["", False], "BL": ["", False]}}
    }


class Levels(object):
    def get_Q_as_json(self, i: int, i2: int):
        if i in QText and i2 in QText[i]:
            return str(QText[i][i2])
        
    def get_next_level(self, i: int, c: int):
        if i == -1 and c == -1:
            return 0, 0
        c += 1
        if i in QText and c in QText[i]:
            return i, c
        i += 1
        if i in QText:
            return i, 0
        return -1, -1
        
    
