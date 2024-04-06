
from random import choice
import matplotlib.pyplot as plt
import pygal
class RandomWalk:
    def __init__(self, num_points=10000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = choice([1, -1]) 
            y_step = choice([1, -1]) 
            x_distance = choice([0, 1, 2, 3, 4]) 
            y_distance = choice([0, 1, 2, 3, 4]) 
            x_step *= x_distance
            y_step *= y_distance
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
  rw = RandomWalk()
  rw.fill_walk()
  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolor='none', s=5)
  plt.scatter(0, 0, c='green', edgecolors='none', s=100)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
  plt.show()
  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
   break

