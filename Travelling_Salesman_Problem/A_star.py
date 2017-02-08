import numpy as np
import random
from itertools import combinations
nodes=30
min=random.randrange(20,30)
max=random.randrange(60,70)
costli=[]
class Cities():
	def __init__(self,j):
		self.x1= random.randrange(min,max)
		self.x1= random.randrange(min,max)
		self.no=j

def mst(cl):
	mstcost=0
	Lc=set()

	C=list(combinations(cl,2))

	c1=set()
	x=set()
	while C:
		dc=[]
		for cpa in C:
			(a,b)=cpa
			dc.append(dist(a,b))
	
		ind=dc.index(min(dc))
		c1=set([item for item in C[ind]])
		if c1 & x !=c1 or c1 & x == set([]):
			mstcost+=dc.pop(ind)
			Lc.add(C[ind])
			x=set([item for sublist in Lc for item in sublist])
			C.remove(C[ind])
		
		else:
			C.remove(C[ind])
	return mstcost


def dist(C1,C2):
	dc=((C1.x1-C2.x1)*2+(C1.x1-C2.x1)*2)
	return (dc)


def pathcost(cl):
	pathcost=0
	Citlist=list(cl)
	for j in range(len(Citlist)-1):
		pathcost+=dist(Citlist[j],Citlist[j+1])	
	return(pathcost)

	
def successors(Citie,explored,City):
	children=[]
	hu=[]

	cities=[C for C in Citie if C not in explored]
	for i in range(len(cities)):
		C=list(cities)
		children.append(C.pop(i));
		hu.append(mst(C)+dist(children[i],City))
		
	
	return (hu,children)
	
def astar(citlist):
	ac=[]
	k=0
	evalfunc=[]
	index=0
	frontier = list()
	explored = set()
	frontier.append(citlist[0])
	evalfunc.append(0)
	while frontier:
		City = frontier.pop(index)
		evalfunc.pop(index)
		
		explored.add(City)
		ac.append(City)
		pco=pathcost(ac)
		if len(ac)==len(citlist):
			print"No. of loops"
			print k
			return(ac)
		
		hu,children = successors(citlist,explored,City)
		for i in range(len(children)):
			
			if children[i] not in frontier :
				frontier.append(children[i])
				L=hu[i]+pco
				evalfunc.append(L)
				
		k+=1						
		index=evalfunc.index(min(evalfunc))
	return None


def main():	
	city=[]
	for i in range(nodes):
		cit=Cities(i)
		city.append(cit)
	img=np.zeros((800,800,3))
	solution = astar(city)
	print "initial path"
	city.append(city[0])
	print [pat.no for pat in city]
	print "initial path cost"
	print pathcost(city)
	solution.append(city[0])
	print "final path"
	print [pat.no for pat in solution]
	print "Final pathcost"
	print pathcost(solution)
if __name__ == "__main__":
	main()