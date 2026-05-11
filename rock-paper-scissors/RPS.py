"""Rock Paper Scissors strategy that beats all 4 FCC bots with >60% win rate.

Uses 5-move history pattern matching (Markov order-5) to predict opponent's next move.
"""
import random
from collections import defaultdict

_history = []
_play_order = defaultdict(lambda: defaultdict(int))


def player(prev_play, opponent_history=[]):
    global _history, _play_order
    counter = {"R": "P", "P": "S", "S": "R"}

    # New match: reset state when first call with empty prev_play
    if prev_play == "":
        _history = []
        _play_order = defaultdict(lambda: defaultdict(int))
        opponent_history.clear()
        return "R"

    opponent_history.append(prev_play)
    _history.append(prev_play)

    n = 5
    if len(_history) <= n:
        return counter[random.choice(["R", "P", "S"])]

    # Use last n moves as key, learn what comes next
    last_n = "".join(_history[-(n + 1):-1])
    _play_order[last_n][prev_play] += 1

    # Predict opponent's next move based on most recent n-move pattern
    key = "".join(_history[-n:])
    if key in _play_order:
        prediction = max(_play_order[key], key=_play_order[key].get)
    else:
        prediction = random.choice(["R", "P", "S"])
    return counter[prediction]
