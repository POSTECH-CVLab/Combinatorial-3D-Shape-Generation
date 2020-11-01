import numpy as np
import os

import wrappers
import utils
import constants


str_exp = 'maximize_height'

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


if __name__ == '__main__':
    fun_evaluation = lambda bricks_: score_bricks_height(bricks_)

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
