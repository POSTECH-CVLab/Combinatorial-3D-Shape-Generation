import numpy as np
import pybullet
import pybullet_data
import time

#import brick
#import bricks
#import utils


def get_time_to_be_stable(bricks_):
    unit_size = 0.10
    num_iters = 10000
    num_forces = 200

    mass = 10
    mass_link = 1
    gravity = -20

    epsilon = 1e-3

    id_client = pybullet.connect(pybullet.GUI)
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

    plane = pybullet.createCollisionShape(pybullet.GEOM_PLANE)
    id_plane = pybullet.createMultiBody(0, plane)

    useMaximalCoordinates = True

    id_box = pybullet.createCollisionShape(
        pybullet.GEOM_BOX,
        halfExtents=[unit_size * 2.0, unit_size * 4.0, unit_size * 1.0]
    )

    list_bricks = bricks_.get_bricks()
    len_bricks = bricks_.get_length()
    print('Length: {}'.format(len_bricks))

    force = 500.0 * len_bricks
    brick_prev = list_bricks[0]

    visualShapeId = -1
    position_base = list(brick_prev.get_position())
    direc_base = int(brick_prev.get_direction())
    orientation_base = [0, 0, direc_base, 1]
    anistropicFriction = [1, 1, 1]

    link_masses = []
    linkCollisionShapeIndices = []
    linkVisualShapeIndices = []
    linkPositions = []
    linkOrientations = []
    linkInertialFramePositions = []
    linkInertialFrameOrientations = []
    indices = []
    jointTypes = []
    axis = []

    for ind_brick, brick_ in enumerate(list_bricks[1:]):
        trans = brick_.get_position() - brick_prev.get_position()
        trans = trans * unit_size * 2
        print(brick_.get_position(), brick_prev.get_position())
        print(trans)

        direc = (brick_.get_direction() - brick_prev.get_direction())

        if direc == -1:
            trans = [trans[1], trans[0] * -1, trans[2]]
        elif direc == 1:
            trans = trans
        else:
            if brick_.get_direction() == 0:
                trans = trans
            else:
                trans = [trans[1], trans[0] * -1, trans[2]]

        link_masses.append(mass_link)
        linkCollisionShapeIndices.append(id_box)
        linkVisualShapeIndices.append(-1)
        linkPositions.append(list(trans))
        linkOrientations.append([0, 0, int(direc), 1])
        linkInertialFramePositions.append([0, 0, 0])
        linkInertialFrameOrientations.append([0, 0, 0, 1])
        indices.append(ind_brick)
        jointTypes.append(pybullet.JOINT_FIXED)
        axis.append([0, 0, 1])

        brick_prev = brick_

    id_body = pybullet.createMultiBody(
        mass,
        id_box,
        visualShapeId,
        position_base,
        orientation_base,
        linkMasses=link_masses,
        linkCollisionShapeIndices=linkCollisionShapeIndices,
        linkVisualShapeIndices=linkVisualShapeIndices,
        linkPositions=linkPositions,
        linkOrientations=linkOrientations,
        linkInertialFramePositions=linkInertialFramePositions,
        linkInertialFrameOrientations=linkInertialFrameOrientations,
        linkParentIndices=indices,
        linkJointTypes=jointTypes,
        linkJointAxis=axis,
        useMaximalCoordinates=useMaximalCoordinates
    )

    pybullet.setGravity(0, 0, gravity)
    pybullet.setRealTimeSimulation(0)

    pybullet.changeDynamics(id_body, -1, lateralFriction=2, anisotropicFriction=anistropicFriction)
    pybullet.getNumJoints(id_body)

    for ind in range(0, pybullet.getNumJoints(id_body)):
        pybullet.changeDynamics(id_body, ind, lateralFriction=2, anisotropicFriction=anistropicFriction)


    for ind in range(0, num_iters):
        pos, ori = pybullet.getBasePositionAndOrientation(id_body)

        if ind < num_forces:
            if ind % 8 == 0:
                sign = [1.0, 1.0]
            elif ind % 8 == 2:
                sign = [1.0, -1.0]
            elif ind % 8 == 4:
                sign = [-1.0, -1.0]
            elif ind % 8 == 6:
                sign = [-1.0, 1.0]
            else:
                sign = [0.0, 0.0]

            pybullet.applyExternalForce(
                objectUniqueId=id_body,
                linkIndex=-1,
                forceObj=[force * sign[0], force * sign[1], 0.0],
                posObj=[0, 0, 0],
                flags=pybullet.WORLD_FRAME
            )
        else:
            if np.linalg.norm(np.array(pos) - np.array(pos_prev), ord=2) < epsilon:
                break

        pos_prev = pos
        pybullet.stepSimulation()
        time.sleep(0.1 / num_iters)

    pybullet.disconnect(id_client)

    return ind
