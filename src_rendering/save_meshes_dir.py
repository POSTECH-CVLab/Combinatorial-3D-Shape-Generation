import numpy as np
import os
import open3d as o3d

from geometric_primitives import bricks
from geometric_primitives import brick

import utils
import constants


def save_meshes(str_source, str_meshes, str_files):
    for str_file in str_files:
        str_brick = os.path.join(str_source, str_file)
        str_meshes_ = os.path.join(str_meshes, str_file[:-4])

        if not os.path.exists(str_meshes_):
            os.mkdir(str_meshes_)
        else:
            continue

        print('Creating {}'.format(str_file[:-4]))
        str_save = os.path.join(str_meshes_, str_file)
        str_save = str_save[:-4] + '_{}.ply'

        bricks_ = np.load(str_brick, allow_pickle=True)
        bricks_ = bricks_[()]
        print(bricks_)

        mesh_bricks, mesh_cubes = utils.get_mesh_bricks(bricks_)

        new_mesh = None
        for ind_mesh, mesh_brick in enumerate(mesh_bricks):
            if new_mesh is None:
                new_mesh = mesh_brick
            else:
                new_mesh += mesh_brick

            mesh_brick.rotate(mesh_brick.get_rotation_matrix_from_xyz((-np.pi / 2.0, 0.0, np.pi / 2.0)), center=False)
            mesh_brick.translate(np.array([
                [0],
                [0.5],
                [0]
            ]))

            o3d.io.write_triangle_mesh(str_save.format(ind_mesh + 1), mesh_brick, write_ascii=True)


        new_mesh.rotate(new_mesh.get_rotation_matrix_from_xyz((-np.pi / 2.0, 0.0, np.pi / 2.0)), center=False)
        new_mesh.translate(np.array([
            [0],
            [0.5],
            [0]
        ]))

        o3d.io.write_triangle_mesh(str_save.format('all'), new_mesh, write_ascii=True)


if __name__ == '__main__':
    str_files_dataset = os.listdir(constants.PATH_DATASET)
    print(str_files_dataset)

    if not os.path.exists(constants.PATH_MESHES):
        os.mkdir(constants.PATH_MESHES)

    # single brick
    bricks_ = bricks.Bricks(20)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    bricks_.add(brick_)
    
    mesh_bricks, mesh_cubes = utils.get_mesh_bricks(bricks_)
    mesh_brick = mesh_bricks[0]

    mesh_brick.paint_uniform_color(np.array([1.0, 0.0, 0.0]))

    mesh_brick.rotate(mesh_brick.get_rotation_matrix_from_xyz((-np.pi / 2.0, 0.0, np.pi / 2.0)), center=False)

    mesh_brick.translate(np.array([
        [0],
        [0.5],
        [0]
    ]))

    str_meshes_ = os.path.join(constants.PATH_MESHES, 'single_brick')

    if not os.path.exists(str_meshes_):
        os.mkdir(str_meshes_)

        str_save = os.path.join(str_meshes_, 'single_brick_1.ply')
        o3d.io.write_triangle_mesh(str_save, mesh_brick, write_ascii=True)

    save_meshes(constants.PATH_DATASET, constants.PATH_MESHES, str_files_dataset)
