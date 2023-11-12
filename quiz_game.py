print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
Score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")

print("You got " + str(Score) + "questions correct!")
print("You got " + str((Score / 4) * 100) + "%.")
