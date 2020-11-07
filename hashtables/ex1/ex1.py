packages = [12, 6, 7, 14, 19, 3, 0, 25, 40]


def get_indices_of_item_weights(weights, length, limit):

    dict = {}
    
    for i in range(0, length):
    	temp = limit - weights[i]
    	    	
    	dict[weights[i]] = temp

    print('Printing dict -------', dict[12])

    return None

get_indices_of_item_weights(packages, len(packages), 22)



