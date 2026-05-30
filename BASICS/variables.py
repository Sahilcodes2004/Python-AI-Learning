import random



def get_choices():
    player_choice=input("enter a choice9(rock,paper,scissor65)")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}

    return choices


result=get_choices()
print(result)


def check_win(player,computer):
    print(f"you chose {player}computer chose{computer}")
    if player==computer:
     return "It's a tie!"
    elif player=="rock" and computer=="paper":
      return "computer wins"
    elif player=="paper" and computer=="rock":
       return "player wins"
    elif player=="scissor" and computer=="paper":
       return "player wins"
    elif player == "scissor" and computer=="rock":
       return "computer wins!"
    elif player=="rock" and computer=="scissor":
       return "player wins"
       
    
    else:
       return "It's a TIE !"

check_win("rock","paper")

age=25
print(f"jim is {age} years old")