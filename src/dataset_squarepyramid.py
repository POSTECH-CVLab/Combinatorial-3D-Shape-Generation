import copy

import brick
import bricks
import dataset_common


def plate(length):
    w = length
    h = length

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

    return list_brick_

def squarepyramid(length, trans_offset):
    assert length > 1

    bricks_ = bricks.Bricks(1000)

    list_brick_ = plate(length)
    
    list_brick_new = []

    for brick_ in list_brick_:
        brick_new = copy.deepcopy(brick_)
        pos_new = brick_new.get_position()
        pos_new[0] += trans_offset[0]
        pos_new[1] += trans_offset[1]
        brick_new.set_position(pos_new)
        list_brick_new.append(brick_new)
    list_brick_ = list_brick_new

    trans = 1
    for ind in range(0, 2 * length - 1):
        cur_length = (2 * length - 1 - ind)
        if cur_length % 2 == 1:
            trans += 2

        if cur_length % 2 == 0:
            cur_length_ = int(cur_length / 2)

            for ind_1 in range(0, cur_length):
                for ind_2 in range(0, cur_length_):
                    brick_new = brick.Brick()
                    brick_new.set_position([ind_1 * 2 + ind + trans_offset[0], ind_2 * 4 + trans + trans_offset[1], ind + 2])
                    brick_new.set_direction(0)
                    list_brick_.append(brick_new)
                    
        else:
            cur_length_ = int((cur_length - 1) / 2)

            for ind_1 in range(0, cur_length):
                for ind_2 in range(0, cur_length_):
                    brick_new = brick.Brick()
                    brick_new.set_position([ind_1 * 2 + ind + trans_offset[0], ind_2 * 4 + trans + trans_offset[1], ind + 2])
                    brick_new.set_direction(0)
                    list_brick_.append(brick_new)

    brick_new = brick.Brick()
    brick_new.set_position([(length - 1) * 2 + trans_offset[0], trans - 2 + trans_offset[1], 2 * length])
    brick_new.set_direction(0)
    list_brick_.append(brick_new)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        squarepyramid(2, (0, 0)),
        squarepyramid(3, (0, 0)),
        squarepyramid(4, (0, 0)),
        squarepyramid(5, (0, 0)),
        squarepyramid(6, (0, 0)),
        squarepyramid(2, (5, 5)),
        squarepyramid(3, (5, 5)),
        squarepyramid(4, (5, 5)),
        squarepyramid(5, (5, 5)),
        squarepyramid(6, (5, 5)),
        squarepyramid(2, (5, -5)),
        squarepyramid(3, (5, -5)),
        squarepyramid(4, (5, -5)),
        squarepyramid(5, (5, -5)),
        squarepyramid(6, (5, -5)),
        squarepyramid(2, (-5, 5)),
        squarepyramid(3, (-5, 5)),
        squarepyramid(4, (-5, 5)),
        squarepyramid(5, (-5, 5)),
        squarepyramid(6, (-5, 5)),
        squarepyramid(2, (-5, -5)),
        squarepyramid(3, (-5, -5)),
        squarepyramid(4, (-5, -5)),
        squarepyramid(5, (-5, -5)),
        squarepyramid(6, (-5, -5)),
        squarepyramid(2, (10, 0)),
        squarepyramid(3, (10, 0)),
        squarepyramid(4, (10, 0)),
        squarepyramid(5, (10, 0)),
        squarepyramid(6, (10, 0)),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_SQUAREPYRAMID)

