import numpy as np

from geometric_primitives import brick
from geometric_primitives import bricks

import dataset_common


def line_two_layers(length, direction):
    bricks_ = bricks.Bricks(200)

    list_bricks = []
    
    for ind in range(0, length):
        brick_ = brick.Brick()
        if direction == 0:
            brick_.set_position([0, 3 * ind, ind % 2])
        else:
            brick_.set_position([3 * ind, 0, ind % 2])
        brick_.set_direction(direction)
        list_bricks.append(brick_)
    
    for brick_ in list_bricks:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        line_two_layers(3, 0),
        line_two_layers(4, 0),
        line_two_layers(5, 0),
        line_two_layers(6, 0),
        line_two_layers(7, 0),
        line_two_layers(8, 0),
        line_two_layers(9, 0),
        line_two_layers(10, 0),
        line_two_layers(15, 0),
        line_two_layers(20, 0),
        line_two_layers(25, 0),
        line_two_layers(50, 0),
        line_two_layers(75, 0),
        line_two_layers(100, 0),
        line_two_layers(150, 0),
        line_two_layers(3, 1),
        line_two_layers(4, 1),
        line_two_layers(5, 1),
        line_two_layers(6, 1),
        line_two_layers(7, 1),
        line_two_layers(8, 1),
        line_two_layers(9, 1),
        line_two_layers(10, 1),
        line_two_layers(15, 1),
        line_two_layers(20, 1),
        line_two_layers(25, 1),
        line_two_layers(50, 1),
        line_two_layers(75, 1),
        line_two_layers(100, 1),
        line_two_layers(150, 1),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_LINE)

