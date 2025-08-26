#TODO need to figure out how thsi backtrack works

def calcSubset(A, res, subset, index,ans,target):
    # Add the current subset to the result list
    res.append(subset[:])

    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])
        if sum(subset[:]) == target:
            ans.append(subset[:])

        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1,ans,target)

        # Exclude the current element from the subset (backtracking)
        subset.pop()


def subsets(A,target):
    subset = []
    res = []
    ans=[]
    index = 0
    calcSubset(A, res, subset, index,ans,target)
    return ans


# Driver code
if __name__ == "__main__":
    array = [10,1,2,7,6,1,5]
    target = 8
    ans = subsets(array,target)   

    # Print the generated subsets
    for subset in ans:
        print(subset)