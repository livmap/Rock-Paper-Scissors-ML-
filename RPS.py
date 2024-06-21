# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    # To WIN
    combos = {
        "R": "P",
        "P": "S",
        "S": "R"
    }
    if len(opponent_history) > 2:
        if(prev_play == "R" or prev_play == "S"or prev_play == "P"):
            guess = combos[prev_play]
        else:
            guess = "R"

    return guess

# I Lost / Won
# Why did I lose?
# How can I be better now?
# We have 1000 games