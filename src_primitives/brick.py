import numpy as np


class Brick(object):
    # TODO: position is on integer grid, it makes vertex coordinates to real numbers.
    def __init__(self, size_upper=[2, 4], size_lower=[2, 4], height=1):
        self.size_upper = np.array(size_upper)
        self.size_lower = np.array(size_lower)
        self.height = 1
        self.position = None
        self.direction = 0
        self.vertices = None

    def set_vertices(self):
        assert self.position is not None

        vertices = []
        signs = np.array([
            [1.0, 1.0],
            [1.0, -1.0],
            [-1.0, 1.0],
            [-1.0, -1.0],
        ])

        for elem in signs:
            size_lower = self.size_lower
            if self.get_direction() == 1:
                # TODO: make it smarter
                size_lower = np.array([size_lower[1], size_lower[0]])

            trans = elem * size_lower / 2
            trans = np.concatenate((trans, np.array([0.0])))
            vertices.append(self.get_position() + trans)

        for elem in signs:
            size_upper = self.size_upper
            if self.get_direction() == 1:
                size_upper = np.array([size_upper[1], size_upper[0]])

            trans = elem * size_upper / 2
            trans = np.concatenate((trans, np.array([float(self.height)])))
            vertices.append(self.get_position() + trans)

        vertices = np.array(vertices)
        self.vertices = np.array(vertices)

        assert len(self.vertices) == 8

    def get_vertices(self):
        return self.vertices

    def set_position(self, pos):
        assert len(pos) == 3

        self.position = np.array(pos)
        self.set_vertices()

    def get_position(self):
        return self.position

    def set_direction(self, direc):
        assert direc in [0, 1]

        self.direction = direc
        self.set_vertices()

    def get_direction(self):
        return self.direction

    def set_configuration(self, pos_direc):
        assert isinstance(pos_direc, dict)

        pos = pos_direc['position']
        direc = pos_direc['direction']

        self.set_position(pos)
        self.set_direction(direc)


if __name__ == '__main__':
    obj_brick = Brick()
    print(obj_brick)
    print(obj_brick.size_upper)
    print(obj_brick.size_lower)

    obj_brick.set_position([1, 2, 3])
    print(obj_brick.position)
    print(obj_brick.vertices)

    obj_brick.set_position([1, -2, 3])
    print(obj_brick.position)
    print(obj_brick.vertices)

    print(obj_brick.get_vertices())
    print(obj_brick.get_position())

    config = {
        'position': [1, 4, 2],
        'direction': 1
    }
    obj_brick.set_configuration(config)

    print(obj_brick.get_vertices())
    print(obj_brick.get_position())
    print(obj_brick.get_direction())

