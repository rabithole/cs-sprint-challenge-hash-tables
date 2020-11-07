packages = [12, 6, 7, 14, 19, 3, 0, 25, 40]


def get_indices_of_item_weights(weights, length, limit):

    dict = {}
    dict1 = {}
    
    for i in range(0, length):
    	temp = limit - weights[i]
    	    	
    	dict[weights[i]] = temp
    	for weight in dict:
    		iter = dict[weight]
    		# print('Value', dict[weight], 'key', weight)
    		# dict[weight] = value or iter
    		# weight = key
    		if iter in dict:
    			print('sum equals', dict[weight], weight)


    print('Printing dict -------', dict)

    return None

get_indices_of_item_weights(packages, len(packages), 22)



