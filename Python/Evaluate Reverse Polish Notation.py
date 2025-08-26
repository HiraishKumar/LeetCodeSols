tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["4","3","-"]

# def evalRPN(tokens:list[str])-> int:
#     stack=[]
#     for i in tokens:
#         if i == '+':
#             stack.append(stack.pop()+stack.pop())
#         elif i == '-':
#             stack.append(stack.pop()-stack.pop())
#         elif i == '*':
#             stack.append(stack.pop()*stack.pop())
#         elif i == '/':
#             x=stack.pop()
#             y=stack.pop()
#             stack.append(int(y/x))
#         else:
#             stack.append(int(i))
#     return stack[0]
# print(evalRPN(tokens))

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                y, x = stack.pop(), stack.pop()
                if x*y<0:
                    stack.append(-(abs(x)//abs(y)))
                else:
                    stack.append(x//y)
            else:
                stack.append(int(c))


                
        return stack[0]