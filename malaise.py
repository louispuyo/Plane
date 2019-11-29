import numpy as np 

mar = np.array([[1,2,3,4]])
print(mar)

class brain(object):
    def __init__(self, y):
        self.y = np.ndarray(3)
        self.weight = np.array([3,4])
        self.bias = 0.02
        self.stat_0 = [0,0,0]
        self.net_stat = [i for i in [1,0,-1]]
        

print(brain(object).y)
print(brain(object).net_stat)


class Telegramme:

    def __init__(self, ert):
        self.ert = 3
        
    @classmethod
    def classmethod(cls):
        return 'class method called', cls


    @classmethod
    def zeed(cls):
       return cls('hello')
       
Telegramme.zeed



    