import random as r
import flask as fl

################################################################
###                                                          ###
### 2024-02: v0.2                                            ###
### KNOWN ISSUES:                                            ###
###                                                          ###   
################################################################

app = fl.Flask(__name__)
app.config['SECRET_KEY'] = 'big!secret'

@app.route('/')
def welcome():
    return fl.render_template("index.html")

@app.route('/start')
def start():
    def word_list():
        with open("words.txt", "r") as words:
            full_word_list = [line.strip() for line in words]
        return full_word_list
    goal = r.choice(word_list())
    fl.session['goal'] = goal
    
    # playcount = 1
    # wincond = "XXXXX"

    print(goal) ### TEST

    # won = "You won!"
    # lost = f"You lost!\nThe word was: {goal}"
    
    # while playcount <= 6:

    #     playcount += 1
    #     guess = input("Pls guess a 5-letter word:").lower()
        
    #     if guess not in word_list():
    #         print("That's not a real word!")
    #     else:
    #         guess = check_guess(guess, goal)
    #         print(guess)
    #         if guess == wincond:
    #             break

    # if guess == wincond:
    # else:

    return fl.render_template("start.html")

@app.route('/play', methods=["POST"])
def play(output=None, guess=None, playcount=None):

    guess = fl.request.form['guess'].lower()
    goal = fl.session.get('goal', None)

    playcount = 0
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

    return fl.render_template("play.html", output=output, guess=guess, playcount=playcount)