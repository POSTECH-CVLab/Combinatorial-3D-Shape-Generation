import brick
import bricks
import dataset_common


def table_1():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([3, 1, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 1, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 -1, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 5, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 1, 5, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    # 4 * 4 Done
    
    
    """
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    """
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 3, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 6, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)        
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_2():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([3, 1, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 1, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 -1, 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 5, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 1, 5, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 3, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 3, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 1, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 5, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_3():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, -2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, -2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, 6, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 6, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 8, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 8, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 8, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 10, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, 10, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 8, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 4, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 6, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 10, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 4, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 8, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, -2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 6, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 10, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 8, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 8, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_4():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, -1, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 1, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -1, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 5, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 5, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 0, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 4, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 1, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 3, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 0, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 4, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, -1, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, 5, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 2, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_5():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, -2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, -4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, -2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -3, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 3, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, -4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, -2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, -2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_6():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -1, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 1, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, 0, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_7():
    bricks_ = bricks.Bricks(120)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, -1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, -1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([9, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([11, -1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([13, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([15, -1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([17, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 0, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 11, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([2, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 11, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([6, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, 1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([9, 11, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([10, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([10, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([10, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([10, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([10, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([11, 1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([12, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([12, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([12, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([12, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([12, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([13, 11, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([14, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([14, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([14, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([14, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([14, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([15, 1, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([16, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([16, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([16, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([16, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([16, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([17, 11, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 10, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 8, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 6, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 4, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([18, 2, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for ind in range(0, 8):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 7 - ind])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for ind in range(0, 8):
        brick_ = brick.Brick()
        brick_.set_position([18, 0, 7 - ind])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for ind in range(0, 8):
        brick_ = brick.Brick()
        brick_.set_position([0, 10, 7 - ind])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for ind in range(0, 8):
        brick_ = brick.Brick()
        brick_.set_position([18, 10, 7 - ind])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_8():
    bricks_ = bricks.Bricks(40)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, -1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, -2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 3, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([3, 5, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([1, 7, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 8, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 6, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 6, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, -2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([4, 8, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, -1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 3, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 7, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, 1, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([7, 5, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, -2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 8, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 6, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([8, 6, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_that_is_bench_like():
    bricks_ = bricks.Bricks(40)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 3, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 5, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 7, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 9, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 9, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 11, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 13, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 13, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 14, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 14, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_that_is_bridge_like():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-(i % 2 == 1), (i % 2 == 1), i])
        brick_.set_direction((i % 2 == 0))
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, 2, i * 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 1])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2, j * 2 + 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 2, j * 2 + 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 2, j * 2 + 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12, i * 2, j * 2 + 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([14, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16, i * 2, j * 2 + 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([20, i * 2, j * 2 + 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([21, 1, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([21, 1, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([20, i * 2, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 19, 1, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([20, i * 2, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_11():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 7, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_12():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 12, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_13():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
           
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6 - 2 * i,j * 2 + 2, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([3, 3, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 2, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1 , j * 2 + 1, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_14():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_15():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12 - 2 * i,j * 2 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 5 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 4 + 1, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([13, i * 4 + 1, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_16():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 6 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 5, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 5, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_17():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 6 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 8 + 1, 5 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_18():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, 3, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 3, 3 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_19():
    bricks_ = bricks.Bricks(80)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 1, 3 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_20():
    bricks_ = bricks.Bricks(80)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 8, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 7 - 2 * i, 4 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 6 + 1, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 + 2, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 6 + 1, 1])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_21():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
           
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6 - 2 * i,j * 2 + 2, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([3, j * 2 + 1, 4 - i])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 2, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1 , j * 2 + 1, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 8 - 1, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_22():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
           
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6 - 2 * i,j * 2 + 2, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 0, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 6, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 - 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 0, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 - 1, 3, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 0, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 6, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 - 1, 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 0, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 - 1, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 0, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 0])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_23():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12 - 2 * i,j * 2 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 5 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 4 + 1, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([13, i * 4 + 1, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([7, i * 4 + 1, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_24():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 3, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2 + 2, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2 + 1, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 1])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_25():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 6 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 10, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 8 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 10, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 4 + 3, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_26():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
           
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6 - 2 * i,j * 2 + 2, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([3, 3, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 2, 3, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1 , j * 2 + 1, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 2 + 1, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_27():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 6 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2, 5 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 3, 5 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_28():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 6 + 2, 6 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 6 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 8 + 1, 5 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2 + 2, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 + 3, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_29():
    bricks_ = bricks.Bricks(80)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 1, 3 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def table_30():
    bricks_ = bricks.Bricks(80)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 1, 3 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 6 - 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        table_1(),
        table_2(),
        table_3(),
        table_4(),
        table_5(),
        table_6(),
        table_7(),
        table_8(),
        table_that_is_bench_like(),
        table_that_is_bridge_like(),
        table_11(),
        table_12(),
        table_13(),
        table_14(),
        table_15(),
        table_16(),
        table_17(),
        table_18(),
        table_19(),
        table_20(),
        table_21(),
        table_22(),
        table_23(),
        table_24(),
        table_25(),
        table_26(),
        table_27(),
        table_28(),
        table_29(),
        table_30(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_TABLE)

