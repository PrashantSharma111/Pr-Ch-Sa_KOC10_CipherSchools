d = {"Is 1 prime?":{"T":0, "F":1}, "Is every square matrix singular?":{"T":1, "F":0}, "Is 120 factorial of 5?":{"T":1, "F":0},
"Does octopus has three hearts?":{"T":1, "F":0}, "Is python a case sensitive language?":{"T":1, "F":0}}
print("Welcome t0 Group 9's Quiz!\nAnswer every question by typing 'T' for true and 'F' for false.")
score = 0
i = 0
k = list(d.keys())
v = list(d.values())
while(i < len(k)):
    print("Question", str(i+1) + ":", k[i])
    n = input("Enter your answer('T' or 'F'): ").upper()
    if (n not in v[i]):
        print("Incorrect input :(\nTry Again.")
    else:
        x = v[i][n]
        score += x
        i += 1
        if (x == 1):
            print("Correct :)")
        else:
            print("Incorrect :(")
print("Your score is : ", score)