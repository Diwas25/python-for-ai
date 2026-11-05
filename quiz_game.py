#project 1 
# youtube - https://www.youtube.com/watch?v=NpmFbWO6HPU&list=PPSV

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("OK! Let's play! :) ")
score = 0

answer = input("what does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct !!")
    score += 1
else:
    print("Incorrect !!")

answer = input("what does GPU stand for? ").lower()

if answer == "graphical processing unit":
    print("Correct !!")
    score += 1
else:
    print("Incorrect !!")

answer = input("what does SIM stand for? ").lower()

if answer == "subscriber identity module":
    print("Correct !!")
    score += 1
else:
    print("Incorrect !!")

answer = input("what does ATM stand for? ").lower()

if answer == "autometic teller machine":
    print("Correct !!")
    score += 1
else:
    print("Incorrect !!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score / 4) * 100) + "%.")