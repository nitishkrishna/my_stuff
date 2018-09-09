# Complete the activityNotifications function below.
def calc_median(arr, take_mid, mid):
    if take_mid:
        return arr[mid]
    else:
        return (arr[mid]+arr[mid+1])/2.0

def activityNotifications(expenditure, n, d):
    n_count = 0
    l = take_mid = 0
    r = d-1
    cur = d
    if d%2 == 1:
        take_mid = 1
    mid = l + (r-l)/2
    
    sorted_window = sorted(expenditure[l:r+1])
    
    while(cur<len(expenditure)):
        
        med = calc_median(sorted_window, take_mid, mid)
        if expenditure[cur] >= 2*med:
            n_count+=1
        
        # Move Window
        sorted_window.pop(bisect.bisect_left(sorted_window,expenditure[l]))
        sorted_window.insert(bisect.bisect(sorted_window, expenditure[cur]),expenditure[cur])
        l+=1
        cur+=1
    
    return n_count
