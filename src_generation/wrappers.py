import numpy as np
import time
import copy

import bo
import utils

from geometric_primitives import utils as utils_gp


def random_all(bricks_initial, num_bricks):
    bricks_ = copy.deepcopy(bricks_initial)

    for ind_brick in range(0, num_bricks - 1):
        print('{}th bricks'.format(ind_brick + 2))
        time_start = time.time()

        next_brick = bricks_.sample()[0]
        bricks_.add(next_brick)

        time_end = time.time()
        print('Time consumed: {:.4f} sec.'.format(time_end - time_start))

    return bricks_

def random_eval_all(bricks_initial, num_bricks, num_acq, fun_evaluation):
    bricks_ = copy.deepcopy(bricks_initial)

    for ind_brick in range(0, num_bricks - 1):
        print('{}th bricks'.format(ind_brick + 2))
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
        print('Time consumed: {:.4f} sec.'.format(time_end - time_start))

    return bricks_

def bo_all(bricks_initial, num_bricks, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, use_rollback, use_multi, str_path=None):
    num_limit = 5

    list_len_bricks_all = []
    bricks_ = copy.deepcopy(bricks_initial)

    while bricks_.get_length() < num_bricks:
        ind_brick = bricks_.get_length() - 1
        print('{}th bricks'.format(ind_brick + 2))
        time_start = time.time()

        next_brick = bo.optimize(fun_evaluation, bricks_, num_bo_acq, num_bo_init, time_bo_acq, use_multi)[0]
        bricks_.add(next_brick)

        if use_rollback:
            bricks_rolled_back = utils.roll_back(bricks_, fun_evaluation, use_multi)

            if np.sum(bricks_rolled_back.get_length() == np.array(list_len_bricks_all)) <= num_limit:
                if not bricks_.get_length() == bricks_rolled_back.get_length():
                    print('Rolled back')
                bricks_ = copy.deepcopy(bricks_rolled_back)

            list_len_bricks_all.append(bricks_.get_length())
            print(list_len_bricks_all)
        print(bricks_.max_bricks)

        time_end = time.time()
        print('Time consumed: {:.4f} sec.'.format(time_end - time_start))

    if str_path is not None:
        utils_gp.save_bricks(bricks_, str_path=str_path)

    return bricks_
