# Complete the riddle function below.
def riddle(arr):
    # complete this function
    my_stack = []
    min_no_max_ws_map = {}
    
    for i in range(len(arr)):
        num = arr[i]
        
        if not len(my_stack):
            my_stack.append(int(num))
            min_no_max_ws_map[num] =1
        else:
            top = my_stack[-1]
            if num>top:
                for x in my_stack:
                    min_no_max_ws_map[x] += 1
                my_stack.append(int(num))
                min_no_max_ws_map[num] = 1
            elif num<=top:
                min_no_max_ws_map[num] = 1
                while len(my_stack) and (num<=top):
                    my_stack = my_stack[:-1]
                    min_no_max_ws_map[num] = min_no_max_ws_map[top] + 1
                    if len(my_stack):
                        top = my_stack[-1]
                for x in my_stack:
                    min_no_max_ws_map[x] += 1
                my_stack.append(int(num))
                
    print min_no_max_ws_map
    keys = min_no_max_ws_map.keys()
    values = min_no_max_ws_map.values()
    ws_min_map = {}
    
    for key,val in min_no_max_ws_map.iteritems():
        if val not in ws_min_map:
            ws_min_map[val] = key
        else:
            if key > ws_min_map[val]:
                ws_min_map[val] = key
    for size in range(len(arr), 0,-1):
        if size not in ws_min_map:
            ws_min_map[size] = ws_min_map[size+1]
    return ws_min_map.values()  
