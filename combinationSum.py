def helper(inp,cur,index,res,target):
    if target == 0:
        res.append(cur+[])
        return
    if target < 0:
        return
    
    for i in range(index,len(inp)):
        cur.append(inp[i])
        helper(inp,cur,i,res,target-inp[i])
        cur.pop()

def combinationSum(candidates, target):
    if len(candidates) == 0:
        return []
    res = []
    helper(candidates,[],0,res,target)
    print(res)

combinationSum([2,3,4],7)

