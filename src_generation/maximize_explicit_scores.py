import numpy as np
import os
import itertools

import wrappers
import utils
import constants

from geometric_primitives import bricks
from geometric_primitives import rules


str_score = 'height'
#str_score = 'width'
#str_score = 'depth'
#str_score = 'contacts'

str_exp = 'maximize_{}'.format(str_score)

num_bricks = 30

num_bo_rounds = 10
num_bo_init = 10
num_bo_acq = 10

time_bo_acq = 2.0

def score_bricks_height(bricks_):
    list_bricks_ = bricks_.get_bricks()

    height = 0
    for brick_ in list_bricks_:
        pos_2 = brick_.get_position()[2]
        cur_height = (pos_2 + 1) * brick_.height

        if height < cur_height:
            height = cur_height

    score = -1.0 * height
    return score

def score_bricks_axis(bricks_, ind_axis):
    list_bricks = bricks_.get_bricks()

    min_ = np.inf
    max_ = -np.inf

    for brick_ in list_bricks:
        vertices = brick_.get_vertices()
        vertices_ = vertices[:, ind_axis]
        min_vertices_ = np.min(vertices_)
        max_vertices_ = np.max(vertices_)

        if min_vertices_ < min_:
            min_ = min_vertices_
        if max_vertices_ > max_:
            max_ = max_vertices_

    score = max_ - min_
    score *= -1.0
    return score

def get_connections(bricks_, len_connections):
    list_bricks = bricks_.get_bricks()
    len_bricks = bricks_.get_length()
    print(len_bricks)

    num_combi = 1
    for ind in range(0, len_connections):
        num_combi *= len_bricks - ind
    for ind in range(0, len_connections):
        num_combi /= ind + 1

    num_connections = np.minimum(50, int(num_combi / 10))
    print(num_connections)

    list_connections = []

    while len(list_connections) < num_connections:
        for ind in range(0, len_bricks - len_connections + 1):
            new_bricks = bricks.Bricks(len_bricks)
            new_bricks.bricks = list_bricks[ind:ind+len_connections]

            try:
                new_bricks.validate_all()
                list_connections.append(new_bricks)
            except:
                pass

        np.random.shuffle(list_bricks)

    return list_connections

def order_bricks(brick_1, brick_2):
    if brick_1.get_position()[2] > brick_2.get_position()[2]:
        brick_temp = brick_1
        brick_1 = brick_2
        brick_2 = brick_temp
    return brick_1, brick_2

def transpose_position(brick_1, brick_2, diff_position):
    if brick_2.get_direction() == 0 and  brick_1.get_direction() == 0:
        pass
    elif brick_2.get_direction() == 0 and  brick_1.get_direction() == 1:
        pass
    elif brick_2.get_direction() == 1 and  brick_1.get_direction() == 0:
        diff_position = [diff_position[1], diff_position[0]]
    else:
        diff_position = [diff_position[1], diff_position[0]]

    diff_position = np.array(diff_position)
    return diff_position

def get_category(bricks_):
    list_bricks = bricks_.get_bricks()
    list_rules = rules.LIST_RULES_2_4

    brick_1 = list_bricks[0]
    brick_2 = list_bricks[1]
    brick_1, brick_2 = order_bricks(brick_1, brick_2)

    diff_direction = (brick_2.get_direction() + brick_1.get_direction()) % 2
    diff_position = (brick_2.get_position() - brick_1.get_position())[:2]

    diff_position = transpose_position(brick_1, brick_2, diff_position)

    ind = None
    num_ind = 0
    for rule in list_rules:
        if diff_direction == rule[1][0] and np.all(diff_position == np.array(rule[1][1])):
            ind = rule[0]
            num_ind += 1

    if not num_ind == 1:
        raise ValueError('Invalid category.')

    return ind

def get_categories(bricks_):
    list_bricks = bricks_.get_bricks()
    list_pairs = list(itertools.combinations(list_bricks, 2))

    list_categories = []

    for pair in list_pairs:
        new_bricks = bricks.Bricks(len(pair))
        new_bricks.bricks = list(pair)

        try:
            new_bricks.validate_all()
        except:
            continue

        category = get_category(new_bricks)
        list_categories.append(category)

    return list_categories

def score_bricks_num_contacts(bricks_):
    categories = get_categories(bricks_)
    list_rules = rules.LIST_RULES_2_4

    num_contacts = 0.0

    for category in categories:
        cur_elem = list_rules[category]
        cur_contacts = cur_elem[1][2]
        num_contacts += cur_contacts

    score_contacts = num_contacts
    score_contacts *= -1.0

    return score_contacts


if __name__ == '__main__':
    if str_score == 'height':
        fun_evaluation = lambda bricks_: score_bricks_height(bricks_)
    elif str_score == 'width':
        fun_evaluation = lambda bricks_: score_bricks_axis(bricks_, 0)
    elif str_score == 'depth':
        fun_evaluation = lambda bricks_: score_bricks_axis(bricks_, 1)
    elif str_score == 'contacts':
        fun_evaluation = lambda bricks_: score_bricks_num_contacts(bricks_)
    else:
        raise ValueError

    str_path = os.path.join(constants.PATH_RESULTS, str_exp)

    for ind_round in range(0, num_bo_rounds):
        np.random.seed(42 * (ind_round + 1))

        bricks_initial = utils.get_initial_bricks(2000)
        bricks_random = wrappers.random_all(bricks_initial, num_bricks)

        utils.save_results(
            str_path,
            'random_round_{}'.format(ind_round + 1),
            fun_evaluation,
            bricks_random,
            str_exp + '_random',
            False
        )

    for ind_round in range(0, num_bo_rounds):
        np.random.seed(42 * (ind_round + 1))

        bricks_initial = utils.get_initial_bricks(2000)
        bricks_randomeval = wrappers.random_eval_all(bricks_initial, num_bricks, num_bo_acq + num_bo_init, fun_evaluation)

        utils.save_results(
            str_path,
            'randomeval_round_{}'.format(ind_round + 1),
            fun_evaluation,
            bricks_randomeval,
            str_exp + '_randomeval',
            False
        )

    for ind_round in range(0, num_bo_rounds):
        np.random.seed(42 * (ind_round + 1))

        bricks_initial = utils.get_initial_bricks(2000)
        bricks_bo = wrappers.bo_all(bricks_initial, num_bricks, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, False, False)

        utils.save_results(
            str_path,
            'bo_round_{}'.format(ind_round + 1),
            fun_evaluation,
            bricks_bo,
            str_exp + '_bo',
            False
        )
