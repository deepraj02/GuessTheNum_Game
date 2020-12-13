import random
randNumber = random.randint(1, 100)
user = None
chance = 0

print("\t Welcome To Number Guessing Game \t")

while True:
    msg = input("Would You Like to Play the Game[y/n]:- ")
    if msg=='y':
        while(user != randNumber):
            user = int(input("Enter your guess between (1-100): "))
            chance += 1
            if(user == randNumber):
                print("\nYou WON,You Guessed it Right ")
                print(f"\tYou guessed the number in {chance} guesses")
            else:
                if(user > randNumber):
                    print("You guessed it wrong! Enter a smaller number")
                else:
                    print("You guessed it wrong! Enter a larger number")
    else:
        print("Hope You Enjoyed the Game.")
        break
