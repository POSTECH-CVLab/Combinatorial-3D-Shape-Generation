import copy

import brick
import bricks
import dataset_common


def cuboid(w, h, d):
    assert d > 1
    bricks_ = bricks.Bricks(1000)

    list_brick_ = []

    w_last = 2 * w - 2
    h_last = 2 * h - 1 # 5

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    for i in range(h_last):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, h_last * 2, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    leftmost_x = 2
    bottommost_y = 0

    rightmost_x = w_last * 2
    topmost_y = h_last * 2

    #if w % 2 == 0:
    for idx in range(h):
        if idx % 2 == 0:
            for i in range(w_last):
                for j in range(2):
                    brick_ = brick.Brick()
                    brick_.set_position([i * 2 + leftmost_x,
                                         j * (topmost_y - bottommost_y) + bottommost_y, (i % 2 == 0)])
                    brick_.set_direction(1)
                    list_brick_.append(brick_)
            if idx != (h - 1):
                for i in range(2):
                    brick_ = brick.Brick()
                    brick_.set_position([rightmost_x + 1,
                                         i * (topmost_y - 1 - (bottommost_y + 1)) + (bottommost_y + 1), 1])
                    brick_.set_direction(0)
                    list_brick_.append(brick_)
        else:
            for i in range(w_last):
                for j in range(2):
                    brick_ = brick.Brick()
                    brick_.set_position([rightmost_x - i * 2,
                                         j * (topmost_y - bottommost_y) + bottommost_y, (i % 2 == 1)])
                    brick_.set_direction(1)
                    list_brick_.append(brick_)
            if idx != (h - 1):
                for i in range(2):
                    brick_ = brick.Brick()
                    brick_.set_position([leftmost_x - 1,
                                         i * (topmost_y - 1 - (bottommost_y + 1)) + (bottommost_y + 1), 0])
                    brick_.set_direction(0)
                    list_brick_.append(brick_)

        topmost_y -= 2
        bottommost_y += 2

    if h % 2 == 0:
        brick_ = brick.Brick()
        brick_.set_position([1, h_last, 0])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    else:
        brick_ = brick.Brick()
        brick_.set_position([rightmost_x + 1, h_last, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for ind in range(2, d):
        for brick_ in list_brick_:
            if brick_.get_position()[2] == (ind % 2):
                brick_new = copy.deepcopy(brick_)
                pos_new = brick_new.get_position()
                pos_new[2] = ind
                brick_new.set_position(pos_new)

                list_brick_.append(brick_new)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        cuboid(1, 1, 2),
        cuboid(1, 1, 3),
        cuboid(1, 1, 4),
        cuboid(1, 2, 2),
        cuboid(1, 2, 3),
        cuboid(1, 2, 4),
        cuboid(1, 3, 2),
        cuboid(1, 3, 3),
        cuboid(1, 3, 4),
        cuboid(2, 1, 2),
        cuboid(2, 1, 3),
        cuboid(2, 1, 4),
        cuboid(2, 2, 2),
        cuboid(2, 2, 3),
        cuboid(2, 2, 4),
        cuboid(2, 3, 2),
        cuboid(2, 3, 3),
        cuboid(2, 3, 4),
        cuboid(2, 4, 2),
        cuboid(2, 4, 3),
        cuboid(2, 4, 4),
        cuboid(3, 1, 2),
        cuboid(3, 1, 3),
        cuboid(3, 1, 4),
        cuboid(3, 2, 2),
        cuboid(3, 2, 3),
        cuboid(3, 2, 4),
        cuboid(3, 3, 2),
        cuboid(3, 3, 3),
        cuboid(3, 3, 4),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_CUBOID)

