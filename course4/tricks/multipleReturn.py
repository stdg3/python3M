def findMinMax (data):
	minNum = min(data)
	maxNum = max(data)
	return minNum, maxNum # equal return (minNum, maxNum)
	# return( min, max) desekte demesekte iki ve daha fazla return ifadeler tuple tipinde döner

minimum, maximum = findMinMax([1,5,7,8,0])

print ("min {}, max {}".format(minimum, maximum))