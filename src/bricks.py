import numpy as np
import copy
import time

import rules
import utils


def check_duplicate(bricks_, brick_):
    for cur_brick in bricks_:
        if np.all(cur_brick.get_position() == brick_.get_position()) and cur_brick.get_direction() == brick_.get_direction():
            return False
    return True

def _fun_validate_overlap(min_max_1, brick_2):
    vert_2 = brick_2.get_vertices()
    min_max_2 = utils.get_min_max_3d(vert_2)

    res = utils.check_overlap_3d(min_max_1, min_max_2)

    return res

def _fun_validate_contact(pos_1, vert_1, min_max_1, brick_2):
    pos_2 = brick_2.get_position()
    vert_2 = brick_2.get_vertices()

    if np.abs(pos_1[2] - pos_2[2]) == 1:
        min_max_2 = utils.get_min_max_3d(vert_2)

        res = utils.check_overlap_2d(min_max_1[:2], min_max_2[:2])
        if res: 
            return 1
    return 0

def fun_validate_overlap_outer(brick_1, list_bricks):
    vert_1 = brick_1.get_vertices()
    min_max_1 = utils.get_min_max_3d(vert_1)

    results = [_fun_validate_overlap(min_max_1, elem) for elem in list_bricks]

    if np.any(results):
        raise ValueError('Occur a brick overlap.')

def fun_validate_contact_outer(brick_1, list_bricks):
    if len(list_bricks) == 0:
        return

    pos_1 = brick_1.get_position()
    vert_1 = brick_1.get_vertices()
    min_max_1 = utils.get_min_max_3d(vert_1)

    results = [_fun_validate_contact(pos_1, vert_1, min_max_1, elem) for elem in list_bricks]

    if int(np.sum(results)) == 0:
        raise ValueError('Do not have a contact.')

    return np.sum(results)

def fun_validate_origin_outer(brick_):
    pos = brick_.get_position()
    if pos[2] < 0:
        raise ValueError('Brick is located under an origin surface.')


class Bricks(object):
    def __init__(self, max_bricks):
        self.max_bricks = max_bricks
        self.bricks = []

    def _validate_overlap(self):
        len_bricks = self.get_length()
        list_bricks = self.get_bricks()

        [fun_validate_overlap_outer(brick_1, list_bricks[ind_1+1:]) for ind_1, brick_1 in enumerate(list_bricks)]

    def _validate_contact(self):
        len_bricks = self.get_length()
        list_bricks = self.get_bricks()

        if len_bricks == 1:
            return
        else:
            results = [fun_validate_contact_outer(brick_1, list_bricks) for brick_1 in list_bricks]
            summation = np.sum(results)
            summation /= 2

            if (self.get_length() - 1) > summation:
                raise ValueError('Do not have a contact.')

    def _validate_origin(self):
        bricks_ = self.get_bricks()
        for brick_ in bricks_:
            fun_validate_origin_outer(brick_)

    def _validate_length(self):
        if self.get_length() > self.max_bricks:
            raise ValueError('Exceed the maximum number of bricks.')

    def validate_all(self):
        self._validate_overlap()
        self._validate_contact()
        self._validate_origin()
        self._validate_length()

    def validate_brick(self, brick_):
        fun_validate_overlap_outer(brick_, self.get_bricks())
        fun_validate_contact_outer(brick_, self.get_bricks())
        fun_validate_origin_outer(brick_)

    def add(self, brick_):
        if self.get_length() < self.max_bricks:
            self.validate_brick(brick_)
            self.bricks.append(brick_)
        else:
            raise ValueError('Exceed the maximum number of bricks.')

    def get_bricks(self):
        return self.bricks

    def get_length(self):
        return len(self.bricks)

    def get_vertices(self):
        bricks_ = self.get_bricks()

        vertices_all = []
        for brick_ in bricks_:
            vertices_all += list(brick_.get_vertices())

        vertices_all = np.array(vertices_all)
        vertices_all = np.unique(vertices_all, axis=0)
        
        return vertices_all

    def _validate_bricks(self, bricks_):
        bricks_validated = []
        for brick_ in bricks_:
            cur_bricks = copy.deepcopy(self)

            try:
                cur_bricks.add(brick_)
                bricks_validated.append(brick_)
            except:
                pass

        return bricks_validated

    def get_possible_contacts(self):
        bricks = self.get_bricks()
        new_bricks = []

        for brick_ in bricks:
            cur_position = brick_.get_position()
            cur_direction = brick_.get_direction()

            for rule in rules.RULE_CONTACTS_2_4:
                translations = rule['translations']
                direction = rule['direction']
                
                for trans in translations:
                    # upper
                    new_brick = copy.deepcopy(brick_)
                    new_brick.set_position(cur_position + np.concatenate((np.array(trans), [new_brick.height])))
                    new_brick.set_direction((cur_direction + direction) % 2)
                    if new_brick.get_position()[2] >= 0:
                        new_bricks.append(new_brick)

                    # lower
                    new_brick = copy.deepcopy(brick_)
                    new_brick.set_position(cur_position + np.concatenate((np.array(trans), [-1.0 * new_brick.height])))
                    new_brick.set_direction((cur_direction + direction) % 2)
                    if new_brick.get_position()[2] >= 0:
                        new_bricks.append(new_brick)

        new_bricks = self._validate_bricks(new_bricks)
        
        return new_bricks

    def sample_one(self):
        bricks = self.get_bricks()
        brick_sampled = np.random.choice(bricks)

        cur_position = brick_sampled.get_position()
        cur_direction = brick_sampled.get_direction()

        cur_rule = np.random.choice(rules.RULE_CONTACTS_2_4, p=rules.PROBS_CONTACTS_2_4)
        
        translations = cur_rule['translations']
        direction = cur_rule['direction']
        ind_trans = np.random.choice(len(translations))
        trans = translations[ind_trans]

        new_bricks = []

        if True:
            # upper
            new_brick = copy.deepcopy(brick_sampled)
            new_brick.set_position(cur_position + np.concatenate((np.array(trans), [new_brick.height])))
            new_brick.set_direction((cur_direction + direction) % 2)
            if new_brick.get_position()[2] >= 0:
                new_bricks.append(new_brick)

            # lower
            new_brick = copy.deepcopy(brick_sampled)
            new_brick.set_position(cur_position + np.concatenate((np.array(trans), [-1.0 * new_brick.height])))
            new_brick.set_direction((cur_direction + direction) % 2)
            if new_brick.get_position()[2] >= 0:
                new_bricks.append(new_brick)

        new_bricks = self._validate_bricks(new_bricks)

        if len(new_bricks) == 0:
            return None
        else:
            return np.random.choice(new_bricks)

    def sample(self, num_samples=None):
        if num_samples is None:
            num_samples = 1

        possible_bricks = []
        while len(possible_bricks) <= num_samples:
            brick_sampled = self.sample_one()

            if brick_sampled is not None and check_duplicate(possible_bricks, brick_sampled):
                possible_bricks.append(brick_sampled)

        return possible_bricks


if __name__ == '__main__':
    import brick
    import time

    brick1 = brick.Brick()
    brick2 = brick.Brick()
    brick3 = brick.Brick()

    brick1.set_position([0, 0, 0])
    brick1.set_direction(0)

    brick2.set_position([1, -2, 1])
    brick2.set_direction(1)

    brick3.set_position([-1, -3, 1])
    brick3.set_direction(0)

    bricks_ = Bricks(6)
    bricks_.add(brick1)
    bricks_.add(brick2)

    brick1 = brick.Brick()

    brick1.set_position([0, 0, 0])
    brick1.set_direction(0)

    bricks_ = Bricks(6)
    bricks_.add(brick1)

    bricks_._validate_overlap()
    bricks_.get_possible_contacts()

    def stack(bricks):
        possible_bricks = bricks.get_possible_contacts()
        new_bricks = []

        for possible_brick in possible_bricks:
            copy_bricks = copy.deepcopy(bricks)
            copy_bricks.add(possible_brick)

            new_bricks.append(copy_bricks)

        return new_bricks
    
    list_bricks = [bricks_]

    for ind in range(0, 4):
        time_start = time.time()
        new_list_bricks = []

        num_bricks = 0
        for bricks_ in list_bricks:
            cur_list_bricks = stack(bricks_)
            num_bricks += len(cur_list_bricks)
            if ind < 3:
                new_list_bricks += cur_list_bricks

        list_bricks = new_list_bricks
        print(num_bricks)
        time_end = time.time()
        print('time consumed: ', time_end - time_start, 'sec.')

