test = ["bella","label","roller"]


def commonChars(self, words):
   if len(words) == 1:
       return words[0]
   result = []
   chars = set(words[0])      
   for char in chars:
       frequency = min([word.count(char) for word in words])
       result += frequency * [char]

   return result

print ( commonChars(test))
