
from random import choice

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in ["rock", "paper", "scissors"]:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(["rock", "paper", "scissors"])
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" and c == "rock":
    print("It's a tie!")
elif u == "rock" and c == "paper":
    print("The computer wins")
elif u == "rock" and c == "scissors":
    print("The user wins")

elif u == "paper" and c == "rock":
    print("The computer wins")
elif u == "paper" and c == "paper":
    print("It's a tie!")
elif u == "paper" and c == "scissors":
    print("The user wins")

elif u == "scissors" and c == "rock":
    print("The computer wins")
elif u == "scissors" and c == "paper":
    print("The user wins")
elif u == "scissors" and c == "scissors":
    print("It's a tie!")


def determine_winner(user_choice, computer_choice):
    #return "paper"
    """
    This function determines the winner of the rock, paper, scissors game.
    The parameters are the user's choice and the computer's choice.
    The parameters are strings.
    The function will return the winning choice.
    The winning choice will be compared to the parameters to determine the winner.
    
    Invoke like this: determine_winner("rock", "scissors")
    """
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"




if __name__ == "__main__":





    valid_selections = ["rock", "paper", "scissors"] # only have to update in one place

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_selections)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    #if u == "rock" and c == "rock":
    #    print("It's a tie!")
    #elif u == "rock" and c == "paper":
    #    print("The computer wins")
    #elif u == "rock" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "paper" and c == "rock":
    #    print("The computer wins")
    #elif u == "paper" and c == "paper":
    #    print("It's a tie!")
    #elif u == "paper" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "scissors" and c == "rock":
    #    print("The computer wins")
    #elif u == "scissors" and c == "paper":
    #    print("The user wins")
    #elif u == "scissors" and c == "scissors":
    #    print("It's a tie!")

    winner = determine_winner(u,c)
    if winner == u:
        print("YOU WON")
    elif winner == c:
        print("COMPUTER WON")
    else:
        print("TIE")
