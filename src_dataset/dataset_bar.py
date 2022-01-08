from geometric_primitives import brick
from geometric_primitives import bricks

import dataset_common


def bar(height, direction):
    bricks_ = bricks.Bricks(200)

    list_brick_ = []
    
    for ind in range(0, height):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, ind])
        brick_.set_direction(direction)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        bar(3, 0),
        bar(4, 0),
        bar(5, 0),
        bar(6, 0),
        bar(7, 0),
        bar(8, 0),
        bar(9, 0),
        bar(10, 0),
        bar(12, 0),
        bar(14, 0),
        bar(16, 0),
        bar(18, 0),
        bar(20, 0),
        bar(22, 0),
        bar(24, 0),
        bar(3, 1),
        bar(4, 1),
        bar(5, 1),
        bar(6, 1),
        bar(7, 1),
        bar(8, 1),
        bar(9, 1),
        bar(10, 1),
        bar(12, 1),
        bar(14, 1),
        bar(16, 1),
        bar(18, 1),
        bar(20, 1),
        bar(22, 1),
        bar(24, 1),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_BAR)
