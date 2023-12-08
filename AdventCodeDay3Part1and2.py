filepath = "C:\\Users\\jtint\\OneDrive\\Documents\\Advent\\inputday3.txt"
grid = []
sum = 0

with open(filepath, "r") as myFile:
    for line in myFile:
        grid.append(line.strip())

#Part 1
def containsSymbol(string):
    for char in string:
        if not (char.isdigit() or char=='.'):
            return True
    return False

def isAdjacent(row, start, end):
    if start > 0:
        start-=1
    if end < len(grid[row]) - 1:
        end+=1
    
    if containsSymbol(grid[row][start]) or containsSymbol(grid[row][end]):
        return True
    if row > 0:
        if containsSymbol(grid[row-1][start:end+1]):
            return True
    if row < len(grid) - 1:
        if containsSymbol(grid[row+1][start:end+1]):
            return True
    return False    
        
for row in range(0, len(grid)):
    line = grid[row]
    x = 0
    # print(line)
    while x < len(line):
        if line[x].isdigit():
            end = x
            while (end < len(line) - 1) and line[end+1].isdigit():
                end+=1
            if isAdjacent(row, x, end):
                sum+=int(line[x:end+1])
            x = end
        x+=1
print(sum)


#Part 2
sum = 0
def adjacentNums(row, col):
    # Note: I looked at the grid manually and saw there were no *s on the edges, so I'm not worrying about borders
    nums = []
    for row in range(row - 1, row +2):
        line = grid[row]
        x = col -1
        while x < col+2:
            if line[x].isdigit():
                end = x
                while (x>0) and line[x-1].isdigit():
                    x-=1
                while (end < len(line) - 1) and line[end+1].isdigit():
                    end+=1
                nums.append(line[x:end+1])
                x = end
            x+=1
    return nums

for row in range(0, len(grid)):
    line = grid[row]
    for col in range(0, len(line)):
        if line[col] == "*":
            nums = adjacentNums(row, col)
            if len(nums) == 2:
                sum+=int(nums[0]) * int(nums[1])
print(sum)