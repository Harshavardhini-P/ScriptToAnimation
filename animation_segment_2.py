import bpy
import json
from math import radians


def set_floor(color=None):
    bpy.ops.mesh.primitive_plane_add(location=[0,0,0])
    Floor = bpy.context.active_object
    Floor.scale = 3*[100] 
    if color != None:
        mat = bpy.data.materials.new("Floor_color")
        mat.diffuse_color = color
        Floor.data.materials.append(mat)
        for face in Floor.data.polygons:
            face.material_index = face.index % 3
    return Floor

try:
    if bpy.context.object.mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.data.objects['Camera'].select_set(False)
    bpy.data.objects['Light'].select_set(False)
    bpy.ops.object.delete()
except:
    pass

#set floor on scene
#Floor = set_floor(color=(0.486,0.988,0,0))
Floor = set_floor()

#------------------Animation Process Begins----------------#
#read data from file
dataFile = open("E:/Mini Project ML/blender/SampleIO.json")
data = json.load(dataFile)
dataFile.close()

path = "C:/Users/thede/Downloads/Goalkeeper Overhand Throw.fbx"
loaction = [0,3,0]
rotation = [1.5707964897155762, -0.0, 0.4363323152065277]

bpy.ops.import_scene.fbx( filepath = path)
Fred  = bpy.context.active_object
Fred.location=loaction
Fred.rotation_euler = rotation

path = "C:/Users/thede/Downloads/thrown_ball.fbx"
#loaction = [0,3,0]
#rotation = [1.5707964897155762, -0.0, 0.4363323152065277]

bpy.ops.import_scene.fbx( filepath = path)
Ball  = bpy.context.active_object
#ob.location=loaction
#ob.rotation_euler = rotation