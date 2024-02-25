import random as r

################################################################
###                                                          ###
### 2024-02: v0.1                                            ###
### KNOWN ISSUES:                                            ###
###   [X] too many functions                                 ###
###   [X] false positive (O) when two guess chars in places  ###
###       before the one goal char                           ###
###   [X] randint could be changed                           ###
###   [X] input that's not in word list doesn't count as try,###
###       will loop forever                                  ###
###                                                          ###   
################################################################

def word_list():

    with open("words.txt", "r") as words:
        full_word_list = [line.strip() for line in words]
    return full_word_list

def check_guess(guess, goal):

    this_guess_char_count = 0
    output = ""

    for i in range(len(guess)):

        if guess[i] in goal:

            if guess[i] == goal[i]:

                this_guess_char_count += 1
                output += "X"

            elif guess[i] != goal[i]:

                this_guess_char_count += 1

                if guess.count(guess[i]) > goal.count(guess[i]) and guess[i] == goal[-1]:
                    output += "_"

                elif guess.count(guess[i]) == goal.count(guess[i]) or this_guess_char_count == 1:
                    output += "O"

                elif this_guess_char_count > 1:
                    output += "_"

        else: ### guess[i] not in goal
            output += "_"

    return output

# print(check_guess("carat", "train")) ### TEST
# print(check_guess("taunt", "train")) ### TEST
# print(check_guess("solos", "boobs")) ### TEST
# print(check_guess("aabcd", "qqaqq")) ### TEST

def play():

    goal = r.choice(word_list())
    print(goal) ### TEST

    playcount = 1
    wincond = "XXXXX"
    won = "You won!"
    lost = f"You lost!\nThe word was: {goal}"
    
    while playcount <= 6:

        playcount += 1
        guess = input("Pls guess a 5-letter word:").lower()
        
        if guess not in word_list():
            print("That's not a real word!")
        else:
            guess = check_guess(guess, goal)
            print(guess)
            if guess == wincond:
                break
    
    if guess == wincond:
        return print(won)
    else:
        return print(lost)

# play()