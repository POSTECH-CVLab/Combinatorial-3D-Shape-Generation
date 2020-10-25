import numpy as np
import time
import os
import copy

import brick
import bricks
import bo
import visualization as vis
import utils_primitive


def get_initial_bricks(num_bricks):
    brick_ = brick.Brick()

    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)

    bricks_ = bricks.Bricks(num_bricks)
    bricks_.add(brick_)

    return bricks_

def random_all(bricks_initial, num_bricks, num_rounds):
    list_bricks = []

    for ind_round in range(0, num_rounds):
        print('{} round'.format(ind_round + 1))

        bricks_ = copy.deepcopy(bricks_initial)

        for ind_brick in range(0, num_bricks - 1):
            print('{} round {}th bricks'.format(ind_round + 1, ind_brick + 2))
            time_start = time.time()

            next_brick = bricks_.sample()[0]
            bricks_.add(next_brick)

            time_end = time.time()
            print('Time consumed:', time_end - time_start, 'sec.')

        list_bricks.append(bricks_)

    return list_bricks

def random_eval_all(bricks_initial, num_bricks, num_rounds, num_acq, fun_evaluation):
    list_bricks = []

    for ind_round in range(0, num_rounds):
        print('{} round'.format(ind_round + 1))

        bricks_ = copy.deepcopy(bricks_initial)

        for ind_brick in range(0, num_bricks - 1):
            print('{} round {}th bricks'.format(ind_round + 1, ind_brick + 2))
            time_start = time.time()

            possible_bricks = bricks_.sample(num_acq)

            list_scores = []

            for possible_brick in possible_bricks:
                bricks_copied = copy.deepcopy(bricks_)
                bricks_copied.add(possible_brick)

                score_ = fun_evaluation(bricks_copied)
                list_scores.append(score_)

            scores = np.array(list_scores)
            ind_best = scores.argsort()[0]

            next_brick = possible_bricks[ind_best]
            bricks_.add(next_brick)

            time_end = time.time()
            print('Time consumed:', time_end - time_start, 'sec.')

        list_bricks.append(bricks_)

    return list_bricks

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

def bo_all(bricks_initial, num_bricks, num_bo_rounds, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, str_path, is_save=False, is_roll_back=False, is_multi=False):
    num_limit = 5

    list_bricks = []

    for ind_round in range(0, num_bo_rounds):
        print('{} round'.format(ind_round + 1))

        list_len_bricks_all = []

        bricks_ = copy.deepcopy(bricks_initial)

        while bricks_.get_length() < num_bricks:
            ind_brick = bricks_.get_length() - 1
            print('{} round {}th bricks'.format(ind_round + 1, ind_brick + 2))
            time_start = time.time()

            next_brick = bo.optimize(fun_evaluation, bricks_, num_bo_acq, num_bo_init, time_bo_acq, is_multi)[0]
            bricks_.add(next_brick)

            if is_roll_back:
                bricks_rolled_back = roll_back(bricks_, fun_evaluation, is_multi)

                if np.sum(bricks_rolled_back.get_length() == np.array(list_len_bricks_all)) <= num_limit:
                    if not bricks_.get_length() == bricks_rolled_back.get_length():
                        print('Rolled back')
                    bricks_ = copy.deepcopy(bricks_rolled_back)

                list_len_bricks_all.append(bricks_.get_length())
                print(list_len_bricks_all)
            print(bricks_.max_bricks)

            time_end = time.time()
            print('Time consumed:', time_end - time_start, 'sec.')

        if False:
            vis.visualize(bricks_)

        list_bricks.append(bricks_)

        if is_save:
            utils_primitive.save_bricks(bricks_, str_path=str_path)

    return list_bricks

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
