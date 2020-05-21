def helper(prefix,suffix,res):
	if len(suffix) == 0:
		res.append(prefix)
		return res

	for i in range(len(suffix)):
		helper(prefix+suffix[i],suffix[:i]+suffix[i+1:],res)

		

def permute(s):
	if len(s) == 0:
		return []
	res = []
	helper("",s,res)
	print(res)

permute("abc")

'''
Time Complexity: 

'''