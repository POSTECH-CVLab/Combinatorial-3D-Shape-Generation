import open3d as o3d
import numpy as np
import numpy.matlib
import os

import constants


def preprocess(model, color):
    min_bound = model.get_min_bound()
    max_bound = model.get_max_bound()
    center = min_bound + (max_bound - min_bound) / 2.0
    scale = np.linalg.norm(max_bound - min_bound) / 2.0
    vertices = np.asarray(model.vertices)
    vertices -= np.matlib.repmat(center, len(model.vertices), 1)
    model.vertices = o3d.utility.Vector3dVector(vertices / scale)

    model.paint_uniform_color(color)

    return model

def get_cube(color):
    path_cube = os.path.join(constants.PATH_UNIT_MESHES, constants.STR_CUBE)

    mesh_cube = o3d.io.read_triangle_mesh(path_cube)
    mesh_cube = preprocess(mesh_cube, color)

    mesh_cube.translate(np.array([
        [0],
        [0],
        [0]
    ]))

    mesh_cube.transform(np.array([
        [0.735, 0, 0, 0],
        [0, 1.4775, 0, 0],
        [0, 0, 0.445, 0],
        [0, 0, 0, 1],
    ]))

    return mesh_cube

def get_voxel(color):
    path_cube = os.path.join(constants.PATH_UNIT_MESHES, constants.STR_CUBE)

    mesh_cube = o3d.io.read_triangle_mesh(path_cube)
    mesh_cube = preprocess(mesh_cube, color)

    mesh_cube.translate(np.array([
        [0],
        [0],
        [0]
    ]))

    mesh_cube.transform(np.array([
        [0.5, 0, 0, 0],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 0],
        [0, 0, 0, 1],
    ]))

    return mesh_cube

def get_mesh_bricks(bricks_):
    path_lego_2_4 = os.path.join(constants.PATH_UNIT_MESHES, constants.STR_LEGO_2_4)

    len_bricks = bricks_.get_length()
    mesh_bricks = []
    mesh_cubes = []

    for ind_bricks in range(1, len_bricks + 1):
        color = np.random.RandomState(43 * ind_bricks).rand(3)

        mesh_brick = o3d.io.read_triangle_mesh(path_lego_2_4)
        mesh_brick = preprocess(mesh_brick, color)
        mesh_bricks.append(mesh_brick)

        mesh_cube = get_cube(color)
        mesh_cubes.append(mesh_cube)

    mesh_brick = mesh_bricks[0]
    bound_min = mesh_brick.get_min_bound()
    bound_max = mesh_brick.get_max_bound()
    unit_axis_1 = (bound_max[0] - bound_min[0]) / 2
    unit_axis_2 = (bound_max[1] - bound_min[1]) / 4
    unit_axis_3 = (bound_max[2] - bound_min[2]) - 0.085

    for brick, mesh_brick, mesh_cube in zip(bricks_.get_bricks(), mesh_bricks, mesh_cubes):
        pos = brick.get_position()
        direc = brick.get_direction()
        mesh_brick.translate(np.array([
            [unit_axis_1 * pos[0]], 
            [unit_axis_2 * pos[1]], 
            [unit_axis_3 * pos[2]]
        ]))
        mesh_brick.rotate(mesh_brick.get_rotation_matrix_from_xyz((0.0, 0.0, np.pi / 2.0 * direc)))

        mesh_cube.translate(np.array([
            [unit_axis_1 * pos[0]], 
            [unit_axis_2 * pos[1]], 
            [unit_axis_3 * pos[2]]
        ]))

        mesh_cube.rotate(mesh_cube.get_rotation_matrix_from_xyz((0.0, 0.0, np.pi / 2.0 * direc)))

    return mesh_bricks, mesh_cubes

def get_mesh_voxels(voxels_):
    len_voxels = voxels_.get_length()
    mesh_voxels = []

    for ind_bricks in range(1, len_voxels + 1):
        color = np.random.RandomState(42 * ind_bricks).rand(3)

        mesh_voxel = get_voxel(color)
        mesh_voxels.append(mesh_voxel)

    mesh_voxel = mesh_voxels[0]
    bound_min = mesh_voxel.get_min_bound()
    bound_max = mesh_voxel.get_max_bound()
    unit_axis_1 = (bound_max[0] - bound_min[0]) + 0.03
    unit_axis_2 = (bound_max[1] - bound_min[1]) + 0.03
    unit_axis_3 = (bound_max[2] - bound_min[2]) + 0.03

    print(unit_axis_1)
    print(unit_axis_2)
    print(unit_axis_3)

    for voxel, mesh_voxel in zip(voxels_.get_voxels(), mesh_voxels):
        pos = voxel.get_position()
        direc = voxel.get_direction()
        mesh_voxel.translate(np.array([
            [unit_axis_1 * pos[0]], 
            [unit_axis_2 * pos[1]], 
            [unit_axis_3 * pos[2]]
        ]))
#        mesh_voxel.rotate(mesh_voxel.get_rotation_matrix_from_xyz((0.0, 0.0, np.pi / 2.0 * direc)))

    return mesh_voxels
