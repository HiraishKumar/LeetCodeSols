test_set=[1,2,3]

def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    subset = [] 
    def create_subset(i):
        if i == len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[i])
        create_subset(i+1) 
        subset.pop()
        create_subset(i+1) 
    create_subset(0)
    return res

print(subsets(test_set))