# def lengthOfLongestSubstring(s:str) -> list:
#     lst=[]
#     test=0
#     lent=len(s)
#     while test <= lent:
#         string=''
#         for i in range(test,lent):
#             letter=s[i]
#             if letter not in string:
#                 string+=letter
#             else:
#                 test=i
#                 lst.append(string)
#                 break
    
#     return lst       
                         
# print(lengthOfLongestSubstring('bbbbb'))

def lengthOfLongestSubstring(s: str) -> int:
    longest_length = 0
    start = 0
    char_index_map = {}  # Keeps track of the most recent index of each character
    
    for end in range(len(s)):
        letter=s[end]
        if letter in char_index_map and char_index_map[letter] >= start:
            start = char_index_map[letter] + 1
        char_index_map[letter] = end
        longest_length = max(longest_length, end - start + 1)
    
    return longest_length

print(lengthOfLongestSubstring('abcabcbb'))


def Longest(s:str)->int:
    char_index={}
    Longest,start=0,0
    for end in range(len(s)):
        letter=s[end]
        if letter in char_index and char_index[letter]>=start:
            start=char_index[letter]+1
        char_index[letter]=end
        Longest=max(Longest,end-start+1)
        
    return Longest
    