# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Search each listed prime for the curves of highest prime order.

For every prime p, scans a and b over range(200) in ascending order, and keeps
the first curve of highest prime order below p and the first of highest prime
order overall. Each is printed as the Curve() call that builds it, in the form
ellipticcurves.py writes.

The cofactor printed is 1: the search counts points, so the order printed is
the curve's full point count. Curve() checks only that the cofactor times the
order lies in Hasse's interval, so it accepts 1 here, and also any larger
cofactor whose product with the order stays in the interval.
"""

from ecc.number_theory import mod_sqrt_var


def isprime(n: int) -> bool:
    """Return True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i ** 2 <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


primes = [
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
]
for prime in primes:
    maxorder = 0
    maxordera = -1
    maxorderb = -1
    maxorderlessthanprime = 0
    maxorderlessthanprimea = -1
    maxorderlessthanprimeb = -1
    for a in range(200):
        for b in range(200):
            order = 0
            for x in range(prime):
                y2 = ((x * x + a) * x + b) % prime
                if y2 == 0:
                    order += 1
                    # print("#", order+1, " ", x, ", ", 0, "  #####", sep="")
                    continue
                try:
                    y = mod_sqrt_var(y2, prime)
                    assert (y * y) % prime == y2
                    # print("#", order+1, " ", x, ",", y, sep="")
                    # print("#", order+2, " ", x, ",", prime-y, sep="")
                    order += 2
                except ValueError:
                    # y2 has no square root mod prime, most x in the search do
                    # not: mod_sqrt_var raises rather than the loop finding one
                    continue
            order += 1
            if isprime(order):
                # print(a, b, prime, "gen", order)
                if order > maxorder:
                    maxorder = order
                    maxordera = a
                    maxorderb = b
                if order > maxorderlessthanprime and order < prime:
                    maxorderlessthanprime = order
                    maxorderlessthanprimea = a
                    maxorderlessthanprimeb = b

    if maxorderlessthanprimea != -1:
        gx = 0
        gy = -1
        while gy == -1:
            y2 = (
                (gx ** 2 + maxorderlessthanprimea) * gx + maxorderlessthanprimeb
            ) % prime
            try:
                y = mod_sqrt_var(y2, prime)
                assert (y * y) % prime == y2
                gy = y
            except ValueError:
                gx += 1
        print(
            f"ec{prime}_{maxorderlessthanprime} = Curve({prime}, "
            f"{maxorderlessthanprimea}, {maxorderlessthanprimeb}, ({gx}, {gy}), "
            f"{maxorderlessthanprime}, 1, False)",
        )
    if maxordera != -1:
        gx = 0
        gy = -1
        while gy == -1:
            y2 = ((gx ** 2 + maxordera) * gx + maxorderb) % prime
            try:
                y = mod_sqrt_var(y2, prime)
                assert (y * y) % prime == y2
                gy = y
            except ValueError:
                gx += 1
        print(
            f"ec{prime}_{maxorder} = Curve({prime}, {maxordera}, {maxorderb}, "
            f"({gx}, {gy}), {maxorder}, 1, False)",
        )
