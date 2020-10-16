import brick
import bricks
import dataset_common


def wall(height, width, direction):
    bricks_ = bricks.Bricks(200)

    list_brick_ = []
    
    for ind_width in range(0, width):
        for ind_height in range(0, height):
            brick_ = brick.Brick()
            if direction == 1:
                brick_.set_position([ind_width * 4 + (ind_height % 2) * 2, 0, ind_height])
            else:
                brick_.set_position([0, ind_width * 4 + (ind_height % 2) * 2, ind_height])

            brick_.set_direction(direction)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        wall(2, 3, 0),
        wall(2, 4, 0),
        wall(2, 5, 0),
        wall(3, 3, 0),
        wall(3, 4, 0),
        wall(3, 5, 0),
        wall(4, 3, 0),
        wall(4, 4, 0),
        wall(4, 5, 0),
        wall(5, 3, 0),
        wall(5, 4, 0),
        wall(5, 5, 0),
        wall(5, 6, 0),
        wall(6, 3, 0),
        wall(6, 4, 0),
        wall(6, 5, 0),
        wall(6, 6, 0),
        wall(7, 3, 0),
        wall(7, 4, 0),
        wall(7, 5, 0),
        wall(7, 6, 0),
        wall(8, 4, 0),
        wall(8, 5, 0),
        wall(8, 6, 0),
        wall(9, 4, 0),
        wall(9, 5, 0),
        wall(9, 6, 0),
        wall(10, 4, 0),
        wall(10, 5, 0),
        wall(10, 6, 0),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_WALL)

