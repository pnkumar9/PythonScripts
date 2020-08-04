def maxSubsetSumNoAdjacent(array):
	
	if not array:
		return 0
	if len(array) == 1:
		return array[0]
	
	#formula = maxsum[i] =max(maxsums[i-1], maxsums[i-2] + array[i])
	
	dp = [0] * len(array)
	
	dp[0] = array[0]
	dp[1] = max(array[1],array[0])
	
	for i in range(2, len(array)):
		
		dp[i] = max(dp[i-1], dp[i-2]+array[i])
		
	return dp[-1]		
    
