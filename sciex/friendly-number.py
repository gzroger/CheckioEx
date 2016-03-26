import math


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    i = 0
    b = 1
    while abs(number / b) >= base:
        if i == len(powers) - 1:
            break
        b *= base
        i += 1
    n = number / b

    n = round(n * 10 ** decimals) / 10 ** decimals if decimals > 0 else math.trunc(n)
    res = ("{n:.{prec}f}{power}{suffix}").format(n=n, prec=decimals, power=powers[i], suffix=suffix)
    print(res)
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=["", "d", "D"]) == '-1d'
    assert friendly_number(255000000000, powers=["", "k", "M"]) == '255000M'
