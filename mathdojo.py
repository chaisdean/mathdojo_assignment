import math



class mathdojo(object):
    def __init__(self):
        self.results = 0
        #print self.results

    def add(self, *args):
        for i in args:
            if type(i) == list and type(i) == tuple:
                for k in i:
                    self.results += k
            else:
                self.results += i
        return self

    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.results -= k
            else:
                self.results -= i
        return self
Mathdojo = mathdojo()
print Mathdojo.add(2,4).add(2,5).subtract(3,2).results
