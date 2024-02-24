################################################################
###                                                          ###
### 2024-02: v0.1                                            ###
### KNOWN ISSUES:                                            ###
###   - too many functions                                   ###
###   - randint could be changed                             ###
###   - input that's not in word list doesn't count as try,  ###
###     will loop forever                                    ###
###   - namespace missing                                    ###
###                                                          ###   
################################################################

import random as r

def word_list():
    with open("words.txt", "r") as words:
        full_word_list = [line.strip() for line in words]
    return full_word_list ### last index == 5756

# print(word_list()) ### TEST

def random_word(w_list):
    return w_list[r.randint(0, len(w_list)-1)]

# print(random_word(word_list())) ### TEST

def is_real_word(guess, w_list):
    return guess in w_list ### we convert to lower in next_guess() as per req

# print(is_real_word("about", word_list())) ### TEST

def next_guess(w_list):
    pls_guess = input("Pls guess a 5-letter word:").lower()
    while not is_real_word(pls_guess, w_list):
        print("That's not a real word!")
        pls_guess = input("Pls guess again:").lower()
    return pls_guess

# next_guess(word_list()) ### TEST

def check_guess(guess, goal):

    output = ""

    for i in range(len(guess)):

        if guess[i] in goal:

            if guess[i] == goal[i]:
                output += "X"

            elif guess[i] != goal[i]:

                if guess.count(guess[i]) == goal.count(guess[i]) or guess[i] in goal[i:-1]: ### guess char count same in guess and goal OR char will occur later in goal, except last index
                    output += "O"

                elif guess[i] == goal[-1] or guess[i] not in goal[i:]: ### char will be the last char of goal OR not occur in the rest of the goal (we already marked this as "O")
                    output += "_"

        else: ### guess[i] not in goal
            output += "_"

    return output

# check_guess("trani", "train") ### TEST

def play():
    goal = random_word(word_list())
    # print(goal) ### TEST

    playcount = 1
    wincond = "XXXXX"
    won = "You won!"
    lost = f"You lost!\nThe word was: {goal}"
    
    while playcount <= 6:
        playcount += 1
        thisplay = next_guess(word_list())
        didyouwin = check_guess(thisplay, goal)
        print(didyouwin)
        if didyouwin == wincond:
            break
    
    if didyouwin == wincond:
        return print(won)
    else:
        return print(lost)

play()