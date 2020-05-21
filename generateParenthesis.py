def helper(l,r,cur,res):
    if(l < 0 or r < 0):
        return
    if(l == 0 and r == 0):
        res.append(cur)
        return
    if(l > r):
        return
    
    helper(l-1,r,cur+"(",res)
    helper(l,r-1,cur+")",res)
    
def generateParenthesis(n):
    cur = ""
    res = []
    helper(n,n,cur,res)
    print(res)

generateParenthesis(2)


    