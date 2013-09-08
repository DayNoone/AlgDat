from sys import stdin
def main():
	stdin.readline(),stdin.readline()
	level=0
	d=dict()
	start_node=stdin.readline().strip()
	ratatosk_node=stdin.readline().strip()
	for line in stdin:
		children=line.split()
		parent=children.pop(0)
		for child in children:
			d[child]=parent
		while ratatosk_node in d:
			ratatosk_node=d[ratatosk_node]
			level+=1
		if(ratatosk_node==start_node):
			return level
print(main())
