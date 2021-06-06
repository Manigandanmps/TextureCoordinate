import openmesh as om
import numpy as np
import sys
import os
from pathlib import Path
import os.path 

def get_texture(file_name):
    mesh = om.TriMesh()
    # mesh = om.read_trimesh(file_name, vertex_normal=True)
    mesh = om.read_trimesh(file_name)
    
    #iterate over the vertices adjacent to a vertex vh0
    for vh in mesh.vertices():                                                                                                                                                     
        print(vh.idx())
        
    #Get texture coordinates of vertex:
    tc = mesh.texcoord2D(vh)
    # tx= mesh.vertex_normals(vh)
    
    #Let's start with adding vertex normals to the mesh:
    mesh.request_vertex_normals()
    
    #Let's start with adding face normals to the mesh:
    # mesh.request_face_normals();

           
    
    #OpenMesh doesn’t save texture coordinates for vertices(vt lines) in obj file. 
    #To fix it pass argument vertex_tex_coord in the method write_mesh

    #get stem of file name 
    output_name = Path(file_name).stem
                
    om.write_mesh(file_name+'_filled.obj', mesh, vertex_tex_coord=True, vertex_normal=True)
    # mesh1 = om.read_trimesh('mani_mesh.obj', vertex_tex_coord=True)
    # om.write_mesh('mani_texture.obj', mesh, vertex_tex_coord=True, face_color=True)

if __name__ == "__main__":
    
    arg = sys.argv[1]
    print (arg)
    
    

    if os.path.isfile(arg):
        print ("Input is file")
        get_texture(arg)
    else:
        print ("Invalid file")

    if os.path.isdir(arg):
        for root, dirs, files in os.walk(arg):
            for file in files:
                if file.endswith(".obj"):
                    input = (os.path.join(root, file))
                    get_texture(input)
   