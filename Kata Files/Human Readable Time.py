"""""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

"""


def make_readable(seconds):
    # Do something
    hh = seconds // 3600
    mm = (seconds % 3600) // 60
    ss = (seconds % 60)

    return "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)


print(make_readable(3658))