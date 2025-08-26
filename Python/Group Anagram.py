
strs = ["eat","tea","tan","ate","nat","bat"]
# strs =["",""]
def FindAnagram(strs:list(str))->list(list(str)):
    '''finds and groups together words that are anagrams of
     each other into a list which is housed in a nested list
     Time complexity of O(n)'''
    dic={}
    for word in strs:
        temp=''.join(sorted(word))
        if temp in dic:
            dic[temp].append(word)
        else:
            dic[temp]=[word]
    return dic.values()
