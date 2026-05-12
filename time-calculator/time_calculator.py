"""FCC SCP #2 — Time Calculator."""


def add_time(start, duration, day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    time_part, ampm = start.split()
    sh, sm = map(int, time_part.split(":"))
    if ampm == "PM": sh += 12
    dh, dm = map(int, duration.split(":"))
    total = sh * 60 + sm + dh * 60 + dm
    days = total // (24 * 60)
    rem = total % (24 * 60)
    new_h, new_m = divmod(rem, 60)
    display_ampm = "AM" if new_h < 12 else "PM"
    display_h = new_h if 1 <= new_h <= 12 else (new_h - 12 if new_h > 12 else 12)
    out = f"{display_h}:{new_m:02d} {display_ampm}"
    if day:
        idx = (days_of_week.index(day.capitalize()) + days) % 7
        out += f", {days_of_week[idx]}"
    if days == 1:
        out += " (next day)"
    elif days > 1:
        out += f" ({days} days later)"
    return out
