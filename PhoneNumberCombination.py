def helper(digits,index,cur,maps,res):
	if index == len(digits):
		res.append(cur)
		return

	s1 = maps[digits[index]]
	for i in range(len(s1)):
		helper(digits,index+1,cur+s1[i],maps,res)




def Phonecombinations(n):

	res = []
	maps = {
	'2':'abc',
	'3':'def',
	'4':'ghi',
	'5':'jkl',
	'6':'mno',
	'7':'pqrs',
	'8':'tuv',
	'9':'qxyz'
	}
	helper(n,0,"",maps,res)
	print(res)

Phonecombinations("23")