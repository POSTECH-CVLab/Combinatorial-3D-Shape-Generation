import brick
import bricks
import dataset_common


def sofa_1():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 8 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - 2 * i, j * 6 + 2, 5 + (i % 2 == 0)])
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
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 2 + 4, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([7, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 3, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 11])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 3, 12 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 15])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 3 + 1, j * 10, 10 - (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, j * 10, 9 - i])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2 + 1, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([1, 1, 3 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, 1, 3 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([1, 10, 3 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, 10, 3 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_2():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([5, i * 8 + 1, 3 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 2, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 3, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 10, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_heart():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)

    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 4 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([6, i * 10, 3 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 1, j * 8 + 1, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 3, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 5, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 2 - 1, j * 4 + 1,2 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 10, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 3, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 10 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 6 + 2, 13])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_3():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, 1, i])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 4 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 4 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 8 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(4):
                brick_ = brick.Brick()
                brick_.set_position([i * 2 + 5, j * 8 + 1, 3 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6 - i * 2, j * 6 + 2, 4 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 4 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, j * 4 + 3, 6 + i])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, 9, 3 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 10, 6 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_4():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i, 0, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 3 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 6, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 6, 3 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 9, 3 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 10, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 12, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 12, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 12, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 2 + 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2 + 2, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


def sofa_5():
    bricks_ = bricks.Bricks(150)

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1,i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 10, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-3,i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-3,i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 10, 4 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2,i * 6 + 2, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):    
        brick_ = brick.Brick()
        brick_.set_position([3, i * 8 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-2, i * 2,6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):    
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 2 + 4, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-2, i * 2 + 8,6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 - 3, j * 4 + 3, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):    
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 3, 5, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_6():
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
        
    for i in range(3):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 5, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 2, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 5, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 11 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 10 - 1, 5, 14])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 3 - 2 * j, 15 - (j % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 1, 13 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 6, 14])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 15])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_7():
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
    
    for i in range(12):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([25, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(12):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([24 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1,7 + j])
            brick_.set_direction((j % 2 == 1))
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([25, i * 4 + 1,7 + j])
            brick_.set_direction((j % 2 == 1))
            list_brick_.append(brick_)
    
    for i in range(13):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 11 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 10, 6 + (i % 2 == 1), 10 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 14 + 5, 7, 10 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def sofa_8():
    
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_9():
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
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 2, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_10():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16 - 2 * i,j * 6 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([17, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2 + 8, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 16, j * 10, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 4, j * 10, 4 - i])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 10, j * 10, 3 + i])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 16, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_11():
    bricks_ = bricks.Bricks(100)
    
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
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 6, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 4 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i + 10, 3, 4 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_12():
    bricks_ = bricks.Bricks(100)
    
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
    
    for i in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 - 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 7, j * 4 - 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, -2, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 + 2, -3, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 + 2, 6, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_13():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 8, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 7 - 2 * i, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 0, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 3, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_14():
    bricks_ = bricks.Bricks(100)
    
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 + 7, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 8 + 2, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_15():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 3 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 10 - 1, i * 2 + 1, 3 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8, 4, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 + 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 3, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 0, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, j * 4, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_16():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - i * 2, j * 6 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([9, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, j * 10, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 3, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2 + 8, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    brick_ = brick.Brick()
    brick_.set_position([4, 9, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)
                
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_17():
    bricks_ = bricks.Bricks(100)
    
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
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 4 + 1, 6 - 2 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_18():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 5 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 4, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 5, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 + 1, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_19():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 8, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 7 - 2 * i, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 8, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([5, i * 4 + 2, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([5, 4, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_20():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16 - 2 * i,j * 6 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([17, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            for k in range(4):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2 + 8, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 16, j * 10, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 18 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_21():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16 - 2 * i,j * 6 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([17, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            for k in range(4):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2 + 8, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 16, j * 10, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 18 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 2 + 8, 11])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_22():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 8, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 7 - 2 * i, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 0, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 3, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, 0, 9 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 1, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_23():
    bricks_ = bricks.Bricks(100)
    
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 + 7, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 8 + 2, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 7, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 + 2, 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_24():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 3 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 10 - 1, i * 2 + 1, 3 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8, 4, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 + 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 3, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 0, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 4, 2 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, 0, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_25():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - i * 2, j * 6 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([9, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, j * 10, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 3, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2 + 8, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 2, 9, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, 6 - j * 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_26():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 5 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 4, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 5, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 + 1, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_27():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4 - 2 * i,j * 2 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 5 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 4, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 5, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def sofa_28():
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
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 2, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 6, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_
    
def sofa_29():
    bricks_ = bricks.Bricks(100)
    
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
    
    for i in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 - 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 7, j * 4 - 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, -2, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 + 2, -3, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 8 + 2, 6, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, j * 4 - 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 7, j * 4 - 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_


if __name__ == '__main__':
    # Removed sofa_1 and sofa_2, and then renamed all.
    list_bricks_ = [
        sofa_heart(),
        sofa_1(),
        sofa_2(),
        sofa_3(),
        sofa_4(),
        sofa_5(),
        sofa_6(),
        sofa_7(),
        sofa_8(),
        sofa_9(),
        sofa_10(),
        sofa_11(),
        sofa_12(),
        sofa_13(),
        sofa_14(),
        sofa_15(),
        sofa_16(),
        sofa_17(),
        sofa_18(),
        sofa_19(),
        sofa_20(),
        sofa_21(),
        sofa_22(),
        sofa_23(),
        sofa_24(),
        sofa_25(),
        sofa_26(),
        sofa_27(),
        sofa_28(),
        sofa_29(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_SOFA)

