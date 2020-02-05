import collections

""" Consider any array of non-negative integers. A second array is forming by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. """

""" finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) """


""" def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
 """

""" def finder(arr1, arr2):

    # if the key is not in the dictionary, it will just add the key to it
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] =+ 1

    print(d)
    for num in arr1:
        if d[num] == 0:
            return num
        else: 
            d[num] -= 1

    print(d)
print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])) """

def finder(arr1, arr2): 
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2:
        result^=num

    return result

print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))