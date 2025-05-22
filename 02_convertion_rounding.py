def round_ans(val):
    """
    Rounds temparatures to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature to be convert in °F
    :return: Converted temperature in °C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature to be convert in °C
    :return: Converted temperature in °F
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)


# Main Routine / testing starts here
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} C is {ans} C")