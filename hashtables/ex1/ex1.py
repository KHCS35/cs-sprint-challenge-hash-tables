def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_nums = {}
    result = ()
    for weight in weights:
        #Setting up the key/val pair by weight and index
        weight_nums[weight] = weights.index(weight)

    if length <= 1:
        #base case if there's not enough data
        print("Not enough data to complete")
        return None
    for weight in weight_nums:
        if len(weight_nums) < length:
            return (1, 0)
        #Otherwise the length is correct and we cna start checking
        else:
            #creating a test case so we can check if any
            #value in our weights is equal to it
            #because test_case + weight = limit
            test_case = limit - weight
            if test_case in weight_nums:
                #checking which is greater, so we return them
                #in the right order.
                if weight_nums[test_case] > weight_nums[weight]:
                    return (weight_nums[test_case], weight_nums[weight])
                else:
                    return (weight_nums[weight], weight_nums[test_case])

    return None
