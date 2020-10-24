import numpy as np
import copy
import time

import brick
import rules
import utils_primitive


def convert_to_bricks(X, A):
    list_bricks = []
    for bx, ba in zip(X, A):
        brick_ = brick.Brick()
        brick_.set_position(bx[:3])
        brick_.set_direction(bx[3])

        list_bricks.append(brick_)

    bricks_ = Bricks(len(list_bricks))
    bricks_.bricks = list_bricks
    try:
        bricks_.validate_all()
    except:
        bricks_ = None

    return bricks_

def check_duplicate(bricks_, brick_):
    for cur_brick in bricks_:
        if np.all(cur_brick.get_position() == brick_.get_position()) and cur_brick.get_direction() == brick_.get_direction():
            return False
    return True

def get_connection_type(brick_1, brick_2):
    # brick_1 is a yardstick.
    list_rules = rules.LIST_RULES_2_4

    diff_direction = (brick_2.get_direction() + brick_1.get_direction()) % 2
    diff_position = (brick_2.get_position() - brick_1.get_position())[:2]

    if brick_1.get_direction() == 1:
        diff_position = [diff_position[1], diff_position[0]]
        diff_position = np.array(diff_position)

    ind = None
    num_ind = 0
    for rule in list_rules:
        if diff_direction == rule[1][0] and np.all(diff_position == np.array(rule[1][1])):
            ind = rule[0]
            num_ind += 1

    if not num_ind == 1:
        print(num_ind)
        print(diff_direction)
        print(diff_position)
        raise ValueError('Invalid connection type.')

    return ind

def _fun_validate_overlap(min_max_1, brick_2):
    vert_2 = brick_2.get_vertices()
    min_max_2 = utils_primitive.get_min_max_3d(vert_2)

    res = utils_primitive.check_overlap_3d(min_max_1, min_max_2)

    return res

def _fun_validate_contact(pos_1, vert_1, min_max_1, brick_2):
    pos_2 = brick_2.get_position()
    vert_2 = brick_2.get_vertices()

    if np.abs(pos_1[2] - pos_2[2]) == 1:
        min_max_2 = utils_primitive.get_min_max_3d(vert_2)

        res = utils_primitive.check_overlap_2d(min_max_1[:2], min_max_2[:2])
        if res: 
            return 1
    return 0

def fun_validate_overlap_outer(brick_1, list_bricks):
    vert_1 = brick_1.get_vertices()
    min_max_1 = utils_primitive.get_min_max_3d(vert_1)

    results = [_fun_validate_overlap(min_max_1, elem) for elem in list_bricks]

    if np.any(results):
        raise ValueError('Occur a brick overlap.')

def fun_validate_contact_outer(brick_1, list_bricks):
    if len(list_bricks) == 0:
        return

    pos_1 = brick_1.get_position()
    vert_1 = brick_1.get_vertices()
    min_max_1 = utils_primitive.get_min_max_3d(vert_1)

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
        self.adjacency_matrix = np.array([])
        self.degree_matrix = np.array([])
        self.connection_types = []

    def _validate_overlap(self):
        len_bricks = self.get_length()
        list_bricks = self.get_bricks()

        [fun_validate_overlap_outer(brick_1, list_bricks[ind_1+1:]) for ind_1, brick_1 in enumerate(list_bricks)]

    def _check_reachibility(self):
        len_bricks = self.get_length()
        reached = np.zeros(len_bricks)

        self.compute_adjacency_degree_matrices()
        A = self.get_adjacency_matrix()
        D = self.get_degree_matrix()

        for ind_1 in range(0, len_bricks):
            for ind_2 in range(0, len_bricks):
                if ind_1 > ind_2:
                    A[ind_1, ind_2] = 0

        def check_contacts(ind_):
            for ind_elem, elem in enumerate(A[ind_]):
                if elem == 1:
                    reached[ind_elem] = 1
                    check_contacts(ind_elem)

        check_contacts(0)
        reached[0] = 1
        return reached

    def _validate_contact(self):
        len_bricks = self.get_length()
        list_bricks = self.get_bricks()

        if len_bricks == 1:
            return
        else:
            reached = self._check_reachibility()
            if not np.sum(reached) == len_bricks:
                raise ValueError('Do not have a contact.')

            '''
            results = [fun_validate_contact_outer(brick_1, list_bricks) for brick_1 in list_bricks]
            summation = np.sum(results)
            summation /= 2

            if (self.get_length() - 1) > summation:
                raise ValueError('Do not have a contact.')
            '''

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

    def add(self, brick_,
        compute_adjacency_matrix=False,
        validate_all=False
    ):
        if self.get_length() < self.max_bricks:
            self.validate_brick(brick_)
            self.bricks.append(brick_)

            if compute_adjacency_matrix:
                self.compute_adjacency_degree_matrices()

            if validate_all:
                self.validate_all()
        else:
            raise ValueError('Exceed the maximum number of bricks.')

    def get_bricks(self):
        return self.bricks

    def get_length(self):
        return len(self.bricks)

    def get_connection_types(self):
        return self.connection_types

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def get_degree_matrix(self):
        return self.degree_matrix

    def get_vertices(self):
        bricks_ = self.get_bricks()

        vertices_all = []
        for brick_ in bricks_:
            vertices_all += list(brick_.get_vertices())

        vertices_all = np.array(vertices_all)
        vertices_all = np.unique(vertices_all, axis=0)
        
        return vertices_all

    def get_positions(self):
        bricks_ = self.get_bricks()

        positions_all = []
        for brick_ in bricks_:
            cur_pos = brick_.get_position()
            cur_dir = brick_.get_direction()

            positions_all.append([cur_pos[0], cur_pos[1], cur_pos[2], cur_dir])
        return np.array(positions_all)

    def _validate_bricks(self, bricks_):
        bricks_validated = []
        for brick_ in bricks_:
            cur_bricks = copy.deepcopy(self)

            try:
                cur_bricks.add(brick_)
                bricks_validated.append(brick_)
            except Exception as e:
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
                    new_brick.set_position(cur_position + np.concatenate((np.array(trans), [-1 * new_brick.height])))
                    new_brick.set_direction((cur_direction + direction) % 2)
                    if new_brick.get_position()[2] >= 0:
                        new_bricks.append(new_brick)

        new_bricks = self._validate_bricks(new_bricks)
        
        return new_bricks

    def sample_one(self):
        list_bricks = self.get_bricks()
        ind_brick = np.random.choice(self.get_length())
        brick_sampled = list_bricks[ind_brick]

        cur_position = brick_sampled.get_position()
        cur_direction = brick_sampled.get_direction()

        ind_rule = np.random.choice(len(rules.RULE_CONTACTS_2_4), p=rules.PROBS_CONTACTS_2_4)
        cur_rule = rules.RULE_CONTACTS_2_4[ind_rule]
        
        translations = cur_rule['translations']
        direction = cur_rule['direction']

        ind_trans = np.random.choice(len(translations))
        trans = translations[ind_trans]

        new_bricks = []

        if True:
#        for trans in translations:
            # upper
            new_brick = copy.deepcopy(brick_sampled)
            new_brick.set_position(cur_position + np.concatenate((np.array(trans), [new_brick.height])))
            new_brick.set_direction((cur_direction + direction) % 2)
            if new_brick.get_position()[2] >= 0:
                new_bricks.append(new_brick)

            # lower
            new_brick = copy.deepcopy(brick_sampled)
            new_brick.set_position(cur_position + np.concatenate((np.array(trans), [-1 * new_brick.height])))
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

    def compute_adjacency_degree_matrices(self):
        bricks_ = self.get_bricks()
        len_bricks = self.get_length()
        connection_types = []

        A = np.zeros((len_bricks, len_bricks))
        D = np.zeros((len_bricks, len_bricks))

        for ind_1, brick_1 in enumerate(bricks_):
            connection_type = []
            for ind_2, brick_2 in enumerate(bricks_):
                if ind_1 == ind_2:
                    continue

                pos_1 = brick_1.get_position()
                pos_2 = brick_2.get_position()
                vert_1 = brick_1.get_vertices()
                vert_2 = brick_2.get_vertices()
                min_max_1 = utils_primitive.get_min_max_3d(vert_1)
                min_max_2 = utils_primitive.get_min_max_3d(vert_2)

                if np.abs(pos_1[2] - pos_2[2]) == 1 and utils_primitive.check_overlap_2d(min_max_1[:2], min_max_2[:2]) == 1:
                    A[ind_1, ind_2] = 1
                    conn = get_connection_type(bricks_[ind_1], bricks_[ind_2])
                    connection_type.append(conn)
                    D[ind_1, ind_1] += 1

            connection_types.append(connection_type)

        self.adjacency_matrix = A
        self.degree_matrix = D
        self.connection_types = connection_types
        if not len(self.get_connection_types()) == self.get_length():
            raise ValueError('Lengths are different.')

        return

    def get_graph(self):
        self.compute_adjacency_degree_matrices()

        X = self.get_positions()
        A = self.get_adjacency_matrix()
        D = self.get_degree_matrix()

        return X, A, D


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
            copy_bricks.add(possible_brick, compute_adjacency_matrix=False, validate_all=False)

            X, A, D = copy_bricks.get_graph()
            connection_types = copy_bricks.get_connection_types()

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

