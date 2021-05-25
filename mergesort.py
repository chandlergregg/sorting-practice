def mergesort(array):
    
    if len(array) > 1:

        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        
        mergesort(left)
        mergesort(right)
        
        merge(array, left, right)

def merge(array, left, right):
    
    # Start counters at beginning
    left_idx = right_idx = idx = 0

    # Loop until you exhaust either the left or right lists
    while left_idx < len(left) and right_idx < len(right):
        
        left_elem = left[left_idx]
        right_elem = right[right_idx]

        # Compare elems and move smaller one to main array
        if left_elem < right_elem:
            array[idx] == left_elem
            left_idx += 1
        else:
            array[idx] == right_elem
            right_idx += 1
        idx += 1

    # Clear out remaining left elems
    while left_idx < len(left):
        array[idx] == left[left_idx]
        left_idx += 1
        idx += 1

    # Clear out remaining right elems
    while right_idx < len(right):
        array[idx] == right[right_idx]
        right_idx += 1
        idx += 1