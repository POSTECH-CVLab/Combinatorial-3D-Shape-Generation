import numpy as np
from datetime import datetime
import time
import os
import argparse

from geometric_primitives import bricks
from geometric_primitives import utils as utils_gp

import bo
import wrappers
import utils
import constants

parser = argparse.ArgumentParser()
parser.add_argument('--ind_class', type=int)
parser.add_argument('--ind_target', type=int)
parser.add_argument('--use_stability', action='store_true')
parser.add_argument('--use_rollback', action='store_true')
args = parser.parse_args()

print('ind_class', args.ind_class, type(args.ind_class))
print('ind_target', args.ind_target, type(args.ind_target))
print('use_stability', args.use_stability, type(args.use_stability))
print('use_rollback', args.use_rollback, type(args.use_rollback))

use_stability = args.use_stability
use_rollback = args.use_rollback

str_exp = 'assembly_bo_overlap'

if use_stability:
    import stability

    str_exp += '_'
    str_exp += 'w_stability'


if use_rollback:
    str_exp += '_'
    str_exp += 'w_rollback'

num_bo_init = 10
num_bo_acq = 10

time_bo_acq = 1.0

ind_class = args.ind_class
ind_target = args.ind_target


str_label = 'label{:02}'.format(ind_class)
str_target = '{}_{:02}.npy'.format(str_label, ind_target)
print(str_target)

target = np.load(os.path.join(constants.PATH_DATASET, str_target), allow_pickle=True)
target = target[()]
print(target.get_length())
target = utils_gp.align_bricks_to_origin(target)

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

                dist_0, dist_1 = utils_gp.get_dists(vert_source, vert_target)

                if dist_0 > 0 and dist_1 > 0:
                    list_overlaps.append(dist_0 * dist_1)

    score_overlap = np.max(list_overlaps) * -1.0
    print(score_overlap)

    if use_stability:
        time_to_be_stable = stability.get_time_to_be_stable(bricks_)
        print('Time to be stable:', time_to_be_stable)
        score_stability = (time_to_be_stable - 200.0)
        score_stability = np.tanh(score_stability / 200.0) * 1.0
        return score_overlap, score_stability
    else:
        return score_overlap


if __name__ == '__main__':
    time_start_all = time.time()

    fun_evaluation = lambda bricks_: evaluate(bricks_)
    
    str_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    str_path = os.path.join(constants.PATH_BRICKS, str_time)

    bricks_initial = bricks.Bricks(2000)
    bricks_initial.add(target.get_bricks()[0])

    bricks_bo = wrappers.bo_all(bricks_initial, num_bricks, num_bo_acq, num_bo_init, time_bo_acq, fun_evaluation, str_path, is_roll_back=use_rollback, is_multi=use_stability)

    time_end_all = time.time()
    print('Overall time: {:.4f} sec.'.format(time_end_all - time_start_all))

    ind_bricks = 1
    utils.save_results(
        os.path.join(constants.PATH_RESULTS, '{}_class_{:02}_target_{:02}'.format(str_exp, ind_class, ind_target)),
        '{}_class_{}_bricks_{}_init_{}_acq_{}_datetime_{}_round_{}'.format(str_exp, ind_class, num_bricks, num_bo_init, num_bo_acq, str_time, ind_bricks),
        fun_evaluation,
        bricks_bo,
        str_exp,
        use_stability
    )
