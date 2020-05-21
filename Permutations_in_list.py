def helper(prefix,suffix,res):
	if(len(suffix) == 0):
		res.append(prefix)
		return

	for i in range(len(suffix)):
		helper(prefix+[suffix[i]],suffix[:i]+suffix[i+1:],res)

def permute(nums):
	if len(nums) == 0:
		return []

	res = []
	helper([],nums,res)
	print(res)

permute([1,2,3])