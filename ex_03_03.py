score = input("Enter Score: ")

try:
    fs = float(score)
except:
    print("Error, Value is out of range.")
    quit()

if fs < 0.0 or fs > 1.0:
    print("Error, score is out of range.")
else:
    if fs >= 0.9:
        print("A")
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    else:
        print("F")