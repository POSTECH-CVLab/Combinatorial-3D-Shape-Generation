import numpy as np
import os

import constants


if __name__ == '__main__':
    str_files = os.listdir(constants.PATH_MESHES)
    print(str_files)

    for str_file in str_files:
        str_path_file = os.path.join(constants.PATH_MESHES, str_file)

        if os.path.isdir(str_path_file):
            str_plys = os.listdir(str_path_file)

            for str_ply in str_plys:
                if '.ply' in str_ply:
                    cur_ply = os.path.join(str_path_file, str_ply)
                    print(cur_ply)
                    file_new = open('temp.ply', 'w')

                    with open(cur_ply, 'r') as file_old:  
                        for row in file_old:
                            row = row.replace('double', 'float')
                            file_new.write(row)
                    file_new.close()
            
                    os.rename('temp.ply', cur_ply)

