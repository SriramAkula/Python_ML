def check_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt < 3:
        if guess.lower()==answer.lower():
            print("Correct Answer\n")
            score=score+1
            still_guessing = False
        else:
            if attempt < 2:
                guess=input("Wrong answer,try again\n")
            attempt +=1 
    if attempt == 3:
        print("The correct answer : ",answer)   
                  
score = 0
print("Guess the Animal")
guess1=input("Which Bear lives at the North Pole?\n")
check_guess(guess1,"polar bear")
guess2=input("Which is the fastest land animal?\n")
check_guess(guess2,"Cheetah")
guess3=input("Which is the largest animal?\n")
check_guess(guess3,"Blue Whale")
print("Your Score is ",score)