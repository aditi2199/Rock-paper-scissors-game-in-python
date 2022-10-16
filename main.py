import random
def gameWon(computer, you):
    if computer == you:
        return None
    elif computer== 'r':
        if you== 's':
            return False
        elif you == 'p':
            return True
    elif computer== 'p':
        if you== 'r':
            return False
        elif you == 's':
            return True
    elif computer== 's':
        if you== 'p':
            return False
        elif you == 'r':
            return True
print(" The Battle of Rock(r), Paper(p) or Scisors(s)?")
randNumber= random.randint(1,3) #rock: choose 1 paper: choose 2 scissorrs: choose 3
if randNumber == 1:
    computer = 'r'
elif randNumber == 2:
    computer = 'p'
elif randNumber == 3:
    computer = 's'
computer = input("Computer's Turn: Rock(r), Paper(p) or Scisors(s)?")
you = input("Player's Turn: Rock(r), Paper(p) or Scisors(s)?")
results= gameWon(computer,you)
print(f"Computer chooses {computer}")
print(f"You chose {you}")
if results == None:
    print("This game is a tie")
elif you:
    print("Congratulations! You Won")
else:
    print("Computer wins! Better luck next time!")
