import numpy as np

from geometric_primitives import brick
from geometric_primitives import bricks

import dataset_common


def random(num_bricks_min=5, num_bricks_max=100):
    num_bricks = np.random.randint(low=num_bricks_min, high=num_bricks_max)
    print('Assembling {} bricks'.format(num_bricks))

    brick_ = brick.Brick()

    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)

    bricks_ = bricks.Bricks(num_bricks, '0')
    bricks_.add(brick_)

    for ind in range(0, num_bricks - 1):
        next_brick = None
        while next_brick is None:
            next_brick = bricks_.sample()[0]

        bricks_.add(next_brick)

    bricks_.validate_all()

    return bricks_


if __name__ == '__main__':
    num_brick_combinations = 30

    list_bricks_ = []
    for ind in range(0, num_brick_combinations):
        np.random.seed(ind * 42)
        list_bricks_.append(random())

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_RANDOM)
