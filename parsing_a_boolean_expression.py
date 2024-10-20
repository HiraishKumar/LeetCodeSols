test_string1 = "&(|(f))"
test_string2 = "|(f,f,f,t)"
test_string3 = "!(&(f,t))"

def AND (sub_exp:list) -> str:
    return "t" if all(e == "t" for e in sub_exp) else "f"
def NOT (sub_exp:list) -> str:
    return "f" if sub_exp[0] == "t" else "t"
def OR  (sub_exp:list) -> str:
    return "t" if any(e == "t" for e in sub_exp) else "f"

def ParseBoolean(expression:str)->bool:
    opr = []
    exp = []

    for ch in expression:
        if ch ==',':
            pass
        elif ch in ["(","t","f"]:
            exp.append(ch)
        elif ch in ["&","|","!"]:
            opr.append(ch)   
        elif ch == ")":
            sub_exp = []
            while exp[-1] != "(":
                sub_exp.append(exp.pop())
            exp.pop() #removes the trailing "("
            operand = opr.pop()
            if operand == "&":
                exp.append(AND(sub_exp))
            elif operand == "|":
                exp.append(OR(sub_exp))
            elif operand == "!":
                exp.append(NOT(sub_exp))
    return exp[0] == "t"
print(ParseBoolean(test_string1))
print(ParseBoolean(test_string2))
print(ParseBoolean(test_string3))