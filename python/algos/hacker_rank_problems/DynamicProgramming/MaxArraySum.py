# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp={}
    dp[0]=arr[0]
    if(len(arr)==1):
        return arr[0]
    dp[1]=max(arr[1],arr[0])
    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i],arr[i])
    return dp[len(arr)-1]
