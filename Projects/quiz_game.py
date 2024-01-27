print ("This is a quiz game!")
print ("Do you want to play?")

question = input("Choose your option 'yes or no': ").lower()

if question != "yes":
    quit()
print("Let's get started!")

score = 0
answer = input("What are Linux, Mac and Windows? ").lower()
if answer == "operating systems" or answer == "os":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

answer = input("What is CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is DHCP? ").lower()
if answer == "dynamic host configuration protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the long form for OSI model? ").lower()
if answer == "open system interconnecting":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Your score is {score} and You answers are {score/5 * 100}% correct.")