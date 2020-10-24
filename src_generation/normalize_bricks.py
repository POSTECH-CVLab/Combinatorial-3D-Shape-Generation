import numpy as np
import os
import copy

import brick
import bricks


def align_to_origin(bricks_):
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


if __name__ == '__main__':
    import visualization as vis

    str_dataset = '../dataset'

    ind_label = 9
    ind_target = 3

    str_label = 'label{}'.format(ind_label)
    str_target = '{}_{}.npy'.format(str_label, ind_target)
    print(str_target)

    target = np.load(os.path.join(str_dataset, str_target), allow_pickle=True)
    target = target[()]
    print(target.get_length())

    vis.visualize(target)
    bricks_ = align_to_origin(target)
    vis.visualize(bricks_)
