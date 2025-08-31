def findKthBit( n: int,k:int) -> str:
    def invert_and_reverse(string:str)->str:
        rev_inv = ""
        for i in string[::-1]:
            if i == "1":
                rev_inv += "0"
            else:
                rev_inv += "1"
        return rev_inv
    def recursor(n:int)->str:
        if n == 1:
            return "0"
        recursed = recursor(n-1)
        return recursed + "1" + invert_and_reverse(recursed)
    return recursor(n)[k-1]

    
print(findKthBit(3,1))