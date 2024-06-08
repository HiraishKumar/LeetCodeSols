dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

def replaceWords( dictionary: list[str], sentence: str) -> str:
    class TrieNode:
        def __init__(self) -> None:
            self.children={}
            self.is_end_of_word = False
        
    class Trie:
        def __init__(self) -> None:
            self.root = TrieNode()
        def insert(self,word) -> None:
            node = self.root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.is_end_of_word = True
            
        def shortest_prefix(self,word) -> str:
            node = self.root
            prefix = ""
            for letter in word:
                if letter not in node.children:
                    break 
                
                prefix += letter 
                node = node.children[letter]
                if node.is_end_of_word :
                    return prefix
            return word
                
                    
    trie = Trie()
    for i in dictionary:
        trie.insert(i)
        
    def replace_word(word:str)->str:
        return trie.shortest_prefix(word)
    
    return ' '.join(map(replace_word,sentence.split()))
        
result = replaceWords(dictionary, sentence)
print(result) 