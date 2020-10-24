import numpy as np
import time
from datetime import datetime
import os
import copy

import brick
import bricks
import rules


def check_overlap_1d(min_max_1, min_max_2):
    assert isinstance(min_max_1, tuple)
    assert isinstance(min_max_2, tuple)

    return min_max_1[1] > min_max_2[0] and min_max_2[1] > min_max_1[0]

def check_overlap_2d(min_max_1, min_max_2):
    assert len(min_max_1) == 2
    assert len(min_max_2) == 2

    return check_overlap_1d(min_max_1[0], min_max_2[0]) and check_overlap_1d(min_max_1[1], min_max_2[1])

def check_overlap_3d(min_max_1, min_max_2):
    assert len(min_max_1) == 3
    assert len(min_max_2) == 3

    return check_overlap_1d(min_max_1[0], min_max_2[0]) and check_overlap_1d(min_max_1[1], min_max_2[1]) and check_overlap_1d(min_max_1[2], min_max_2[2])

def get_min_max_3d(vertices):
    min_max = [
        (np.min(vertices[:, 0]), np.max(vertices[:, 0])),
        (np.min(vertices[:, 1]), np.max(vertices[:, 1])),
        (np.min(vertices[:, 2]), np.max(vertices[:, 2]))
    ]

    return min_max

def get_dists(vert_source, vert_target):
    vert_source_0 = np.unique(vert_source[:, 0])
    vert_target_0 = np.unique(vert_target[:, 0])

    vert_source_1 = np.unique(vert_source[:, 1])
    vert_target_1 = np.unique(vert_target[:, 1])

    vert_source_0.sort()
    vert_source_1.sort()
    vert_target_0.sort()
    vert_target_1.sort()

    dist_0_all = np.maximum(vert_target_0[1] - vert_source_0[0], vert_source_0[1] - vert_target_0[0])
    dist_0_all = np.maximum(vert_target_0[1] - vert_target_0[0], dist_0_all)
    dist_0_all = np.maximum(vert_source_0[1] - vert_source_0[0], dist_0_all)

    dist_0 = (vert_source_0[1] - vert_source_0[0])\
        + (vert_target_0[1] - vert_target_0[0])\
        - dist_0_all

    dist_1_all = np.maximum(vert_target_1[1] - vert_source_1[0], vert_source_1[1] - vert_target_1[0])
    dist_1_all = np.maximum(vert_target_1[1] - vert_target_1[0], dist_1_all)
    dist_1_all = np.maximum(vert_source_1[1] - vert_source_1[0], dist_1_all)

    dist_1 = (vert_source_1[1] - vert_source_1[0])\
        + (vert_target_1[1] - vert_target_1[0])\
        - dist_1_all

    return dist_0, dist_1

def align_bricks(bricks_):
    list_bricks = bricks_.get_bricks()

    list_positions = []
    for brick_ in list_bricks:
        list_positions.append(brick_.get_position())
    positions = np.array(list_positions)

    trans = np.array([
        np.min(positions[:, 0]),
        np.min(positions[:, 1]),
        np.min(positions[:, 2]),
    ])

    list_bricks_new = []
    for brick_ in list_bricks:
        position_new = copy.deepcopy(brick_.get_position())
        direction_new = copy.deepcopy(brick_.get_direction())

        position_new -= trans

        brick_new = brick.Brick()
        brick_new.set_position(position_new)
        brick_new.set_direction(direction_new)
        list_bricks_new.append(brick_new)

    bricks_aligned = bricks.Bricks(bricks_.get_length())
    bricks_aligned.bricks = list_bricks_new
    bricks_aligned.validate_all()

    return bricks_aligned

def align_bricks_to_origin(bricks_):
    list_bricks = bricks_.get_bricks()

    list_positions = []
    for brick_ in list_bricks:
        list_positions.append(brick_.get_position())
    positions = np.array(list_positions)
    bottoms = np.where(positions[:, 2] == np.min(positions[:, 2]))[0]
    ind_origin = np.random.choice(bottoms, 1)
    ind_origin = ind_origin[0]

    brick_origin = copy.deepcopy(list_bricks[ind_origin])

    list_bricks_new = []
    for brick_ in list_bricks:
        position_new = copy.deepcopy(brick_.get_position())
        direction_new = copy.deepcopy(brick_.get_direction())

        position_new -= brick_origin.get_position()

        if brick_origin.get_direction() == 1:
            angle_rotated = np.pi * 1.0 / 2.0
            position_new_ = copy.deepcopy(position_new)
            position_new_.astype(np.float)
            position_new.astype(np.float)

            position_new[0] = np.round(np.cos(angle_rotated) * position_new_[0]) - np.round(np.sin(angle_rotated) * position_new_[1])
            position_new[1] = np.round(np.sin(angle_rotated) * position_new_[0]) + np.round(np.cos(angle_rotated) * position_new_[1])

            position_new = np.round(position_new)

            direction_new = (direction_new + brick_origin.get_direction()) % 2

        brick_new = brick.Brick()
        brick_new.set_position(position_new)
        brick_new.set_direction(direction_new)
        list_bricks_new.append(brick_new)

    bricks_aligned = bricks.Bricks(bricks_.get_length())
    bricks_aligned.bricks = list_bricks_new
    bricks_aligned.validate_all()

    return bricks_aligned

def save_bricks(bricks_, str_path, str_file=None):
    if not os.path.exists(str_path):
        os.makedirs(str_path)

    str_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    if str_file is None:
        str_save = os.path.join(str_path, 'bricks_{}.npy'.format(str_time))
    else:
        str_save = os.path.join(str_path, str_file + '.npy')

    np.save(str_save, bricks_)
    return
