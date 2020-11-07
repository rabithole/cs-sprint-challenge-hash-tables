theList = [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = []

    for num in a:
    	# print('Num', num)
    	if abs(num) not in dict:
    		dict[abs(num)] = abs(num)
    		# print('Dict', dict)
    	else:
    		result.append(abs(num))
    		# print('Result', result)
    # print('Result', result)
    return result

# has_negatives(theList)


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
