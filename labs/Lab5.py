import random

correct_number = random.randint(1, 10)

has_won = False





while not has_won:

    try:

        guess = int(input("Guess a number between 1 and 10 "))


        if guess == correct_number:

            print(f"Congrats. You have guessed the correct number of {correct_number}")

            has_won = True
        elif guess < correct_number:
		
            print(f"Too low")
	
        elif guess > correct_number:
		
            print(f"Too high")
    
        else:

            print("Sorry try again")

    except:

        print("Must be a number between 1 and 10")