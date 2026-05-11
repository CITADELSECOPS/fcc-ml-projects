"""FCC Multi-Function Calculator: proportions, percentages, conversions."""


def proportion(a, b, c):
    return c * b / a


def percent(part, whole):
    return part / whole * 100


def percent_change(old, new):
    return (new - old) / old * 100


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


if __name__ == "__main__":
    print("proportion(2, 4, 10):", proportion(2, 4, 10))
    print("percent(15, 60):", percent(15, 60))
    print("percent_change(80, 100):", percent_change(80, 100))
    print("km_to_miles(100):", km_to_miles(100))
    print("F=98.6 ->C:", fahrenheit_to_celsius(98.6))
