#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        if(type(size) != int):
            print("size must be an integer")
        else:
            self._size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if(type(size) != int):
            print("size must be an integer")
        else:
            self._size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")