class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ptr1 ,ptr2 = 0,0
        len1,len2  = len(str1),len(str2)

        def next_letter(char):
            return chr(((ord(char)-97-1)%26)+97) 

        while ptr1 < len1 and ptr2 < len2:
            if str1[ptr1] == str2[ptr2] or str1[ptr1] == next_letter(str2[ptr2]):
                ptr2+=1
            ptr1+=1
    
        return ptr2 == len2