from pycat.core import Window
from pycat.experimental import LdtkFile
from os.path import dirname

w = Window()

dir = dirname(__file__)
ldtk = LdtkFile(dir + "/Frist.ldtk")
ldtk.render_level(w, "Level_0", debug_tags= True)

def seeksome(ldtkr:LdtkFile):
    for level in ldtkr._data.levels:
        for layer in level.layer_instances:
            if layer.int_grid_csv:
                rows = layer.c_hei
                cols = layer.c_wid
                whatiwant =[]
                now = 0
                for i in range(rows):
                    rowr = []
                    for i in range(cols):     
                        rowr.append(layer.int_grid_csv[now])
                        now +=1
                    whatiwant.append(rowr)
    return whatiwant

final = seeksome(ldtk)
for i in final:
    print(*i)

w.run()
