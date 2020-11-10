import random
import copy


class Hat:
  def __init__(self, **colors):
    balls = []

    for color, quantity in colors.items():
      for _ in range(0, quantity):
        balls.append(color)

    self.contents = balls

  def draw(self, num):
    # self.contents is to be mutated (no copying required)
    balls = self.contents
    drawn = []

    while len(balls) and num > 0:
      i = random.randrange(len(balls))
      ball = balls.pop(i)
      drawn.append(ball)
      num -= 1

    return drawn



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  good_draws = 0

  for _ in range(0, num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_list = hat_copy.draw(num_balls_drawn)
    drawn_dict = make_dict(drawn_list)

    for color, quant in expected_balls.items():
      if color in drawn_dict and quant <= drawn_dict[color]:
        success = True
      else:
        success = False
        break

    if success:
      good_draws += 1

  return good_draws / num_experiments

def make_dict(list):
  dict = {}

  for item in list:
    if item not in dict:
      dict[item] = 1
    else:
      dict[item] += 1

  return dict
