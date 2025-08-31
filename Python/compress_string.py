characters = ["a","a","b","b","c","c","c"]

def compress( chars: list[str]) -> int:
    i = 0
    write = 0 
    while i < len(chars):
        it = chars[i]
        j = i 
        count = 0
        while j < len(chars) and it == chars[j]:
            count += 1
            j += 1
        chars[write] = it
        write +=1
        if count != 1:
            for k in (str(count)):
                chars[write] = k
                write += 1
        i = j 
    return write
            
print (compress(characters))
print (characters)