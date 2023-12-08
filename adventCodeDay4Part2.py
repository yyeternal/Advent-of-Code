filepath = "C:\\Users\\jtint\\OneDrive\\Documents\\Advent\\inputday4.txt"

arrayFile=[]
plsWork = [] 
with open(filepath, 'r') as File:
    for line in File:
        arrayFile.append(line)
        plsWork.append(1)

i=0
total = 0 
while i<len(plsWork):
    row=arrayFile[i]
    game, numbers = row.split(":")
    winningNums, myNums = numbers.split("|")
    winners = winningNums.split()
    cards = myNums.split()
    farDown = 0
    for num in cards:
        if num in winners:
            farDown += 1
    for j in range(1, farDown+1):
        if farDown != 0:
            plsWork[i+j] += plsWork[i]     
    i+=1
total = sum(plsWork[0:len(arrayFile)])
print(total)
    