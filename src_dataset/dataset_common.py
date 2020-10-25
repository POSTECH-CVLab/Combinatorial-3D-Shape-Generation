import time
import os

from geometric_primitives import utils as utils_gp


STR_COMBI_DATASET = 'dataset'
STR_PATH_COMBI_DATASET = os.path.join('../', STR_COMBI_DATASET)

STR_LABEL_PARALLEL = 'label01'
STR_LABEL_PERPENDICULAR = 'label02'

STR_LABEL_BAR = 'label11'
STR_LABEL_LINE = 'label12'
STR_LABEL_PLATE = 'label13'
STR_LABEL_WALL = 'label14'
STR_LABEL_CUBOID = 'label15'
STR_LABEL_SQUAREPYRAMID = 'label16'

STR_LABEL_BENCH = 'label21'
STR_LABEL_SOFA = 'label22'
STR_LABEL_CUP = 'label23'
STR_LABEL_HOLLOW = 'label24'
STR_LABEL_TABLE = 'label25'
STR_LABEL_CAR = 'label26'

STR_LABEL_RANDOM = 'random'

LIST_STR_LABELS = [
    STR_LABEL_PARALLEL, # 0
    STR_LABEL_PERPENDICULAR, # 1
    STR_LABEL_BAR, # 2
    STR_LABEL_LINE, # 3
    STR_LABEL_PLATE, # 4
    STR_LABEL_WALL, # 5
    STR_LABEL_CUBOID, # 6
    STR_LABEL_SQUAREPYRAMID, # 7
    STR_LABEL_BENCH, # 8
    STR_LABEL_SOFA, # 9
    STR_LABEL_CUP, # 10
    STR_LABEL_HOLLOW, # 11
    STR_LABEL_TABLE, # 12
    STR_LABEL_CAR, # 13
    STR_LABEL_RANDOM, # 14
]


def create_bricks(list_bricks, str_label):
    if not os.path.exists(STR_PATH_COMBI_DATASET):
        os.mkdir(STR_PATH_COMBI_DATASET)

    print('[{}] # of brick combinations: {}'.format(str_label, len(list_bricks)))

    for ind_bricks_, bricks_ in enumerate(list_bricks):
        print('Creating bricks {}'.format(ind_bricks_ + 1))

        utils_gp.save_bricks(bricks_, STR_PATH_COMBI_DATASET, str_file='{}_{:02}'.format(str_label, ind_bricks_+1))
        time.sleep(1)
