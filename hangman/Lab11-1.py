print("Hangman Game. You have 8 chances. Good luck!")
secret_word = "szczecin"
guess_string = ""
Health = 8

while Health > 0:
    try:
        Gamer = input("\nGuess a letter :")
        Gamer = Gamer.lower()
        guess_string += Gamer
    except:
        print("enter the letter")

    word_left = 0

    for char in secret_word:
        if char in guess_string:
            print(char, end="")
        else:
            print("_", end="")
            word_left += 1

    if word_left == 0:
        print("\nWon")
        break

    if Gamer not in secret_word:
        Health -= 1
        print(f"\nYou have {Health} chances left, yet. ")

        if Health == 0:
            print("You Died")