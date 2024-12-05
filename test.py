_start = "_L__R__R_"
_target = "L______RR"

def canChange(start: str, target: str) -> bool:
    if start == target:
        return True
    waitL = 0   
    waitR = 0    
    ref = list(zip(start, target))
    for curr, goal in zip(start, target):
        if curr == 'R':
            if waitL > 0:
                return False
            waitR += 1  
        if goal == 'L':
            if waitR > 0:
                return False
            waitL += 1
        if goal == 'R':
            if waitR == 0:
                return False
            waitR -= 1 
        if curr == 'L':
            if waitL == 0:
                return False
            waitL -= 1    
    return waitL == 0 and waitR == 0



# def canChange(initial: str, final: str) -> bool:
#     lent = len(initial) 
#     i = lent - 1
#     j = lent - 1

#     res = ["_" for i in range(lent)]

#     def CanMoveR(ini:int,fin:int)->bool:
#         for mov in range(ini+1,fin):
#             if initial[mov] != "_":
#                 return False
#         return True

#     while i >= 0  :
#         if initial[i] == "R":
#             while j >= 0:
#                 if final[j] == "R":
#                     if CanMoveR(i,j) :
#                         res[j] = "R"
#                         j-=1
#                         print(res)
#                         break
#                     else: 
#                         return False
#                 j -= 1    
#         i -= 1

#     result = ""
#     for i in res:
#         result+= i
#     print (res)
#     print(result)
#     # return res == final 



print(canChange(_start,_target))

# print(list(zip(start,target)))
