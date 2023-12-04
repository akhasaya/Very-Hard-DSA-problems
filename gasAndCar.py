class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
        excess = [x - y for x,y in zip(A,B)]
        # print(excess)
        prefix = []
        summ = 0
        for i in excess:
            summ = summ + i
            prefix.append(summ)
        
        if prefix[-1] < 0:
            return -1
        # print(prefix)
        minn = float("inf") 
        min_i = 0
        for i, val in enumerate(prefix):
            if val < minn:
                minn = val
                min_i = i
        
        for i, val in enumerate(prefix):
            if val - minn < 0:
                return -1
                
        return (min_i + 1) % len(prefix) if minn < 0 else 0
        
