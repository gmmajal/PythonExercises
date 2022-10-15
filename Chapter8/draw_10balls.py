import random


def make_balls():
    red = ['red'] * 10
    yellow= ['yellow'] * 10
    blue = ['blue'] * 10
    purple = ['purple'] * 10
    balls=red+yellow+blue+purple
    return balls


def comp_Prob():
    N = 10 ** 4
    count = 0
    for nn in range(N):
        balls=make_balls()
        random.shuffle(balls)
        draw_balls = [balls[i] for i in range(10)]
        del balls[:10]
        if draw_balls.count('blue')==2 and draw_balls.count('purple')==2:
            count += 1
    print('Probability of drawing two blue and two purple balls out of 10 from the hat is:%f'%(count/float(N)))


if __name__=='__main__':
    comp_Prob()

