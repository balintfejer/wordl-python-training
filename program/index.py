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
    with open("words.txt", "r") as words:
        full_word_list = [line.strip() for line in words]
    goal = r.choice(full_word_list)
   
    fl.session['goal'] = goal
    fl.session['playcount'] = 0
    fl.session['playlist'] = []

    print(goal) ### TEST
    
    return fl.render_template("start.html")

@app.route('/play', methods=["POST"])
def play(output=None, guess=None, goal=None, playcount=None, playlist=None):

    guess = fl.request.form['guess'].lower()
    goal = fl.session.get('goal', None)
    fl.session['playcount'] += 1
    playcount = fl.session.get('playcount', None)
    this_guess_char_count = 0
    output = ""

    # print(fl.session['playcount']) ### TEST

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

    if guess != goal:
        item = [fl.session.get('playcount'), guess, output]
        fl.session['playlist'].append(item)

    playlist = fl.session.get('playlist', None)

    # print(fl.session.get('playlist')) ### TEST

    return fl.render_template("play.html", output=output, guess=guess, playcount=playcount, playlist=playlist, goal=goal)