import random
print("Lets play rock and scissor")
user_score = 0
comp_score = 0
item_list = ['rock','paper','scissor']
round = int(input("How many round do you want:- "))
for i in range(round):
    print(f"Round is {i+1}")
    user_choice = input("please choice between Rock,paper,scissor:- ").strip().lower()
    if user_choice not in item_list:
        print("please choice from three, its invalid choice")
    comp_choice = random.choice(item_list)
    print(f"user choice : {user_choice},comp choice: {comp_choice}")
    if user_choice == comp_choice:
        print("Game is Tied")
    elif user_choice == "rock":
        if comp_choice =="paper":
            print("You loss")  
            comp_score += 1
        else:
            print("you won") 
            user_score += 1     
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You won")
            user_score += 1     
        else:
            print("You Loss") 
            comp_score += 1   
    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("You Loss")  
            comp_score += 1     
        else:
            print("You won")  
            user_score += 1
    print(f"Your score : {user_score} ,computer score : {comp_score}")
print(f"\n Final score after {round} rounds is your score {user_score} and computer score {comp_score}")    
if user_score > comp_score:
    print("You won")
elif comp_score > user_score:
    print("You Loss")
else:
    print("Its a draw")        
