"""
Next Greater Element 
"""


def next_greater_element(arr):
    """
    Finding the next greather element.
    """
    nxt = []
    for i in range(0, len(arr), 1):
        for j in range(0, len(arr), 1):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        if not nxt:
	    print("There is no next greater element for {}".format(arr[i]))
            break
        n = nxt_sort(nxt)
        print("Next greater element of {} is {}".format(arr[i], n[0]))
        nxt = []    


if __name__ == '__main__':
    arr = [11, 13, 12, 21, 3, 10, 2, 4, 23, 89, 45, 100]
    next_greater_element(arr)
