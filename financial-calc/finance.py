"""FCC Financial Calculator: future value, loan payment, ROI, compound interest."""


def compound_interest(principal, rate, n_periods, years):
    """A = P(1 + r/n)^(nt)"""
    return principal * (1 + rate / n_periods) ** (n_periods * years)


def future_value_annuity(payment, rate_per_period, n_periods):
    """FV = PMT * (((1+r)^n - 1) / r)"""
    return payment * (((1 + rate_per_period) ** n_periods - 1) / rate_per_period)


def loan_payment(principal, annual_rate, years):
    """Monthly payment for a fully amortized loan."""
    r = annual_rate / 12
    n = years * 12
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def return_on_investment(initial, final):
    return (final - initial) / initial * 100


def amortization_schedule(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    payment = loan_payment(principal, annual_rate, years)
    balance = principal
    schedule = []
    for k in range(1, n + 1):
        interest = balance * r
        principal_paid = payment - interest
        balance -= principal_paid
        schedule.append({
            "month": k, "payment": round(payment, 2),
            "interest": round(interest, 2),
            "principal_paid": round(principal_paid, 2),
            "balance": round(max(balance, 0), 2),
        })
    return schedule
