import random
randNumber = random.randint(1, 100)
user = None
chance = 0

print("\t Welcome To Number Guessing Game \t")
msg = input("Would You Like to Play the Game[y/n]:- ")

while msg == 'y':
    while(user != randNumber):
        user = int(input("Enter your guess between (1-100): "))
        chance += 1
        if(user == randNumber):
            print("You guessed it right! Congrats...")
        else:
            if(user > randNumber):
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a larger number")
    else:
        break
print(f"You guessed the number in {chance} guesses")
