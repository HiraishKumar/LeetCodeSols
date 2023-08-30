temperatures = [73,74,75,71,69,72,76,73]
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



    # stack=[temperatures[0]]
    # results=[]
    # for i in range(1,len(temperatures)):
    #     index=i
    #     while temperatures[index] < stack[0]:
    #         if index > len(temperatures)-2:
    #             results.append(0)
    #             break
    #         else:
    #             stack.append(temperatures[index])
    #             index+=1
    #     results.append(len(stack))
    #     stack.clear()
    #     stack.append(temperatures[i])
        
    # results.pop()
    # results.append(0)
    # return results
                