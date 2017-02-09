import sys, random
from math import sqrt

def cm(co):
   matrix = {}
   for i, (x1, y1) in enumerate(co):
      for j, (x2, y2) in enumerate(co):
         dx, dy = x1 - x2, y1 - y2
         dist = sqrt(dx * dx + dy * dy)
         matrix[i, j] = dist
   return matrix 

def city(cities, xmax=8, ymax=6):
   co = []
   for i in xrange(cities):
      x = random.randint(0, xmax)
      y = random.randint(0, ymax)
      co.append((float(x), float(y)))
   return co

def tl(matrix, tour):
   total = 0
   num_cities = len(tour)
   for i in range(num_cities):
      j = (i + 1) % num_cities
      city_i = tour[i]
      city_j = tour[j]
      total += matrix[city_i, city_j]
   return total

def ef(c):
   global cm
   return tl(cm, c) 

class I:
    s = 0
    len = 30
    seperator = ' '
    def __init__(self, c=None, len=30):
        self.c = c or self._mc()
        self.len = len
        self.s = 0  

    def _mc(self):
        "makes a c from randomly sel alleles."
        c = []
        lst = [i for i in xrange(self.len)]
        for i in xrange(self.len):
            choice = random.choice(lst)
            lst.remove(choice)
            c.append(choice)
        return c

    def evaluate(self, optimum=None):
        self.s = ef(self.c)

    def cross(self, other):
        l, r = self._pick()
        p1 = I()
        p2 = I()
        c1 = [ c for c in self.c if c not in other.c[l:r + 1]]
        p1.c = c1[:l] + other.c[l:r + 1] + c1[l:]
        c2 = [ c for c in other.c if c not in self.c[l:r + 1]]
        p2.c = c2[:l] + self.c[l:r + 1] + c2[l:]
        return p1, p2

    def mutate(self):
        l, r = self._pick()
        temp = self.c[l]
        self.c[l] = self.c[r]
        self.c[r] = temp   

    def _pick(self):
        l = random.randint(0, self.len - 2)
        r = random.randint(l, self.len - 1)
        return l, r    

    def __repr__(self):
        return '<%s c="%s" s=%s>' % \
               (self.__class__.__name__,
                self.seperator.join(map(str, self.c)), self.s)  

    def copy(self):
        twin = self.__class__(self.c[:])
        twin.s = self.s
        return twin

    def __cmp__(self, other):
        return cmp(self.s, other.s)

class envi:
    sz = 0
    def __init__(self, po=None, sz=10, gen=10,rate=0.6,crorate=0.9,muterate=0.1):
        self.sz = sz
        self.po = self._mpo()
        self.gen = gen
        self.rate = rate
        self.crorate = crorate
        self.muterate = muterate
        for I in self.po:
            I.evaluate()
        self.generation = 0
        self.mins = sys.maxint
        self.mini = None

    def _mpo(self):
        return [I() for i in range(0, self.sz)]

    def run(self):
        for i in range(1, self.gen + 1):
            for j in range(0, self.sz):
                self.po[j].evaluate()
                curs = self.po[j].s
                if curs < self.mins:
                    self.mins = curs
                    self.mini = self.po[j]
                    print self.mini
            if random.random() < self.crorate:
                children = []
                ni = int(self.rate * self.sz / 2)
                for i in range(0, ni):
                    sel1 = self._rk()
                    sel2 = self._rk()
                    parent1 = self.po[sel1]
                    parent2 = self.po[sel2]
                    c_1, c_2 = parent1.cross(parent2)
                    c_1.evaluate()
                    c_2.evaluate()
                    children.append(c_1)
                    children.append(c_2)
                for i in range(0, ni):
                    sco = 0
                    for k in range(0, self.sz):
                        sco += self.po[k].s
                        
                    r = random.random()
                    a = 0
                    for j in range(0, self.sz):
                        a += (self.po[j].s / sco)
                        if a <= r:
                            self.po[j] = children[i]
                            break
            if random.random() < self.muterate:
                sel = self._select()
                self.po[sel].mutate()
        for i in range(0, self.sz):
                self.po[i].evaluate()
                curs = self.po[i].s
                if curs < self.mins:
                    self.mins = curs
                    self.mini = self.po[i]
                    print self.mini
        print self.mini
        
    def _select(self):
        sco = 0
        for i in range(0, self.sz):
            sco += self.po[i].s
        r = random.random()*(self.sz - 1)
        a = 0
        sel = 0
        for i in range(0, self.sz):
            a += (1 - self.po[i].s / sco)
            if a <= r:
                sel = i
                break
        return sel

    def _rk(self, choosebest=0.9):
        self.po.sort()
        if random.random() < choosebest:
            return random.randint(0, self.sz * self.rate)
        else:
            return random.randint(self.sz * self.rate, self.sz - 1)
     
def main():
    global cm, tour
    tour = range(0,29)
    co =city(30)
    cm = cm(co)
    ev = envi()
    ev.run()

if __name__ == "__main__":
    main()
