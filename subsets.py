def helper(inp,cur,index):
	if index == len(inp):
		print(cur)
		return 

	helper(inp,cur,index+1)
	helper(inp,cur+inp[index],index+1)


def subsets(inp):
	helper(inp,"",0)

subsets("abc")

'''
Time Complexity = O(2^n)
Space Complexity = O(2^n)
For n = 2^n subsets are being generated.
'''