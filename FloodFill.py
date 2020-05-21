def dfs(image,newColor,i,j,originalvalue):
    if (i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != originalvalue):
        return
    
    image[i][j] = newColor
    dfs(image,newColor,i-1,j,originalvalue)
    dfs(image,newColor,i+1,j,originalvalue)
    dfs(image,newColor,i,j-1,originalvalue)
    dfs(image,newColor,i,j+1,originalvalue)

def floodFill(image, sr, sc, newColor):
    originalvalue = image[sr][sc]
    if originalvalue != newColor:
        dfs(image,newColor,sr,sc,originalvalue)
        
    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1 
newColor = 2
out = floodFill(image,sr,sc,newColor)
print(out)