temperatures = [73,74,75,71,69,72,76,73]

def DailyTemprateures(temperatures:list[int])->list[int]:
    stack=[]
    results=[]
    for i in temperatures:
        duration=0
        if stack and i > stack[0]:            
            while stack and i > stack[0]:
                stack.pop()
                duration+=1
                
print(DailyTemprateures(temperatures))