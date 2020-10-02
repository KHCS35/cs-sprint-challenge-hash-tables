def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for number in a:
        if number < 0:
            cache[number] = -number
    for num in cache:
        if cache[num] in a:
            result.append(cache[num])
    print(cache)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
