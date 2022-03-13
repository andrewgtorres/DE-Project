########### Position vs. Number of Transfers #########
######################################################
import json
import numpy as np
import matplotlib.pyplot as plt

# load json file containing data
f = open("dataset.json")
data = json.load(f)


# make list of all positions in dataset
positions = []
for transfers in data:
    position = transfers['position']
    if position in positions:
        continue
    else:
        positions.append(position)

# find # of transfers per position
num_transfers = [0]*len(positions)
for transfers in data:
    position = transfers['position']
    for i in range(len(positions)):
        if position == positions[i]:
            num_transfers[i] += 1

# plot position vs. transfers
plt.figure(figsize=(25, 10))
plt.bar(positions, num_transfers, color ='blue', width = 0.3)
plt.xlabel("Position")
plt.ylabel("Number of Transfers")
plt.title("Transfers by Position")
plt.savefig('transfers-by-position.pdf')