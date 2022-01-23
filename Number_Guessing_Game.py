# ===========================================================================Thanks for Read Me====================================================================================
actual_number = 55
attempts = 0

while True:
    attempts +=1
    guess = int(input("Guess the number:\n"))
    if guess<actual_number:
        print("Your guess was too low")

    elif guess<actual_number:
        print("Your guess was too high")

    else:
        print(f"You guessed te number in {attempts} attempts")
        break
print("Thanks for playing!")
