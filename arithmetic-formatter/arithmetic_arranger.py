"""FCC SCP #1 — Arithmetic Formatter."""


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    top, mid, bot, ans = [], [], [], []
    for p in problems:
        parts = p.split()
        if len(parts) != 3:
            return "Error: Operator must be '+' or '-'."
        a, op, b = parts
        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        if not (a.isdigit() and b.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."
        w = max(len(a), len(b)) + 2
        top.append(a.rjust(w))
        mid.append(op + b.rjust(w - 1))
        bot.append("-" * w)
        if show_answers:
            result = str(int(a) + int(b)) if op == "+" else str(int(a) - int(b))
            ans.append(result.rjust(w))
    arranged = "    ".join(top) + "\n" + "    ".join(mid) + "\n" + "    ".join(bot)
    if show_answers:
        arranged += "\n" + "    ".join(ans)
    return arranged
