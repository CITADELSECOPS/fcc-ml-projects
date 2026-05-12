"""FCC SCP #5 — Probability Calculator (Hat draws)."""
import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        if num >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num)
        for b in drawn:
            self.contents.remove(b)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        drawn = h.draw(num_balls_drawn)
        counts = {}
        for b in drawn:
            counts[b] = counts.get(b, 0) + 1
        if all(counts.get(c, 0) >= n for c, n in expected_balls.items()):
            success += 1
    return success / num_experiments
