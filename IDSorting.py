# Method: 
# Place strings into bins of equivalent length digits
# Sort within bins 
# Return 

# Get the number of cases and construct array 
num_values = int(input())
array = []
for i in range(num_values):
    array.append(input())


def mod_bucket_sort(array):
    """
    \param array the array of numeric strings to be sorted
    Places strings into buckets of equal length
    Sorts buckets
    Prints sorted array 
    """
    maxval = max([len(x) for x in array])
    buckets = [[] for i in range(maxval)]
    sorted_array = []
    for element in array:
        buckets[len(element) - 1].append(element)
    for bucket in buckets:
        if bucket:
            bucket.sort()
    for bucket in buckets:
        sorted_array.extend(bucket)
    for element in sorted_array:
        print(element)
        
mod_bucket_sort(array)
