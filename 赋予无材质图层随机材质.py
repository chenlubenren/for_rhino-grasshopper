import rhinoscriptsyntax as rs
import random
def randomcolor():

    red = int(255*random.random())

    green = int(255*random.random())

    blue = int(255*random.random())

    return [red,green,blue]

layers = rs.LayerNames()
for layer in layers:
    index = rs.LayerMaterialIndex(layer)
    if index==-1: 
        index = rs.AddMaterialToLayer(layer)
        rs.MaterialColor(index, color=randomcolor())
