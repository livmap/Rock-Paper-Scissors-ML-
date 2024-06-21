def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
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

