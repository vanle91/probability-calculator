import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **args):
        self.contents = list()
        for key,value in args.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            balls = self.contents
            self.contents = list()
        else:
            balls = random.sample(self.contents, num)
            for ball in balls:
                self.contents.remove(ball)
            
        return balls
        
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total = 0
    for i in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        balls = experiment_hat.draw(num_balls_drawn)
        draw_balls = dict()
        for ball in balls:
            draw_balls[ball] = draw_balls.get(ball, 0) + 1

        success = 1
        for ball,count in expected_balls.items():
            if draw_balls.get(ball, 0) < count:
                success = 0
        total += success
    return total / num_experiments
        
        