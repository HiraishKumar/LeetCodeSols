test=54845
def isPalindrome(x: int) -> bool:
    '''using two pointers from either side returns False at the first mismatch else returns True'''
    string=str(x)
    left=0
    right=len(string)-1
    while left < right:
        if string[left]==string[right]:
            left+=1
            right-=1
        else:
            return False
    return True

print(isPalindrome(test))