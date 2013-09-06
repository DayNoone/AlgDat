from sys import stdin
def main():
	stdin.readline(),stdin.readline()
	l=0
	d=dict()
	s=stdin.readline().strip()
	r=stdin.readline().strip()
	for li in stdin:
		c=li.split()
		p=c.pop(0)
		for i in c:
			d[i]=p
		while r in d:
			r=d[r]
			l+=1
		if(r==s):
			return l
print(main())