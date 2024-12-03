s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
ans = ""
left = 0
for right in spaces:
    ans += s[left:right]
    ans += " "
    left = right
ans += s[right:]
print(ans) 
print(list(ans))