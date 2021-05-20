def _partition(array, start, end):
    """
    Partitions a given array from given start and end points

    Returns: index of the pivot value
    """
    # Get pivot, left and right pointers
    pivot_idx = int(( start + end ) / 2)
    pivot = array[pivot_idx]
    left = start
    right = end

    # Iterate until the pivot is reached
    while left < right:

        # Iterate reaching two items that need swapping
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        # If left has hit the pivot, return it
        if left >= right:
            return left
          
        # Swap left and right elements
        array[left], array[right] = array[right], array[left]
    

def _quicksort(array, start, end):
    """
    Recursively quicksorts array from given start and end points

    Returns: None
    """
    # If array is larger than 1, partition and quicksort
    if start < end:
    
        # Partition array
        pivot = _partition(array, start, end)

        # Quicksort partitioned array between start and pivot
        _quicksort(array, start, pivot)
        # Quicksort partitioned array between pivot and end
        _quicksort(array, pivot + 1, end)

def quicksort(array):
    """
    Quicksort entire array by calling recursive quicksort function
    
    Returns: None
    """
    start = 0
    end = len(array) - 1
    _quicksort(array, start, end)


