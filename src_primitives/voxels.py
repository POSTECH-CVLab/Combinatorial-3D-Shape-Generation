import numpy as np

import brick


class Voxel(brick.Brick):
    def __init__(self):
        super(Voxel, self).__init__(size_upper=(1, 1), size_lower=(1, 1), height=1)

class Voxels(object):
    def __init__(self):
        self.voxels = []

    def add(self, voxel_):
        self.voxels.append(voxel_)

    def get_voxels(self):
        return self.voxels

    def get_length(self):
        return len(self.voxels)

    def get_vertices(self):
        voxels_ = self.get_voxels()

        vertices_all = []
        for voxel_ in voxels_:
            vertices_all += list(voxel_.get_vertices())

        vertices_all = np.array(vertices_all)
        vertices_all = np.unique(vertices_all, axis=0)
        
        return vertices_all

    def get_positions(self):
        voxels_ = self.get_voxels()

        positions_all = []
        for voxel_ in voxels_:
            cur_pos = voxel_.get_position()
            cur_dir = voxel_.get_direction()

            positions_all.append([cur_pos[0], cur_pos[1], cur_pos[2], cur_dir])
        return np.array(positions_all)
