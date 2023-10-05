#!/bin/python3

import math
import os
import random
import re
import sys


class Item:
    # Implement the Item here
    def __init__(self,name,price):
        self.name = str(name)
        self.price = int(price)
    
    pass


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.namelst = []
        self.pricelst = []
        self.countlst = []
        self.length = 0
        
    def __len__(self):
        return self.length
        
    def add(self,item):
        if item.name in self.namelst:
            ind = self.namelst.index(item.name)
            self.countlst[ind] += 1
        
        else:
            self.namelst.append(item.name)
            self.pricelst.append(item.price)
            self.countlst.append(1)
        
        self.length += 1
        return None
            
    def total(self):
        tot = 0
        for i in self.namelst:
            tot += self.pricelst[self.namelst.index(i)]*self.countlst[self.namelst.index(i)]
        return tot
        
    pass

item1 = Item('1',100)
item2 = Item('2',130)
cart = ShoppingCart()
cart.add(item1)
cart.add(item2)
cart.add(item1)
len(cart)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
