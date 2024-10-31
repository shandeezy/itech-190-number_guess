import random 

def main():
    attempts = 0
    secret_number =random.randrange(100)
    print("I have chosen a number between 1 and 100. Can you guess it?")
    while True:
        guess = input("please guess a number between 1 and 100")
        attempts +=1

        #non numberic condition check
        if guess.isalpha():
            continue
        
        if int(guess) == secret_number:
            #congrats message stating the secret number and how many attempts it took
            print("congrats! secret number was {} and it took you {} attempts".format(secret_number, attempts))
            break

        #if else statement to decide to print the guess too high
        #or guess too low message
        if int(guess) < secret_number:
            print("too low")
            continue 
        else:
            print("too high")
            continue 
       


if __name__ == "__main__":
    main()
