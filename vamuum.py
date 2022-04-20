import os
import random
import math
from time import sleep
from termcolor import colored

class Vacuum():
    position = list()
    current = list()
    dirty = list()

    def __init__(self ,*args , **kwargs):
        self._Dimension = kwargs.get('dimension')
        
        self.make_position()
        self.make_random_dirty(kwargs.get('dirty'))
        self.current = [
            self.get_random(self._Dimension),
            self.get_random(self._Dimension)
        ]
        self.start()

    def create_board(self):
        os.system('cls')
        print(" _",end="")
        print(" _"*(self._Dimension-1))
        Counter_while=0  
        while Counter_while!=self._Dimension:
            for i in range(self._Dimension+1):
                if i !=self._Dimension:
                    if self.current== [Counter_while,i]:    
                        print("|",end="")
                        print(colored("X", "cyan"),end= "")
                    elif [Counter_while,i] in self.dirty:
                        print("|",end="")
                        print(colored("D", "yellow"),end= "")
                    else: 
                        print("|_",end="")    
                else:
                    print("|",end= "\n")
            Counter_while+=1

    def get_random(self, value):
        return random.randint(0,value-1)

    @property
    def up(self):
        self.current[0] -=1

    @property
    def down(self):
        self.current[0] +=1

    @property
    def right(self):
        self.current[1] +=1

    @property
    def left(self):
        self.current[1] -=1

    def make_position(self):
        for i in range(10):
            for j in range(10):
                self.position.append([i,j])

    def clear(self):
        self.position.remove(self.current)

    def make_random_dirty(self, value):
        for i in range(value):
            self.dirty.append(
                [self.get_random(self._Dimension),
                self.get_random(self._Dimension)]
            )

    def get_least_distance(self):
        least_distance= []
        for item in self.dirty:
            new_distance = math.sqrt(
                (self.current[1]-item[1])**2 +
                (self.current[0]-item[0])**2)

            if least_distance:
                least_distance_with_current = math.sqrt(
                    (self.current[1]-least_distance[1])**2 +
                    (self.current[0]-least_distance[0])**2)

            if not least_distance or  new_distance < least_distance_with_current:
                least_distance= item

        return least_distance


    def start(self):
        while True:
            sleep(0.5)

            if self.current in self.dirty:
                self.dirty.remove(self.current)

            if not self.dirty:
                os.system('cls')
                input('YOU WIN')
                exit(0)

            self.create_board()

            least_distance = self.get_least_distance()

            if least_distance[1] < self.current[1] :
                self.left
                continue
            elif least_distance[1] > self.current[1]:
                self.right
                continue

            if least_distance[0] < self.current[0]:
                self.up
                continue
            elif least_distance[0] > self.current[0]:
                self.down
                continue


if __name__=='__main__':
    os.system('cls')
    while True:
        try:
            dimension= int(input('Dimension? '))
            dirty= int(input('\namount of dirts? '))
            break
        except:
            print("PLS ENTER A VALID NUMBER")
            continue
    
    Vacuum(dimension=dimension, dirty=dirty)

