import random
from math import sqrt

def cm(co):
   matrix = {}
   for i, (x1, y1) in enumerate(co):
      for j, (x2, y2) in enumerate(co):
         dx, dy = x1 - x2, y1 - y2
         dist = sqrt(dx * dx + dy * dy)
         matrix[i, j] = dist
   return matrix 

def cr(cities, xmax=8, ymax=6):
   co = []
   for i in xrange(cities):
      x = random.randint(0, xmax)
      y = random.randint(0, ymax)
      co.append((float(x), float(y)))
   return co

def tl(matrix,tour):
    total=0;
    num_cities=len(tour);
    for i in range(num_cities):
        j=(i+1)%num_cities;
        city_i=tour[i];
        city_j=tour[j];
        total+=matrix[city_i,city_j];
    return total;

def rt(tl):
   tour=range(tl);
   random.shuffle(tour);
   return tour;

initial = lambda: rt(len(tour))
of = lambda tour: tl(m,tour)

def ap(size,shuffle=random.shuffle):
    r1=range(size);
    r2=range(size);
    if shuffle:
        shuffle(r1);
        shuffle(r2);
    for i in r1:
        for j in r2:
            yield (i,j);

def sc(tour):
    for i,j in ap(len(tour)):
        if i < j:
            copy=tour[:];
            copy[i],copy[j]=tour[j],tour[i];
            yield copy

def hillclimb(initial, mo, of, max_evaluations):
    best=initial();
    b=of(best);
    m=1;
    while m < max_evaluations:
        move_made=False;
        for next in mo(best):
            if m >= max_evaluations:
                break;
            n=of(next);
            print (m,b,best)
            m+=1;
            if n < b:
                best=next;
                b=n;
                move_made=True;
                break;             
        if not move_made:
            break; 
    print (m,b,best)

def main():
    global tour, co, m
    tour = range(0,29);
    co =cr(30)
    m = cm(co)
    hillclimb(initial, sc, of, 10);
       
if __name__ == "__main__": main()
