import brick
import bricks
import dataset_common


def cup_1():
    bricks_ = bricks.Bricks(40)
    
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
    brick_.set_position([7, 1, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([7, 5, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([7, 3, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 5, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_2():
    bricks_ = bricks.Bricks(40)
    
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
    brick_.set_position([5, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 5, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
 
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 5, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, 0, i + 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
        brick_ = brick.Brick()
        brick_.set_position([-2, 4, i + 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([1, -1, i + 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([5, -1, i + 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([6, 2, i + 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([6, 6, i + 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([-1, 7, i + 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([3, 7, i + 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_3():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0,i * 2 + 2, 3])
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
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([9, 3, 6 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 2, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([5, 3, 6 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(7):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 5 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 6 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([5, 3, 11])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_4():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1 - (i % 2 == 1), i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, -1, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 4, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([8 - (i % 2 == 1), 3 - i * 2,5 - (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_) 
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_) 
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, - 2, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)    
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 4 - 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 6 - 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 6 - 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 1, j * 6 - 2, 6 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, 1, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-3, 1, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 4 - 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_5():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1 - (i % 2 == 1), i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-2, -1, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 -1, 4, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([12 - (i % 2 == 1), 3 - i * 2,5 - (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_) 
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_) 
    '''
    brick_ = brick.Brick()
    brick_.set_position([-1, -3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    '''
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1 - (i % 2 == 1), -3 - i * 2, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_) 
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([11 + (i % 2 == 1), -3 - i * 2, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_) 
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, -2 - i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, -2 - i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)

    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 -1, -6, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 3, j * 6 - 4, 3])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 3, -1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([14, i * 2 - 2, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([16 - i * 4, -1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            for k in range(7):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 1, j * 10 - 6, 6 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        for k in range(6):
            brick_ = brick.Brick()
            brick_.set_position([-2, 3 - i * 4, 6 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-2 - (i % 2 == 1), 3 - i * 4, 12])
        brick_.set_direction(0)
        list_brick_.append(brick_) 
    
    for i in range(2):
        for j in range(7):
            brick_ = brick.Brick()
            brick_.set_position([12, i * 8 - 5, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([14, i * 2 - 2, 12])
        brick_.set_direction(1)
        list_brick_.append(brick_)
     
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_6():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 2 + 2, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 5 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 10, 5 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_7():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 2 + 2, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 4 + 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 5 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 2 + 3, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([12, i * 2 + 4, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, j * 8 + 1, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 3, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 8 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 8 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 8 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 8 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 10, 5, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([12, i * 2 + 4, 12])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, j * 8 + 1, 12])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 3, 12])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([9, 5, 12])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 13 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 13 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 13 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 13 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 15])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 15 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 15 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 15 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 15 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_8():
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
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 8 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 8 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 8 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 8 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 2, 4 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 3, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 4 + 1, 1])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_9():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 4 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 4 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 8])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 8 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 8 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, 5 - i * 2, 8 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4 - i * 2, 0, 8 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_10():
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
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 1, 7])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 10, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 3, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 8 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 10, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 2 + 4, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 2 + 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 11, 5, 6 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 3 + 11, 5, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 11, 5, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([13, i * 2 + 4, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 + 2, j * 10, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, j * 6 + 2, 1])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 10, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 1, 5, 0])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_11():
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 2, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_12():
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([7, i * 2 + 2, 7 - 4 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, 3, 6 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_13():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 4, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 3 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 2, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 2, 6])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([7, 2, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([6, 2, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([5, 2, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([3, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 2, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_14():
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2 + 2, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_15():
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([7, i * 2 + 2, 7 - 4 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, 3, 6 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 7 - 4 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 6, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 6, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 9 - 8 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 9 - 8 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_16():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, 1, 7 - 3 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 9, 7 - 3 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 4 + 2, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2 + 3, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_17():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_) 
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([3, 2 * i + 2, 3 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_18():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 4, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([3, 5, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 2, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 6, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 1, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 4, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([3, 5, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([4, 2, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 6, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_19():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 14 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 14, 8 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(6):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 12, j * 2 + 2, 8 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([i * 8 + 2, j * 2 + 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 4, j * 2 + 2, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 14, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_20():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
       
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 5 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_21():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 4, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 3 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([2, 4, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([3, 1, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 2 + 1, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 2 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 2 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
        brick_ = brick.Brick()
        brick_.set_position([2, 4, 2 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
        brick_ = brick.Brick()
        brick_.set_position([3, 1, 2 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_22():
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([7, i * 2 + 2, 7 - 4 * j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, 3, 6 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 7 - 4 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    brick_ = brick.Brick()
    brick_.set_position([-1, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 6, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 4 + 1, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([-3, 3, 7])
    brick_.set_direction(0)
    list_brick_.append(brick_)
                
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_23():
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
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(4):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_24():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_) 
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([3, 2 * i + 2, 3 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 4, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 - 1, 7, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 1, -1, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_25():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
       
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 6, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
          
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_26():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_) 
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([3, 2 * i + 2, 3 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 1, j * 4 + 1, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 4 + 1, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6, 3, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def cup_27():
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
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_28():
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
        for j in range(2):
            for k in range(5):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 6, 7 + k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(5):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2 + 2, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
                
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_29():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 4, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 3 - i * 2, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([2, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, 1, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([2, 0, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([0, 4, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([3, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 1, j * 2 - 1, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def cup_30():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
       
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 5 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 5 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 2, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([1, 1, 8 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):    
        brick_ = brick.Brick()
        brick_.set_position([0, 4, 8 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([3, 5, 8 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([4, 2, 8 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
          
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        cup_1(),
        cup_2(),
        cup_3(),
        cup_4(),
        cup_5(),
        cup_6(),
        cup_7(),
        cup_8(),
        cup_9(),
        cup_10(),
        cup_11(),
        cup_12(),
        cup_13(),
        cup_14(),
        cup_15(),
        cup_16(),
        cup_17(),
        cup_18(),
        cup_19(),
        cup_20(),
        cup_21(),
        cup_22(),
        cup_23(),
        cup_24(),
        cup_25(),
        cup_26(),
        cup_27(),
        cup_28(),
        cup_29(),
        cup_30(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_CUP)

