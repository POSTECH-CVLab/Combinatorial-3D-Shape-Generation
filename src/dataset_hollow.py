import brick
import bricks
import dataset_common


def square_hollow(w, h):
    bricks_ = bricks.Bricks(200)

    list_brick_ = []

    w_total = 2 * w - 1
    w_last = 2 * w_total

    for i in range(w_total):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)

    for i in range(w_total):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * w_last - 1, i * 2 + 1, 3 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)

    for i in range(w_total):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, w_last, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)

    if h != 2:
        additional_ = h - 2

        for i in range(w):
            for j in range(2):
                for k in range(additional_):
                    brick_ = brick.Brick()
                    brick_.set_position([i * 4, j * w_last, 5 + k])
                    brick_.set_direction(1)
                    list_brick_.append(brick_)

        for i in range(w - 1):
            for j in range(2):
                for k in range(additional_):
                    brick_ = brick.Brick()
                    brick_.set_position([j * w_last - 1, i * 4 + 3, 5 + k])
                    brick_.set_direction(0)
                    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_1():
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

    '''
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
    '''

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_2():
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

    '''
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
    '''
        
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

def hollow_3():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-2 + (i % 2 == 1), i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 8 - 1, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 - 1, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 2, j * 10 -2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-3, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 - 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 - 3, 9, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-4, i * 4 - 2 , 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 - 1, -3 , 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([10, i * 4 - 2, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_4():
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
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 7])
    brick_.set_direction(1)
    list_brick_.append(brick_)
            
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 7 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 7 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 9 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 11])
    brick_.set_direction(1)
    list_brick_.append(brick_)
            
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 11 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 11 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 11 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 11 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_5():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)

        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-2 + (i % 2 == 1), i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 6, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 8 - 1, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 8 - 1, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 2, j * 10 -2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-3, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 - 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, j * 8 - 1, 2])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 2, j * 4 + 1, 2])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 - 2, j * 10 -2, 1])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-3, i * 4 + 1, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([9, i * 4 - 1, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_6():
    bricks_ = bricks.Bricks(100)
    
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
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 -1, -2, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_7():
    bricks_ = bricks.Bricks(100)
    
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
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_8():
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
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 1, 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 10, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6 + 2, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 4 + 3, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6 + 2, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 4 + 3, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_9():
    bricks_ = bricks.Bricks(200)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([13, 13 - i * 2, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([12 - i * 2, 0, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([i * 14 - 1, j * 2 + 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 14, 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)   
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 6])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([13, 13 - i * 2, 6 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([12 - i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([i * 14 - 1, j * 2 + 2, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 14, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)  
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 9])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 9 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 9 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([13, 13 - i * 2, 9 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([12 - i * 2, 0, 9 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(6):
            brick_ = brick.Brick()
            brick_.set_position([i * 14 - 1, j * 2 + 2, 11])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 14, 11])
            brick_.set_direction(0)
            list_brick_.append(brick_)  
            
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 12])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 12 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 12 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([13, 13 - i * 2, 12 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([12 - i * 2, 0, 12 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_10():
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
                
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 10 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 10 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([9, 9 - i * 2, 10 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8 - i * 2, 0, 10 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_11():
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
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 10, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 3, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_12():
    
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
            for k in range(4):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 6, 4 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_13():
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
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_13():
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
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 4 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, 4, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([3, 1, 4 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_14():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 10 - 1, i * 2 + 1, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 10, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_15():
    bricks_ = bricks.Bricks(150)
    
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 5, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 2, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_16():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 2, j * 8 - 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 3, j * 2 + 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_17():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 4, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 1, j * 6 - 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 2, 2, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 8 - 5 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 8 - 5 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, 4, 8 - 5 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 1, 8 - 5 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_18():
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
        
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_19():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 6 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 14, 6 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_20():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 3 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 3 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 3 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 8, 3 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 8, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 7 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 7 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 7 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 8, 7 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 9 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 9 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([7, i * 2 + 1, 9 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 8, 9 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
    
    return bricks_

def hollow_21():
    bricks_ = bricks.Bricks(150)
    
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 5, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 2, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 2, 8 - 5 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_22():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 4, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 1, j * 6 - 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 2, 2, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 8 - 5 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 8 - 5 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, 4, 8 - 5 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 1, 8 - 5 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 9 - 7 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 9 - 7 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, 4, 9 - 7 * i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, 1, 9 - 7 * i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_23():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 2, j * 8 - 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 3, j * 2 + 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 , j * 6, 8])
            brick_.set_direction(1)
            list_brick_.append(brick_)

    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_24():
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
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, j * 4 + 1, 5])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 10, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 4, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 1, 1, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 3, 9, 2 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([8, i * 4 + 2, 2 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6 + 2, 0])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 4 + 3, 0])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6 + 2, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j * 4 + 3, 8])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 4, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 1, 1, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 3, 9, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 2, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_25():
    bricks_ = bricks.Bricks(60)
    
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
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 2 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 6 - 1, 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_26():
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
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, 1, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([2, 0, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([0, 4, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([3, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_27():
    bricks_ = bricks.Bricks(150)
    
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
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 5, 7 - 3 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 2, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 2, 8 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 5, 8 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_28():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 0)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 6, 5 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 - 2, j * 8 - 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 3, j * 2 + 1, 7 - 3 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4 , j * 6, 8 - 5 * k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1 , 3, 8 - 5 * j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)
        
    return bricks_

def hollow_29():
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
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, 1, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, 0, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, 4, 7 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([3, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()  
            brick_.set_position([i * 4 - 1, j * 6 - 1, 11])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 2, 2, 11 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def hollow_30():
    bricks_ = bricks.Bricks(100)
    
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
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 -1, -2, 4 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8 + 1, j * 2, 5])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    list_bricks_ = [
        hollow_1(),
        hollow_2(),
        hollow_3(),
        hollow_4(),
        hollow_5(),
        hollow_6(),
        hollow_7(),
        hollow_8(),
        hollow_9(),
        hollow_10(),
        hollow_11(),
        hollow_12(),
        hollow_13(),
        hollow_14(),
        hollow_15(),
        hollow_16(),
        hollow_17(),
        hollow_18(),
        hollow_19(),
        hollow_20(),
        hollow_21(),
        hollow_22(),
        hollow_23(),
        hollow_24(),
        hollow_25(),
        hollow_26(),
        hollow_27(),
        hollow_28(),
        hollow_29(),
        hollow_30(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_HOLLOW)

