import os
import sys

src_python = "src_python"
src_dir2 = ["src_python", "xx", "src", "yy"]

def syspath_add(filename, dir1, dir2=[]):
    try:
        filename.index(dir1)
        ruta_src = filename.split(dir1)
        
    except:
        if filename.find(src_python) == -1:
            raise PermissionError("Use only in the bussines project.")
        ruta_src = filename.split(src_python)
    
    src_dir2[1] = dir2[0]
    src_dir2[3] = dir2[1]
    ruta_dir1 = os.path.join(ruta_src[0], dir1)
    ruta_dir2yy = os.path.join(ruta_src[0], *src_dir2)
    
    sys.path.append(ruta_dir1)
    sys.path.append(ruta_dir2yy)

    print("Path added to sys.path: ", ruta_dir1)
    print("Path added to sys.path: ", ruta_dir2yy)