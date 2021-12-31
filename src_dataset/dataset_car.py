from geometric_primitives import brick
from geometric_primitives import bricks

import dataset_common


def car_demo():
    bricks_ = bricks.Bricks(150, '0')

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''  
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, 7, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 9, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 10, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, j * 8 + 1, 2 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 6, j * 10, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12, j * 8 + 1, 2 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([14, i * 10, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - i * 4, j * 6 + 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, j * 2 + 1, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 7, j * 2 + 3, 6])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 5, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    '''
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 6 + 2, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 5, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    # (12 * 18) 2-Layer Created
    # Total Block Used = 27  * 2 = 54 So far
    '''
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_ambulance():
    bricks_ = bricks.Bricks(200, '0')

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

    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16 - 2 * i, j * 2 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 3, i * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([0, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 4, i * 2, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 6, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
      
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2 + i * 2, 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 4, i * 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 1, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 4, i * 2 + 1, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 1, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 2, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 11])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, 3, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([16, 3, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 3, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([20, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([20, 6, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 3, i * 8 - 1, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8 + 5, j * 10 - 2, k * 2 + 1])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_sports():
    bricks_ = bricks.Bricks(200, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)   

    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''
    for i in range(11):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, j * 8 - 1, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 8, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, j * 8 - 1, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 20, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([23, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(11):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([22 - 2 * i, j * 2 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 4 + 1, 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 10, j * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 22, j * 4 + 1, 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 2 + 1, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 14, j * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 19, 3, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([11, i * 2 + 1, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 9, j * 4 + 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([12, i * 2, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([24, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 10, j * 4 + 1, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 6, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 16, j * 6, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, j * 4 + 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, j * 4 + 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, j * 8 - 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, j * 4 + 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, j * 8 - 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, j * 4 + 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for j in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, j * 4 + 1, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([3, 3, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_default_1():
    bricks_ = bricks.Bricks(200, '0')

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

    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([18 - 2 * i, j * 2 + 2, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 6, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 11, j * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 6, j * 2, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 9, j * 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 2, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(5):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 2, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 0])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 0])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_default_2():
    bricks_ = bricks.Bricks(200, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)   

    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 6, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 4, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 6, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 6, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6, i * 4 + 1, j + 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 9, j * 6, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 9, j * 6, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([16, i * 6, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 6, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 2, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 7, 5, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 9, 1, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([14, 4, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([17, 3, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 2 + 2, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 15, 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, 3, 4 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([20, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([20, i * 2 + 2, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([21, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 2 - 1, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 2 + 5, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 2 - 1, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 2 + 5, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 6, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 6, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_mini():
    
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(11):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([23, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(11):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([22 - 2 * i,j * 6 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(11):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([23, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)  
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(10):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 5, j * 8 + 1, 9])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([22, i * 2 + 4, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 10, 10])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 7, j * 4 + 3, 10])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 + 1, 11])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 9, 5, 11])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([23, i * 4 + 1, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([21, i * 4 + 3, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([21, i * 4 + 1, 11])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 2 - 1, j * 4 + 1, 6 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(5):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 4, j * 10, 6 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([23, i * 4 + 1, 6 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 3, j * 12 - 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 17, j * 12 - 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([5, i * 14 - 2, 5 - j * 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([19, i * 14 - 2, 5 - j * 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_10():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 6 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 3, i * 2 + 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_11():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_12():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12 - 2 * i,j * 2 + 2, 7 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 2, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([13, i * 4 + 1, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_13():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for k in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 9 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_14():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - 2 * i,j * 2 + 2, 7 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 2, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 6, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-3, 3, 8 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_15():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8 - 2 * i,j * 2 + 2, 7 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 2, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 6, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([9, 3, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 4, j * 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 2, 12])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([1, i * 4 + 1, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_16():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''   
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([13, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 6 - 2, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 6 - 2, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_17():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''   
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([13, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 2, 10])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_18():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 6 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([j * 4 + 3, i * 2 + 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 3, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 4 + 3, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 5, j * 2 + 3, 10])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 3 + 17, i * 4 + 1, 11])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_19():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(4):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([13, i * 4 + 1, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 4 + 1, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 4 + 1, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 9 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_20():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([12 - 2 * i,j * 2 + 2, 7 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([6, i * 2, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 2, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([13, i * 4 + 1, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_orig_1():
    bricks_ = bricks.Bricks(20, '0')

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 2, 2, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-4, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-4, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_1, brick_2 = (brick.Brick(), brick.Brick())
        brick_1.set_position([0, i * 2 + 2, 1])
        brick_1.set_direction(1)
        brick_2.set_position([-4, i * 2 + 2, 1])
        brick_2.set_direction(1)
        list_brick_.append(brick_1)
        list_brick_.append(brick_2)
    
    brick_ = brick.Brick()
    brick_.set_position([-6, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-8, i * 2, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    
    brick_ = brick.Brick()
    brick_.set_position([-7, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-7, 4, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 4, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    '''
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 6, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 9, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_orig_2():
    bricks_ = bricks.Bricks(40, '0')

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

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 1, i + 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, 1, i + 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 5, i + 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, 5, i + 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([-1, 6, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 0, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    brick_ = brick.Brick()
    brick_.set_position([5, 6, 0])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_orig_3():
    bricks_ = bricks.Bricks(40, '0')

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 5, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 6, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 6, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([8, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([8, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([9, 5, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([9, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([8, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([8, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 4, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 4, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, 1, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 5, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 0, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 6, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([7, 0, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([7, 6, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_21():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 6 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 10, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, j * 8 + 1, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 7 - 1, j * 2 + 3, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, j * 4 + 3, 10])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 8, j * 4 + 3, 10])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_22():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 2, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 4 + 1, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 10])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([11, i * 2, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_23():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''   
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([13, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    '''
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 2, 10])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 7, j * 4 - 1, 9])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 8 - 3, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, 2, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 6 - 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 10 - 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8,  j * 8 - 3, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 10 - 4, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_24():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''   
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([13, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 1, -1, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_25():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for k in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 9 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 10, j * 6, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, 3, 9 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_26():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 8 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 6 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([15, 5, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 12 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 14 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 8 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([j * 4 + 3, i * 2 + 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 3, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_27():
    bricks_ = bricks.Bricks(200, '0')

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

    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([18 - 2 * i, j * 2 + 2, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 6, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 11, j * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 6, j * 2, 6])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 9, j * 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 2, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(5):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 2, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 6, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_28():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([15, i * 4 + 1, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([14 - 2 * i,j * 2 + 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, j * 8 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([3, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([11, i * 10 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 16 - 1, i * 4 + 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 2, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for k in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 9 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 10, j * 6, 9 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([15, 3, 9 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_
    
def car_29():
    bricks_ = bricks.Bricks(40, '0')

    list_brick_ = []

    brick_ = brick.Brick()
    brick_.set_position([0, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 2, 2, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-4, 0, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-4, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_1, brick_2 = (brick.Brick(), brick.Brick())
        brick_1.set_position([0, i * 2 + 2, 1])
        brick_1.set_direction(1)
        brick_2.set_position([-4, i * 2 + 2, 1])
        brick_2.set_direction(1)
        list_brick_.append(brick_1)
        list_brick_.append(brick_2)
    
    brick_ = brick.Brick()
    brick_.set_position([-6, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-8, i * 2, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    
    brick_ = brick.Brick()
    brick_.set_position([-7, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-7, 4, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 0, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 4, 0])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-8, 2, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-6, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-4, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    '''
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 6, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 1])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 9, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def car_30():
    bricks_ = bricks.Bricks(300, '0')

    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    '''   
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(6):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 7 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([13, 1, 8])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 4 - 1, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([10, i * 6 - 2, 7 - 2 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    '''
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 2, 10])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    '''
    for i in range(4):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 2 + 7, j * 4 - 1, 9 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 8 - 3, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, 2, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([4, -1, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8, j * 6 - 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 10 - 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 8,  j * 8 - 3, 6])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 10 - 4, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        car_ambulance(),
        car_demo(),
        car_sports(),
        car_default_1(),
        car_default_2(),
        car_mini(),
        car_orig_1(),
        car_orig_2(),
        car_orig_3(),
        car_10(),
        car_11(),
        car_12(),
        car_13(),
        car_14(),
        car_15(),
        car_16(),
        car_17(),
        car_18(),
        car_19(),
        car_20(),
        car_21(),
        car_22(),
        car_23(),
        car_24(),
        car_25(),
        car_26(),
        car_27(),
        car_28(),
        car_29(),
        car_30(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_CAR)
