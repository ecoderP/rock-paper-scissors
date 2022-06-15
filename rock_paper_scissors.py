import random

def get_user_pick():

    global rock_pick
    global paper_pick
    global scissors_pick

    rock_pick = "Rock"
    paper_pick = "Paper"
    scissors_pick = "Scissors"

    #get user input
    userPick = input("""
    Enter one these to pick a choice:
    R for Rock
    P for paper
    S for Scissors
    """)
    # covert pick to lower case
    global userPick_lowercase
    userPick_lowercase = userPick.lower()
    return userPick_lowercase

#get random pick from cpu
def get_cpu_pick():
    possible_picks = ["Rock", "Paper", "Scissors"]
    CPU_pick = random.choice(possible_picks)
    return CPU_pick

#check if user pick is valid
def check_user_pick():
  if (userPick_lowercase == "r" or userPick_lowercase == "p" or userPick_lowercase == "s"):
    if userPick_lowercase == "r":
        userPick_lowercase = rock_pick
    elif userPick_lowercase == "p":
        userPick_lowercase = paper_pick
    else:
        userPick_lowercase = scissors_pick
    
    get_cpu_pick()
  else:
    print("Your entry is invalid. Please pick from the available options.")
    get_user_pick()



  
#rock-paper-scissors
def rock_paper_scissors():
  get_user_pick()
  check_user_pick()
  print(userPick_lowercase)
rock_paper_scissors()
