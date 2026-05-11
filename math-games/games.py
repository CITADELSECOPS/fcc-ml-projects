"""FCC Three Math Games: arithmetic, exponent, fraction practice."""
import operator
import random
from fractions import Fraction


def arithmetic_game(n=5):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    score = 0
    for _ in range(n):
        sym, op = random.choice(list(ops.items()))
        a, b = random.randint(1, 12), random.randint(1, 12)
        ans = op(a, b)
        user = int(input(f"{a} {sym} {b} = "))
        if user == ans: score += 1
        else: print(f"  wrong, was {ans}")
    print(f"Score: {score}/{n}")
    return score


def exponent_game(n=5):
    score = 0
    for _ in range(n):
        base, exp = random.randint(2, 10), random.randint(2, 5)
        ans = base ** exp
        user = int(input(f"{base}^{exp} = "))
        if user == ans: score += 1
        else: print(f"  wrong, was {ans}")
    print(f"Score: {score}/{n}")
    return score


def fraction_game(n=5):
    score = 0
    for _ in range(n):
        a = Fraction(random.randint(1, 10), random.randint(2, 10))
        b = Fraction(random.randint(1, 10), random.randint(2, 10))
        ans = a + b
        user_in = input(f"{a} + {b} = (as numerator/denominator) ").split("/")
        try:
            user = Fraction(int(user_in[0]), int(user_in[1]))
            if user == ans: score += 1
            else: print(f"  wrong, was {ans}")
        except (ValueError, IndexError):
            print(f"  invalid input; was {ans}")
    print(f"Score: {score}/{n}")
    return score
