import Queue

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()
    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")



"""
SOLUTION
"""

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

def isLeaf(node):
    if 
    return True

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    final_string = ""
    cur_node = root
    for i in range(0, len(s)):
        if i == 0:
            cur_node = cur_node.left
        elif i == 1:
            cur_node = cur_node.right
        if isLeaf(cur_node):
            final_string+=cur_node.data
            cur_node = root
    
    print final_string

"""
END SOLN
"""

ip = raw_input()
freq = {}#maps each character to its frequency

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object
dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)