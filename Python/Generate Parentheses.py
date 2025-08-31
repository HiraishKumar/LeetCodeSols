

def generateParenthesis( n: int=3) -> list[str]:
	def dfs(left, right, s):
		if left==3 and right==3:
			res.append(s)
			return None

		if left < n:
			dfs(left + 1, right, s + '(')

		if right < left:
			dfs(left, right + 1, s + ')')

	res = []
	dfs(0, 0, '')
	return res
print(generateParenthesis())
'''
>>>['((()))', '(()())', '(())()', '()(())', '()()()']
'''    
    