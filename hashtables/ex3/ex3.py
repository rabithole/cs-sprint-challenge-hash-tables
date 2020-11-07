listList = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = []

    for array in arrays:
        for element in array:
            if element not in dict:
                dict[element] = 1
                # print(dict[element])
            else: 
                dict[element] += 1
                # print(dict[element])
    # print(dict)
    for key in dict:
        # print('Dict key', dict[key], 'Array length', len(arrays))
        if dict[key] == len(arrays):
            result.append(key)

    print(result)
    return result

# intersection(listList)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
