import numpy as np
import os

from geometric_primitives import brick
from geometric_primitives import bricks


def get_initial_bricks(num_bricks):
    brick_ = brick.Brick()

    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)

    bricks_ = bricks.Bricks(num_bricks)
    bricks_.add(brick_)

    return bricks_

def roll_back(bricks_, fun_evaluation, is_multi, num_steps=1, threshold=2.5):
    list_bricks = bricks_.get_bricks()
    len_bricks = bricks_.get_length()
    if len_bricks - num_steps - 1 < 1:
        return bricks_

    list_scores = []

    for ind in range(len_bricks - num_steps - 2, len_bricks):
        if ind < 1:
            continue
        cur_bricks = bricks.Bricks(bricks_.max_bricks)
        cur_bricks.bricks = list_bricks[:ind+1]
#        cur_bricks.validate_all()

        if is_multi:
            cur_score, _ = fun_evaluation(cur_bricks)
        else:
            cur_score = fun_evaluation(cur_bricks)

        list_scores.append(cur_score)

    list_steps = []

    for ind in range(0, len(list_scores) - 1):
        gap = list_scores[ind+1] - list_scores[ind]
        gap = np.abs(gap)
        list_steps.append(gap)

    if np.sum(list_steps) > threshold:
        print('Rolling back')
        cur_bricks = bricks.Bricks(bricks_.max_bricks)
        cur_bricks.bricks = list_bricks[:len_bricks - num_steps - 1]
        cur_bricks.validate_all()
    else:
        cur_bricks = bricks_

    return cur_bricks

def save_results(str_path, str_file, fun_evaluation, bricks_, str_exp, is_multi):
    if not os.path.exists(str_path):
        os.makedirs(str_path)
    str_path_ = os.path.join(str_path, str_file)

    dict_results = {}

    list_bricks_ = bricks_.get_bricks()

    list_scores = []
    list_lengths = []

    bricks_tested = bricks.Bricks(bricks_.max_bricks)

    for cur_brick in list_bricks_:
        bricks_tested.add(cur_brick)

        if is_multi:
            score, _ = fun_evaluation(bricks_tested)
        else:
            score = fun_evaluation(bricks_tested)

        list_scores.append(score)
        list_lengths.append(bricks_tested.get_length())

    dict_result = {
        'str_exp': str_exp,
        'bricks': bricks_,
        'list_scores': list_scores,
        'list_lengths': list_lengths,
    }

    np.save(str_path_, dict_result)
    return
