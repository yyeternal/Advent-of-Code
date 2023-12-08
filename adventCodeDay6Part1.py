filepath = "C:\\Users\\jtint\\OneDrive\\Documents\\Advent\\inputday6.txt"

charge = 0 
winningNums = 0 
total = 0 
totalNums = 1
with open("inputday6.txt", 'r') as File:
    lines = File.readlines()
    discard, time = lines[0].split(":")
    discard, records = lines[1].split(":")
    timed = time.split()
    recordd = records.split()
    timess = ""
    recordss = ""
    times = timess.join(timed)
    record = recordss.join(recordd)
    winningNums = 0 
    for i in range(int(times)):
        if i*(int(times)-i) > int(record):
            winningNums += 1
        if i == (int(times)-1):
            total = winningNums
    print(total)
