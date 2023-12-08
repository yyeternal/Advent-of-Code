total = 0

maxRed = 12
maxBlue = 14
maxGreen = 13

colors = {
    "red": maxRed,
    "blue": maxBlue,
    "green": maxGreen
}


with open('input.txt', 'r') as File:
    for line in File:
        correct = True
        game, data = line.split(": ")
        gameName, gameId = game.split()
        trials = data.split(";")
        
        for trial in trials:
            numColor = trial.split(",")
            for colour in numColor:
                num, color = colour.split()
                if (int(num) > maxBlue and color == "blue") or (int(num) > maxGreen and color == "green") or (int(num) > maxRed and color == "red"):
                    correct = False 
        if correct:
            total += int(gameId)
                
    print(total)






            