from questions import QUESTIONS # importing questions from our questions.py file database

print("Welcome!!", end="\n\n")  

question = input("Press 'y' or 'yes' if you are ready!! ").lower()  #lower() turns our input in lower case

print( end="\n\n")

if question not in ['yes', 'y']:    # checks in the list if input is yes or y
    print("Come again! bye!")
else :
    print("Here we goo!")
    print()

questionCount = 0
correctAnsCount = 0

for each in QUESTIONS:  # looping thro  each item in list of questions
    questionCount += 1  # incrementing by 1 each time loop runs
    print("**********", end="\n\n")
    print(f"Question number: {questionCount}", end="\n\n")
    print(each["question"], end="\n\n") 

    for item in each["options"]:    # with key pair values, looping thro each items of options list in each items from questtion list
        print(item)
    print()
    print("**********", end="\n\n")

    userInput = input("Type the right choice 'A', 'B', 'C', 'D' ").upper().strip()  # strip() to remove missclicked spaces

    if each["answer"] == userInput :    # checking if answer is correct and giving feedback
        correctAnsCount += 1
        print(f"Correct! You got {correctAnsCount} correct out of {questionCount} questions!! ", end="\n\n")
    else :
        print(f"Incorrect!! You got {correctAnsCount} correct out of {questionCount} questions!! ", end="\n\n")
    


print("**********", end="\n\n")
print(f"Well done! You have made {correctAnsCount} correct answers out of {questionCount} questions!! ", end="\n\n")
print("**********")

