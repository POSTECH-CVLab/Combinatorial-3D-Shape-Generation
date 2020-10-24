import numpy as np
import copy
from bayeso import gp
from bayeso import acquisition
import time

import bricks

str_cov = 'matern52'


def _optimize_objective(fun_acquisition, X_train, Y_train, X_test, cov_X_X, inv_cov_X_X, hyps):
    X_test = np.atleast_2d(X_test)
    pred_mean, pred_std = gp.predict_test_(X_train, Y_train, X_test, cov_X_X, inv_cov_X_X, hyps, str_cov=str_cov, prior_mu=None, debug=False)
    acquisitions = fun_acquisition(pred_mean=pred_mean.flatten(), pred_std=pred_std.flatten(), Y_train=Y_train)

    return acquisitions

def optimize(fun_evaluation, bricks_, num_bricks, num_init, time_bo_acq):
    bricks_all = bricks_.sample(num_init)

    X_all = []
    Y_all = []

    for cur_brick in bricks_all:
        bricks_copied = copy.deepcopy(bricks_)
        bricks_copied.add(cur_brick)

        cur_score = fun_evaluation(bricks_copied)
        cur_vector = cur_brick.get_position_direction()

        X_all.append(cur_vector)
        Y_all.append([cur_score])

    while len(bricks_all) <= num_init + num_bricks:
        print('Iteration', len(bricks_all))
        # TODO: you should double-check this scope carefully.

        time_start_iteration = time.time()

        cov_X_X, inv_cov_X_X, hyps = gp.get_optimized_kernel(
            np.array(X_all),
            np.array(Y_all),
            None, str_cov, debug=False)
        fun_acquisition = acquisition.ucb

        fun_negative_acquisition = lambda X_test: -1.0 * _optimize_objective(fun_acquisition, np.array(X_all), np.array(Y_all), X_test, cov_X_X, inv_cov_X_X, hyps)

        bo_bricks = []
        bo_vectors = []
        bo_acqs = []

        bricks_sampled = []
        time_start = time.time()
        cur_time = time.time()

        num_iters = 0
        while (cur_time - time_start) < time_bo_acq:
            np.random.seed(42 * len(bricks_all) + len(bricks_sampled) + int(cur_time) + num_iters)
            bricks_sampled.append(bricks_.sample(1)[0])
            cur_time = time.time()
            num_iters += 1

        print('#samples:', len(bricks_sampled))

        num_duplicated = 0
        for brick_sampled in bricks_sampled:
            if bricks.check_duplicate(bo_bricks, brick_sampled) and bricks.check_duplicate(bricks_all, brick_sampled):
                bo_bricks.append(brick_sampled)
                cur_vector = brick_sampled.get_position_direction()
                bo_vectors.append(cur_vector)
            else:
                num_duplicated += 1
        print('#duplicates:', num_duplicated)

        bo_acqs = fun_negative_acquisition(np.array(bo_vectors))
        bo_ind = bo_acqs.argsort()[0]

        bricks_all.append(bo_bricks[bo_ind])
        X_all.append(bo_vectors[bo_ind])

        bo_bricks_copied = copy.deepcopy(bricks_)
        bo_bricks_copied.add(bo_bricks[bo_ind])

        cur_score = fun_evaluation(bo_bricks_copied)

        Y_all.append([cur_score])
        time_end_iteration = time.time()
        print('time consumed: {:.4f}'.format(time_end_iteration - time_start_iteration))

    ind_best = np.argmin(Y_all)
    bricks_all = [bricks_all[ind_best]]

#    print(X_all)
#    print(Y_all)
#    print(Y_all[ind_best])

    return bricks_all
