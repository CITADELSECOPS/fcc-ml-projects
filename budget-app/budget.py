"""FCC SCP #3 — Budget App."""


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(e["amount"] for e in self.ledger)

    def transfer(self, amount, other):
        if not self.withdraw(amount, f"Transfer to {other.name}"):
            return False
        other.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for e in self.ledger:
            desc = e["description"][:23]
            amt = f"{e['amount']:.2f}"[:7]
            items += f"{desc:<23}{amt:>7}\n"
        return title + items + f"Total: {self.get_balance():.2f}"


def create_spend_chart(categories):
    spends = []
    for c in categories:
        spent = sum(-e["amount"] for e in c.ledger if e["amount"] < 0)
        spends.append(spent)
    total = sum(spends)
    pcts = [int(s / total * 10) * 10 for s in spends]
    out = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        out += f"{level:>3}|"
        for p in pcts:
            out += " o " if p >= level else "   "
        out += " \n"
    out += "    " + "-" * (3 * len(categories) + 1) + "\n"
    max_len = max(len(c.name) for c in categories)
    names = [c.name.ljust(max_len) for c in categories]
    for i in range(max_len):
        out += "    "
        for n in names:
            out += " " + n[i] + " "
        out += " \n"
    return out.rstrip("\n")
