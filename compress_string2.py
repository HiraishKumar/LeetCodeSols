class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        write = 0
        while i < len (word):
            char = word[i]
            j = i
            count = 0
            while j < len(word) and word[j] == char and count < 9:
                count += 1
                j+=1
            comp.append(str(count))
            comp.append(char)
            i = j
        return ''.join(comp)
            
            