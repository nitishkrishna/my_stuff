class Solution(object):
    def __init__(self):
        self.count_list = list()
        self.orig_amount = 0
    
    def coinChange(self, coins, amount):
        self.count_list = [0] + amount*[sys.maxsize]
        
        for i in xrange(1,amount+1):
            val_list = []
            for c in coins:
                if i-c >=0:
                    val_list.append(self.count_list[i-c])
                else:
                    val_list.append(sys.maxsize)
            self.count_list[i] = 1 + min(val_list)
            
        if self.count_list[amount] > amount:
            return -1
        else:
            return self.count_list[amount]
        
# 23.24%
