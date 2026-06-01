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
    elif player=="rock" 
       if computer=="scissors":
         return "computer wins"
       else:
          return "paper covers rock ! You Lose."
    elif player=="paper"
       if computer=="scissors":
          return "scissors cuts paper!you lose"
       else:
          return
    
    
   

check_win("rock","paper")

age=25
print(f"jim is {age} years old")