from random import seed, randint
from quicksort import quicksort

NUM_ARRAYS = 10
ARRAY_LENGTH = 10
MAX_VAL = 999

def create_arrays(is_positive = True):

    # Seed random number generator
    seed(1)

    # Generate arrays
    arrays = []
    for _ in range(NUM_ARRAYS):

        end = MAX_VAL
        if is_positive:
            start = 0
        else:
            start = -MAX_VAL

        array = [ randint(start, end) for _ in range(ARRAY_LENGTH) ]
        arrays.append(array)
    
    return arrays

if __name__ == "__main__":
    arrays = create_arrays(False)
    for array in arrays:
        
        correct = sorted(array)
        quicksort(array)

        if correct == array:
            print("Success!")

