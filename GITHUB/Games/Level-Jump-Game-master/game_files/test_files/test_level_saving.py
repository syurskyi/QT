from leveleditor import LevelEditor
from levelobject import LevelObject


level_editor = LevelEditor()

#manually set some objects

level_editor.player = LevelObject('player')

level_editor.player.set_pos(20,3)

level_editor.finish.append(LevelObject('finish'))
level_editor.finish[0].set_pos(5,9)

vis = LevelObject('visible')
vis.set_pos(22,6)
level_editor.visible.append(vis)


return_val = level_editor.create_file('surkea_leveli')

print(return_val)

