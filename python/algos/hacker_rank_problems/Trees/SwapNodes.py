l = [0]
r = [0]
d= {}
sys.setrecursionlimit(15000)
def inorder(node,result):
    if l[node]>0:
        result = inorder(l[node],result)
    result.append(node)
    if r[node]>0:
        result = inorder(r[node],result)
    return result

def calc_depth(cur,depth):
    d[cur] = depth
    if l[cur]>0:
        calc_depth(l[cur], depth+1)
    if r[cur]>0:
        calc_depth(r[cur], depth+1)

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    result_list = []
    for idx in indexes:
        l.append(idx[0])
        r.append(idx[1])
    
    calc_depth(1,1)
    
    for k in queries:
        for i in range(1,n+1):
            if d[i]%k ==0:
                tmp = l[i]
                l[i] = r[i]
                r[i] = tmp
        result_list.append(inorder(1,[]))
    
    return result_list
