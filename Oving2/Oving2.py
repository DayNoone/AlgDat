from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    depth = None
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0
        self.depth = 0

def dfs(rot):
    q = [rot]
    while q:
        node = q.pop()
        if(node.ratatosk == True):
            return node.depth
        else:
            for i in node.barn:
                q.append(i)
                i.depth = node.depth + 1
        

def bfs(rot):
    q = deque([rot])
    while q:
        node = q.popleft()
        if(node.ratatosk == True):
            return node.depth
        else:
            for i in node.barn:
                q.append(i)
                i.depth = node.depth + 1
  
        
            

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print (bfs(start_node))
