#PROJECT
def check_guess(player1_choice, player2_choice):
    global score1, score2

    if player1_choice == player2_choice:
        print("It is a tie")
    elif (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "scissors" and player2_choice == "paper") or (player1_choice == "paper" and player2_choice == "rock"):
        print("Player 1 wins this round")
        score1 += 1
    else:
        print("Player 2 wins this round")
        score2 += 1

score1 = 0
score2 = 0

for round in range(1, 4):
    print("Round ",round)
    print("Player 1: 1 - Rock, 2 - Paper, 3 - Scissors")
    player1_choice = int(input("Player 1, enter your choice: "))
    
    print("Player 2: 1 - Rock, 2 - Paper, 3 - Scissors")
    player2_choice = int(input("Player 2, enter your choice: "))
    
    if player1_choice == 1:
        player1_choice = "rock"
    elif player1_choice == 2:
        player1_choice = "paper"
    elif player1_choice == 3:
        player1_choice = "scissors"
    else:
        print("Player 1 made an invalid choice!")
        continue
    
    if player2_choice == 1:
        player2_choice = "rock"
    elif player2_choice == 2:
        player2_choice = "paper"
    elif player2_choice == 3:
        player2_choice = "scissors"
    else:
        print("Player 2 made an invalid choice!")
        continue
    
    check_guess(player1_choice, player2_choice)

print("\nFinal Scores:")
print("Player 1: ",score1)
print("Player 2: ",score2)

if score1 > score2:
    print("Player 1 is the overall winner!")
elif score2 > score1:
    print("Player 2 is the overall winner!")
else:
    print("The game is a tie!")
