import brick
import bricks
import dataset_common


def bench_1():
    bricks_ = bricks.Bricks(40)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([1, 0, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 1, 3])
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
    brick_.set_position([0, 7, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 9, 3])
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
    brick_.set_position([0, 15, 2])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 17, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 18, 2])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(10):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 4 + 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_1, brick_2 = (brick.Brick(), brick.Brick())
        brick_1.set_position([3, i * 4 + 1, 4])
        brick_2.set_position([3, i * 4 + 1, 5])
        brick_1.set_direction(0)
        brick_2.set_direction(0)
        list_brick_.append(brick_1)
        list_brick_.append(brick_2)
        
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_2():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([(i % 2 == 1), 0, 5 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 1, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 0, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 3, 9 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 14, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([(i % 2 == 0), 14, 8 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([- 1 + 2 * (i % 2 == 0), 7, 8 - i])
        brick_.set_direction((i % 2 == 0))
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 7, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 8 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(8):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 12 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 14, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 4 + 5, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 2 + 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 + 1, j  * 7, 3 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j  * 7, 1])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 + 1, j  * 7, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_3():
    bricks_ = bricks.Bricks(150)
    
    list_brick_ = []
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, 5 + i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([0, 1, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 0, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 3, 9 + (i % 2 == 0)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    brick_ = brick.Brick()
    brick_.set_position([1, 14, 10])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([0, 14, 8 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    '''
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([- 1 + (i % 2 == 0), 7, 8 - i])
        brick_.set_direction((i % 2 == 0))
        list_brick_.append(brick_)
    '''
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0, 7, 8 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([-1, 7, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 7, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 8 + 3, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(8):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 12 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 14, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([6, i * 4 + 5, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(6):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 2 + 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([8, i * 4 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 + 1, j  * 14, 3 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_4():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1 - (i % 2 == 1), i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0,i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    '''    
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
    '''
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 8 - 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 12 - 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-2, i * 16 - 5, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 8, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 - 4, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i - 1, 12, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i - 1, -6, 4 - i])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_5():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 4 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(7):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(8):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 2, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 6 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 6 + 4, 7])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 6 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 6 + 4, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_6():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    brick_ = brick.Brick()
    brick_.set_position([0, 0, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 2 + 1, 5 + (i % 2 == 1)])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 2 + 2, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2, 3 - (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 10, j * 4 + 1, 4])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 14, j * 2, 3 - (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([18, i * 4 + 1, 1])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, i * 4 + 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([-1, 3, 2 - i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-2, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([-2, 3, 9])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_7():
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
    
    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([19, i * 4 + 1, 5])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(9):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([18 - 2 * i,j * 2 + 2, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 18, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(9):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 + 1, 6, 10 + (i % 2 == 1)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        brick_ = brick.Brick()
        brick_.set_position([i * 4 + 1, 6, 12])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 20 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_8():
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
    
    for i in range(16):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 6, 5 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([33, i * 4 + 1, 6])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(16):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([32 - 2 * i,j * 2 + 2, 5 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, 6, 7 + k])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 14, 6, 7 + k])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 26, 6, 7 + k])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 34 - 1, 6, 7 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 21, 6, 7 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for k in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 9, 6, 7 + k])
            brick_.set_direction(0)
            list_brick_.append(brick_)
          
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 12 + 10, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 34 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_9():
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
        
    brick_ = brick.Brick()
    brick_.set_position([0, 10, 3])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    # Outer Bricks All Covered
    
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 10, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([17, i * 8 + 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([16 - 2 * i,j * 6 + 2, 3 + (i % 2 == 1)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([1, i * 4 + 3, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(8):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 2 + 2, j * 2 + 4, 3 + (i % 2 == 0)])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    brick_ = brick.Brick()
    brick_.set_position([17, 5, 4])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(5):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6 + 4, 5 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
            
    for i in range(5):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 4 + 5, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(10):
        brick_ = brick.Brick()
        brick_.set_position([i * 2 - 1, 7, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_10():
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
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_11():
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
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_12():
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
        for j in range(4):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
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

def bench_13():
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
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
        
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 4, 7])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_14():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 5 - 2 * i, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_15():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 10, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 9 - 2 * i, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 10, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 4 + 3, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 10, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 8 + 1, 3 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_16():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 10, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 9 - 2 * i, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 4 + 1, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 10, 8])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 3, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 8 + 1, 3 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_17():
    bricks_ = bricks.Bricks(80)
    
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
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2 + 4, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 10 - 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_18():
    bricks_ = bricks.Bricks(80)
    
    list_brick_ = []
    
    for i in range(9):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 18 - 1, 1, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(9):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 2, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, 0, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 18 - 1, 1, 3])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_19():
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
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, j * 6, 4])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2 , j * 6, 3])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 2])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2 , j * 6, 1])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, j * 6, 0])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 10 - 1, j * 4 + 1, 3 - 2 * k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 10 - 1, 3, 2])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_20():
    bricks_ = bricks.Bricks(150)
    
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
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 3])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 5 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 6, 2 - k])
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

def bench_21():
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
            brick_ = brick.Brick()
            brick_.set_position([i * 8 + 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
                
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_22():
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
    
    for i in range(3):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 4, 11 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, j * 8 - 1, 9])
            brick_.set_direction(1)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_
    
def bench_23():
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
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-3, i * 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([-5, i * 4 + 1, 8 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-4, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_24():
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
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([-1, i * 4 + 1, 7 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([1, 3, 5])
    brick_.set_direction(0)
    list_brick_.append(brick_)
    
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-3, i * 2, 9])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 2 -5, j * 4 + 1, 8 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
            
    for i in range(4):
        brick_ = brick.Brick()
        brick_.set_position([-4, i * 2, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8 - 4, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)

    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_25():
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
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 6, 4])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 10 - 1, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(3):
            brick_ = brick.Brick()
            brick_.set_position([i * 4 + 2, j * 2, 7])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_26():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 5 - 2 * i, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 4 + 1, 4 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, i * 4 + 1, 9])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_27():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 5 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 6, 6])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 5 - 2 * i, 5 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 5])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([0, i * 6, 7 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([0, 3, 7 + i])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([2, i * 2, 4 - j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 6 - 1, 3, 4 - j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_28():
    bricks_ = bricks.Bricks(100)
    
    list_brick_ = []
    
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([i * 2, 0, 4 + (i % 2 == 0)])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(5):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 6 - 1, i * 2 + 1, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 4, 10, 5])
        brick_.set_direction(1)
        list_brick_.append(brick_)
        
    for i in range(4):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([j * 2 + 1, 9 - 2 * i, 4 + (i % 2 == 1)])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    brick_ = brick.Brick()
    brick_.set_position([2, 2, 4])
    brick_.set_direction(1)
    list_brick_.append(brick_)
    
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 10, 6 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([4, i * 4 + 3, 6 + j])
            brick_.set_direction(0)
            list_brick_.append(brick_)
            
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([2, i * 10, 3])
        brick_.set_direction(1)
        list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 6 - 1, j * 8 + 1, 3 - k])
                brick_.set_direction(0)
                list_brick_.append(brick_)
                
    for i in range(3):
        brick_ = brick.Brick()
        brick_.set_position([5, i * 4 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([3, i * 8 + 1, 8])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_29():
    bricks_ = bricks.Bricks(80)
    
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
                brick_.set_position([i * 4, j * 2 + 4, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(3):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 4, 6, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
            
    for i in range(2):
        for j in range(2):
            brick_ = brick.Brick()
            brick_.set_position([i * 8, 4, 9 + j])
            brick_.set_direction(1)
            list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(2):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 10 - 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_

def bench_30():
    bricks_ = bricks.Bricks(80)
    
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
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 4, j * 2 + 4, 7 + k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        for j in range(2):
            for k in range(3):
                brick_ = brick.Brick()
                brick_.set_position([i * 8, j * 6, 4 - k])
                brick_.set_direction(1)
                list_brick_.append(brick_)
                
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([i * 10 - 1, 3, 4])
        brick_.set_direction(0)
        list_brick_.append(brick_)
        
    for i in range(2):
        brick_ = brick.Brick()
        brick_.set_position([4, i * 2 + 4, 10])
        brick_.set_direction(1)
        list_brick_.append(brick_)
    
    for brick_ in list_brick_:
        bricks_.add(brick_)

    return bricks_


if __name__ == '__main__':
    # Removed bench_1, and then renamed all.
    list_bricks_ = [
        bench_1(),
        bench_2(),
        bench_3(),
        bench_4(),
        bench_5(),
        bench_6(),
        bench_7(),
        bench_8(),
        bench_9(),
        bench_10(),
        bench_11(),
        bench_12(),
        bench_13(),
        bench_14(),
        bench_15(),
        bench_16(),
        bench_17(),
        bench_18(),
        bench_19(),
        bench_20(),
        bench_21(),
        bench_22(),
        bench_23(),
        bench_24(),
        bench_25(),
        bench_26(),
        bench_27(),
        bench_28(),
        bench_29(),
        bench_30(),
    ]

    dataset_common.create_bricks(list_bricks_, dataset_common.STR_LABEL_BENCH)

