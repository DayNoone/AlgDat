from sys import stdin

def main():
	stdin.readline()
	stdin.readline()
	start_node = stdin.readline().strip()
	ratatosk_node = stdin.readline().strip()

	d = {}
	for line in stdin:
		temp_line = line.split()
		d[temp_line.pop(0)] = temp_line
	find_father(d, ratatosk_node, start_node, 0)

	
def find_father(d, ratatosk_node, start_node, lvl):
	if(ratatosk_node == start_node):
		print lvl
	for i in d.keys():
		for j in d[i]:
			if(j == ratatosk_node):
				find_father(d, i, start_node, lvl+1)
main()