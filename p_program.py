# This is a brain test program
def brain_test():
    print("hello, what is your name?")
    name = input("Name: ")

    print("welcome " + name)
    print("would you like to take a brain test " + name)
    reply = input().capitalize()

    if reply == "Yes":
        print("how old are you")
        answer = input()
        if answer >= str(15) : 
            print("What's full of holes but still holds water?")
            ans = input("answer: ").capitalize()
            if ans == "A sponge" or "Sponge":
                print("Very good!! of you " + name + " have a nice day")
            else :
                print("Test failed")
        elif answer < str(15):
            print("What has a face and two hands but no arms or legs?")
            core = input("Answer: ")
            if core == "A clock" or "Clock":
                print("Very good!! of you " + name + " have a nice day")
            else:
                print("Test Failed")
    elif reply == " " or int():
        print("Error: you didnt enter a number")
    else:
        print("ohh okay then " + name )
    
    second_chance = input("would you like to try again:").lower()
    if second_chance == "yes":
        brain_test()
    else:
        print("Goodbye " + name)

brain_test()


