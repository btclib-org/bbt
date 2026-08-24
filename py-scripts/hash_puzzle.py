# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Search increasing nonces for a sha256 hash with a run of leading zeros.

Times how long each extra zero takes to find, and plots the counts.
"""

import hashlib
import time
from typing import List, Optional

import matplotlib.pyplot as plt

msg = input('insert string (return for "Hello, world!"): ')
if msg == "":
    msg = "Hello, world!"

zerostr = input("number of required zeros (return for 4 zeros): ")
zeros = 4 if zerostr == "" else int(zerostr)
assert zeros > 0, "the number of zeros to look for must be greater than zero"

print(f"\nstring is: {msg}")
print(f"{zeros} required zeros")

# n[i] is used to count the results starting with i+1 zeros
n: List[int] = []
maxEval = pow(16, zeros + 1)
i = j = 0
# None rather than 0, which is a nonce the search can return: with 0 as
# the sentinel a hash found at i == 0 leaves the loop running and the
# report reading the exhausted values instead of the found ones
nonce: Optional[int] = None
# the loop below binds these, and the report at the end reads them: what
# says the loop runs is that maxEval is at least 256, which is arithmetic
# rather than control flow, so bind them here and let the report be safe
string = hashValue = ""
start = time.time()
while i < maxEval and nonce is None:
    string = msg + str(i)
    hashValue = hashlib.sha256(string.encode()).hexdigest()
    while hashValue[j] == "0":
        if j < len(n):
            n[j] += 1
        else:
            n.append(1)
            elapsed = time.time() - start
            report = f"{j+1} zeros found {n}"
            if 0 < elapsed <= 600:
                report += f" in {round(elapsed)} seconds at "
                report += f"{round(i/elapsed)} hash/s"
            elif 600 < elapsed <= 36000:
                report += f" in {round(elapsed/60)} minutes at "
                report += f"{round(i/elapsed)} hash/s"
            elif elapsed > 36000:
                report += f" in {round(elapsed/3600)} hours at "
                report += f"{round(i/elapsed)} hash/s"
            print(report)
            if j == zeros - 1:
                nonce = i
        j += 1
    j = 0
    i += 1

if nonce is not None:
    print("nonce:", nonce)
    print(string)
    print(hashValue)
else:
    print("nonce not found")


# Now plot the result in a bar chart

# len(n) and not zeros: the two agree only by luck. A search that
# exhausts leaves n shorter, and plt.bar refuses two shapes that differ;
# a hash carrying more zeros than were asked for leaves it longer, and
# plt.bar accepts that by broadcasting x, drawing every bar at the first
# tick. len(n) is the length that matches either way
x = range(1, len(n) + 1)
plt.bar(x, n)
plt.xlabel("Leading zeros")
plt.ylabel("Occurrences")
plt.show()

# It is better to use a logarithmic scale for Y axis
plt.bar(x, n, log="true")
plt.xlabel("Leading zeros")
plt.ylabel("Occurrences")
plt.show()
