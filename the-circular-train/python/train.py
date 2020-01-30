#!/usr/bin/python3

import random as rd

class wagon:

    def __init__(self, prev_w = None, next_w = None):
        self.on = bool(rd.getrandbits(1))
        self.prev_w = self if prev_w is None else prev_w
        self.next_w = self if next_w is None else next_w

class train:

    def __init__(self, size):

        first = wagon()
        last = first 

        for i in range(size-1):
            new_w = wagon(last, first) 
            last.next_w = new_w
            last = new_w
            
        first.prev_w=last
        self.current_wagon=first

    def move_next(self):
        self.current_wagon=self.current_wagon.next_w

    def move_prev(self):
        self.current_wagon=self.current_wagon.prev_w

    def is_wagon_on(self):
        return self.current_wagon.on

    def switch_wagon(self):
        self.current_wagon.on = not self.current_wagon.on

