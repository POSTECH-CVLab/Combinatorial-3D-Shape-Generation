import numpy as np
import copy
from bayeso.gp import gp
from bayeso import acquisition
import time

import bricks

str_cov = 'matern52'


def _optimize_objective(fun_acquisition, X_train, Y_train, X_test, cov_X_X, inv_cov_X_X, hyps):
    X_test = np.atleast_2d(X_test)
    pred_mean, pred_std, _ = gp.predict_test_(X_train, Y_train, X_test, cov_X_X, inv_cov_X_X, hyps, str_cov=str_cov, prior_mu=None, debug=False)
    acquisitions = fun_acquisition(pred_mean=pred_mean.flatten(), pred_std=pred_std.flatten(), Y_train=Y_train)

    return acquisitions

def get_weights():
    bw = np.random.uniform(size=2)
    bw[0] = 0.8 + bw[0] * 0.1
    bw[1] = bw[1] * 0.1

    bw /= np.linalg.norm(bw, ord=1)
    return bw

def optimize(fun_evaluation, bricks_, num_bricks, num_init, time_bo_acq, is_multi):
    bricks_all = bricks_.sample(num_init)

    X_all = []
    Y_all = []

    for cur_brick in bricks_all:
        bricks_copied = copy.deepcopy(bricks_)
        bricks_copied.add(cur_brick)

        if is_multi:
            bw = get_weights()

            cur_score_1, cur_score_2 = fun_evaluation(bricks_copied)
            Y_all.append([cur_score_1, cur_score_2, bw[0] * cur_score_1 + bw[1] * cur_score_2])
        else:
            cur_score = fun_evaluation(bricks_copied)
            Y_all.append([cur_score])

        cur_vector = cur_brick.get_position_direction()

        X_all.append(cur_vector)

    while len(bricks_all) <= num_init + num_bricks:
        print('Iteration', len(bricks_all))
        # TODO: you should double-check this scope carefully.

        time_start_iteration = time.time()

        fun_acquisition = acquisition.ucb

        if is_multi:
            cov_X_X_1, inv_cov_X_X_1, hyps_1 = gp.get_optimized_kernel(
                np.array(X_all),
                np.array(Y_all)[:, 0][..., np.newaxis],
                None, str_cov, debug=False)

            cov_X_X_2, inv_cov_X_X_2, hyps_2 = gp.get_optimized_kernel(
                np.array(X_all),
                np.array(Y_all)[:, 1][..., np.newaxis],
                None, str_cov, debug=False)

            fun_negative_acquisition_1 = lambda X_test: -1.0 * _optimize_objective(fun_acquisition, np.array(X_all), np.array(Y_all)[:, 0][..., np.newaxis], X_test, cov_X_X_1, inv_cov_X_X_1, hyps_1)
            fun_negative_acquisition_2 = lambda X_test: -1.0 * _optimize_objective(fun_acquisition, np.array(X_all), np.array(Y_all)[:, 1][..., np.newaxis], X_test, cov_X_X_2, inv_cov_X_X_2, hyps_2)
        else:
            cov_X_X, inv_cov_X_X, hyps = gp.get_optimized_kernel(
                np.array(X_all),
                np.array(Y_all),
                None, str_cov, debug=False)

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

        print('#Samples:', len(bricks_sampled))

        num_duplicated = 0
        for brick_sampled in bricks_sampled:
            if bricks.check_duplicate(bo_bricks, brick_sampled) and bricks.check_duplicate(bricks_all, brick_sampled):
                bo_bricks.append(brick_sampled)
                cur_vector = brick_sampled.get_position_direction()
                bo_vectors.append(cur_vector)
            else:
                num_duplicated += 1

        print('#Duplicates:', num_duplicated)

        if is_multi:
            bo_acqs_1 = fun_negative_acquisition_1(np.array(bo_vectors))
            bo_acqs_2 = fun_negative_acquisition_2(np.array(bo_vectors))

            bw = get_weights()

            bo_acqs = bw[0] * bo_acqs_1 + bw[1] * bo_acqs_2
        else:
            bo_acqs = fun_negative_acquisition(np.array(bo_vectors))

        bo_ind = bo_acqs.argsort()[0]

        bricks_all.append(bo_bricks[bo_ind])
        X_all.append(bo_vectors[bo_ind])

        bo_bricks_copied = copy.deepcopy(bricks_)
        bo_bricks_copied.add(bo_bricks[bo_ind])

        if is_multi:
            cur_score_1, cur_score_2 = fun_evaluation(bo_bricks_copied)
            Y_all.append([cur_score_1, cur_score_2, bw[0] * cur_score_1 + bw[1] * cur_score_2])
        else:
            cur_score = fun_evaluation(bo_bricks_copied)
            Y_all.append([cur_score])

        time_end_iteration = time.time()
        print('Time consumed: {:.4f}'.format(time_end_iteration - time_start_iteration))

    if is_multi:
        ind_best = np.argmin(np.array(Y_all)[:, 0])
    else:
        ind_best = np.argmin(Y_all)

    bricks_all = [bricks_all[ind_best]]

#    print(X_all)
#    print(Y_all)
#    print(Y_all[ind_best])

    return bricks_all
