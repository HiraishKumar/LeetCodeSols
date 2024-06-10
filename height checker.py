def heightChecker(heights: list[int]) -> int:
    def quick_sort(arr):
        # Base case: arrays with 0 or 1 element are already sorted
        if len(arr) <= 1:
            return arr
        
        # Choose a pivot element (here we are using the last element as the pivot)
        pivot = arr[len(arr) - 1]
        
        # Partition the array into two halves
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        
        # Recursively apply the same logic to the partitions
        sorted_less_than_pivot = quick_sort(less_than_pivot)
        sorted_greater_than_pivot = quick_sort(greater_than_pivot)
        
        # Combine the sorted partitions and the pivot
        return sorted_less_than_pivot + [pivot] + sorted_greater_than_pivot
    expected = quick_sort(heights)
    un_expected = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            un_expected += 1
        else:
            pass
    return un_expected