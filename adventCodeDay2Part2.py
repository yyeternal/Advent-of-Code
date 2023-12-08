total = 0
sum = 0 

colors = {
    "red": 0,
    "blue": 0,
    "green": 0
}
maxBlue = 0 
maxGreen = 0
maxRed = 0 

with open('input.txt', 'r') as File:
    for line in File:
        colors["blue"] = 0
        colors["green"] = 0
        colors["red"] = 0 
        correct = True
        game, data = line.split(": ")
        trials = data.split("; ")
        for trial in trials:
            numColor = trial.split(", ")
            for colour in numColor:
                maxNum, color = colour.split()
                if (int(maxNum) > colors["blue"] and color == "blue"):
                    maxBlue = int(maxNum)
                    colors["blue"] = maxBlue
                if (int(maxNum) > colors["green"] and color == "green"):
                    maxGreen = int(maxNum)
                    colors["green"] = maxGreen
                if(int(maxNum) > colors["red"] and color == "red"):
                    maxRed = int(maxNum)
                    colors["red"] = maxRed
        sum = maxRed*maxBlue*maxGreen
        total += sum 

        
                
    print(total)






            