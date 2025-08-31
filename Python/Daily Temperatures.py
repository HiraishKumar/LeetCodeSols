temperatures = [5, 6, 7, 3, 1, 4, 8, 5]
'''[1,1,4,2,1,1,0,0]'''
def DailyTemprateures(temperatures:list[int])->list[int]:
    stack = []
    ans = [0] * len(temperatures)
    for index in range(len(temperatures)):
        while stack and temperatures[index] > temperatures[stack[-1]]:
            end=stack.pop()
            ans[end] = index - end
        stack.append(index)
        
    return ans
print(DailyTemprateures(temperatures))

