import numpy as np
from datetime import datetime
import time
import os

import bo
import bricks
import common
import normalize_bricks


str_exp = 'assembly_bo_overlap'
str_file = '{}.npy'.format(str_exp)

str_path_bricks = '../bricks'
#str_path_dataset = '../dataset-combi'
str_path_dataset = '../dataset'
str_path_results = '../results'

ind_class = 21
ind_target = 1

str_label = 'label{:02}'.format(ind_class)
str_target = '{}_{:02}.npy'.format(str_label, ind_target)
print(str_target)

target = np.load(os.path.join(str_path_dataset, str_target), allow_pickle=True)
target = target[()]
print(target.get_length())
target = normalize_bricks.align_to_origin(target)

num_bricks = int(target.get_length() * 0.9)


def evaluate(bricks_):
    list_bricks_target = target.get_bricks()
    list_bricks_ = bricks_.get_bricks()
    list_bricks_ = [list_bricks_[-1]]

    list_overlaps = [0.0]
    for brick_source in list_bricks_:
        pos_dir_source = brick_source.get_position_direction()

        for brick_target in list_bricks_target:
            pos_dir_target = brick_target.get_position_direction()

            if pos_dir_source[2] == pos_dir_target[2]:
                vert_source = brick_source.get_vertices()
                vert_target = brick_target.get_vertices()

                vert_source_0 = np.unique(vert_source[:, 0])
                vert_target_0 = np.unique(vert_target[:, 0])

                vert_source_1 = np.unique(vert_source[:, 1])
                vert_target_1 = np.unique(vert_target[:, 1])

                vert_source_0.sort()
                vert_source_1.sort()
                vert_target_0.sort()
                vert_target_1.sort()

                dist_0_all = np.maximum(vert_target_0[1] - vert_source_0[0], vert_source_0[1] - vert_target_0[0])
                dist_0_all = np.maximum(vert_target_0[1] - vert_target_0[0], dist_0_all)
                dist_0_all = np.maximum(vert_source_0[1] - vert_source_0[0], dist_0_all)

                dist_0 = (vert_source_0[1] - vert_source_0[0])\
                    + (vert_target_0[1] - vert_target_0[0])\
                    - dist_0_all

                dist_1_all = np.maximum(vert_target_1[1] - vert_source_1[0], vert_source_1[1] - vert_target_1[0])
                dist_1_all = np.maximum(vert_target_1[1] - vert_target_1[0], dist_1_all)
                dist_1_all = np.maximum(vert_source_1[1] - vert_source_1[0], dist_1_all)

                dist_1 = (vert_source_1[1] - vert_source_1[0])\
                    + (vert_target_1[1] - vert_target_1[0])\
                    - dist_1_all

                if dist_0 > 0 and dist_1 > 0:
                    list_overlaps.append(dist_0 * dist_1)

    score_ = np.max(list_overlaps) * -1.0
    print(score_)
    return score_


if __name__ == '__main__':
    time_start_all = time.time()

    fun_evaluation = lambda bricks_: evaluate(bricks_)

    num_bo_rounds = 3
    num_bo_init = 10
    num_bo_acq = 10

    time_bo_acq = 1.0
    
    str_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    str_path = os.path.join(str_path_bricks, str_time)

    bricks_initial = bricks.Bricks(2000)
    bricks_initial.add(target.get_bricks()[0])

    list_bricks_bo_w_rollback = common.bo_all(bricks_initial, num_bricks, num_bo_rounds, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, str_path, is_roll_back=True)
    list_bricks_bo_wo_rollback = common.bo_all(bricks_initial, num_bricks, num_bo_rounds, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, str_path, is_roll_back=False)
#    list_bricks_bo_wo_rollback = list_bricks_bo_w_rollback

    list_bricks_random = common.random_all(bricks_initial, num_bricks, num_bo_rounds)
    list_bricks_random_eval = common.random_eval_all(bricks_initial, num_bricks, num_bo_rounds, num_bo_acq + num_bo_init, fun_evaluation)

    time_end_all = time.time()
    print('overall time:', time_end_all - time_start_all, 'sec.')

    common.save_results(
        os.path.join('../results', '{}_class_{:02}_target_{:02}'.format(str_exp, ind_class, ind_target)),
        '{}_class_{}_bricks_{}_rounds_{}_init_{}_acq_{}_datetime_{}'.format(str_exp, ind_class, num_bricks, num_bo_rounds, num_bo_init, num_bo_acq, str_time),
        fun_evaluation,
        [list_bricks_random, list_bricks_random_eval, list_bricks_bo_w_rollback, list_bricks_bo_wo_rollback],
        ['random', 'random_eval', 'bo_w_rollback', 'bo_wo_rollback']
    )

