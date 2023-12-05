def minCut(self, A):
		n = len(A)
		cuts = [0]*n
		for i in range (n):
			cuts[i]=i 
		def is_palindrome(sub):
			return sub == sub[::-1]n
		
		for i in range (1,n):
			for j in range (i,-1,-1):
					
				if j==0:
					cuts[i]=0
				else:
					min(cuts[i],cuts[j-1]+1)	
				
		return cuts[n-1]