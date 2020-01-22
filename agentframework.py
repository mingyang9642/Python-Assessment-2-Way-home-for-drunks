# -*- coding: utf-8 -*-
"""
@author: 201376598
"""

import random

class Agent():
    def __init__(self, environment):
        self.x = random.randint(138, 158)
        self.y = random.randint(128, 148)
        self.environment = environment
        
    def move(self):
        if random.random() < 0.25:
            self.x = (self.x + 1) % 300
        elif random.random() < 0.5:
            self.x = (self.x - 1) % 300
        elif random.random() < 0.75:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
        return(self.x, self.y)
        
    def eat(self, environment):
        environment[self.x][self.y] = environment[self.x][self.y] + 1
    

