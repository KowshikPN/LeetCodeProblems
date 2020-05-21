def helper(nums,cur,index,res):
    res.append(cur+[])
    for i in range(index,len(nums)):
        cur.append(nums[i])
        helper(nums,cur,i+1,res)
        cur.pop()
    
def subsets(nums):
    res = []
    helper(nums,[],0,res)
    print(res)

subsets([1,2,3])

        