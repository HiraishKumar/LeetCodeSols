class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(" ")
        test = len(searchWord)
        for i in range(len(arr)):
            if len(arr[i]) >= test and searchWord == arr[i][:test]:
                return i+1
        return -1
        