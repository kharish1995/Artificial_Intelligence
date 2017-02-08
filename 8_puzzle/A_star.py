import numpy as np
class States():
	def __init__(self,s=None):
		
		self.s=s
		self.path = None
		self.pc=0
		self.ef=0
	def d(self):
		goal=np.array([[0,1,2],[3,4,5],[6,7,8]])
		s1=0
		for i in range(9):
			(b1,b2)=np.where(goal==i)
			(a1,a2)=np.where(self.s[1:4,1:4]==i)
			s1=s1+abs(b1-a1)+abs(b2-a2)
		return (s1)	
	
	def swap(self,i,j):
		(a1,a2)=np.where(self.s[1:4,1:4]==0)
		a1=a1+1	
		a2=a2+1
		(self.s[a1,a2],self.s[a1+i,a2+j])=(self.s[a1+i,a2+j],self.s[a1,a2])
		
def succ(cs):
	c=[]
	m=[(1,0), (0,1), (-1,0), (0,-1)]
	for i in range(4):
		new_s=States()
		new_s.s=cs.s.copy()
		(a,b)=m[i]
		new_s.swap(a,b)
		if (new_s.s!=cs.s).any():
			new_s.path=cs
			new_s.pc=new_s.pc+cs.pc+1
			new_s.ef=new_s.ef+new_s.pc+new_s.d()
			c.append(new_s)
	return c
	
def astar():
	x1=np.zeros((5,5))
	x2 = np.arange(9)
	np.random.shuffle(x2)
	count = 0
	for i in range (0,8):
		count += abs(i-x2[i])
	while(count % 2 == 0):
		count = 0
		np.random.shuffle(x2)
		for i in range (0,8):
			count += abs(i-x2[i])
	x2 =x2.reshape(3,3)
	x1[1:4,1:4]=x2
	Init_s=States(x1)
	if Init_s.d()==0:
		return(Init_s)
	f = list()
	explored = set()
	f.append(Init_s)
	front=list()
	z = map(tuple,Init_s.s)
	z=tuple(z)
	front.append(z)
	
	while f:
		kj=0
		f.sort(key=lambda front: front.ef)
		z = map(tuple, f[0].s)
		z=tuple(z)
		try:
			front.remove(z)
		except ValueError:
	  		for x in front:
				if (z == x).all(): 
					del (front[kj])
				kj+=1
		s = f.pop(0)
		if s.d()==0:
			return(s)
		x = map(tuple, s.s)
		x=tuple(x)
		explored.add(x)
		c = succ(s)
		print(len(explored))
		for child in c:
			y = map(tuple, child.s)
			y=tuple(y)
			if (y not in explored) and (not(any((y == x).all() for x in front))) :
				f.append(child)
				front.append(child.s)
	return None

def prsol(sol):
	path = []
	path.append(sol)
	path = sol.path
	while path:
		path.append(path)
		path = path.path
	for t in range(len(path)):
			print path[len(path) - t - 1].s
			print path[len(path) - t - 1].pc
			print path[len(path) - t - 1].ef
			print t

def main():	
	sol = astar()
	prsol(sol)

if __name__ == "__main__":
	main()
