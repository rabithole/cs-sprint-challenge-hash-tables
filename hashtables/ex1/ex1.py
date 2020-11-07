packages = [12, 6, 7, 14, 19, 3, 0, 25, 40]
packages3 = [12, 6, 7, 14, 0, 25, 40]
packages2 = [4, 5]
packages1 = [1]


def get_indices_of_item_weights(weights, length, limit):

    dicto = {}
    
    if length == 1:
    	print('Length One')
    	return None

    for i in range(0, length):
    	# Amount needed to be present to equal the limit. 
    	temp = limit - weights[i]

    	if (temp in weights):
    		# key = weights[i]
    		dicto[weights[i]] = weights[i]
    		if dicto[weights[i]] > temp:
    			print('if', (weights.index(temp) ,weights.index(weights[i])))
    			return (weights.index(weights[i]), weights.index(temp))
    		else:
    			print('Else', (weights.index(temp), weights.index(weights[i])))
    			return (weights.index(temp), weights.index(weights[i]))
    	# if dicto == {}:
    	# 	print('Nothin in dicto')
    	# 	return None
    print('Did not find None')
    return None


get_indices_of_item_weights(packages2, len(packages2), 9)

# Return tuple of integers with indeces of the passed in list
# Hihger value index should be in the 0 position of the set. 
# Return None if a match doesn't exist

