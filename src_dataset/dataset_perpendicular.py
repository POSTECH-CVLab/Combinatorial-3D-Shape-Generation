from geometric_primitives import brick
from geometric_primitives import bricks
from geometric_primitives import rules

import dataset_common


if __name__ == '__main__':
    list_rules = rules.LIST_RULES_2_4
    print(list_rules)

    list_bricks_ = []

    for rule in list_rules:
        bricks_ = bricks.Bricks(100, '0')
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 0])
        brick_.set_direction(0)
        bricks_.add(brick_)

        if rule[1][0] == 1:
            brick_next = brick.Brick()
            brick_next.set_position([rule[1][1][0], rule[1][1][1], 1])
            brick_next.set_direction(rule[1][0])
            bricks_.add(brick_next)

            list_bricks_.append(bricks_)

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_PERPENDICULAR)
