def subsequence(source:str,target:str)->bool:
    len1 = len(source)
    left = 0

    for letter in target:
        right = left
        while right < len1:
            next_letter = chr(((ord(letter)-97+1)%26)+97)
            if source[right] == letter or source[right] == next_letter:
                left = right + 1
                break
            right += 1
            if right == len1:
                return False
    return True



def increment(letter:str)->str:

    asc = ord(letter)
    print(letter+": "+str(asc))
    ans = chr(((asc-97+1)%26)+97)
    print("the Subsequebt is :"+str(ans) )


def canMakeSubsequence(str1, str2):
    ptr1 ,ptr2 = 0,0
    len1,len2  = len(str1),len(str2)

    def next_letter(char):
        return chr(((ord(char)-97-1)%26)+97) 

    while ptr1 < len1 and ptr2 < len2:
        if str1[ptr1] == str2[ptr2] or str1[ptr1] == next_letter(str2[ptr2]):
            ptr2+=1
        ptr1+=1
 
    return ptr2 == len2



str_1 = "zc"
str_2 = "ad"
print(canMakeSubsequence(str_1,str_2))
