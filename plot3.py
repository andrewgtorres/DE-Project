######### TOP 5 Positions for Summer and Winter vs Number of Transfers #######
##############################################################################
from mpl_toolkits import mplot3d
import json
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# load JSON file containing data
f = open("dataset.json")
data = json.load(f)

###### FILTER SUMMER AND WINTER TRANSFERS #####
# make list of positions in Summer
summer_positions = []
for transfers in data:
    period = transfers['transfer_period']
    if 'Summer' in period:
        position = transfers['position']
        summer_positions.append(position)

# make list of positions in Winter
winter_positions = []
for transfers in data:
    period = transfers['transfer_period']
    if 'Winter' in period:
        position = transfers['position']
        winter_positions.append(position)
period = ['Summer', 'Winter']

#### Make summer top 5 positions and count of transfers using Counter ####
top_positions_sum = []
num_transfers_sum = []
counter = Counter(summer_positions)
most_occur = counter.most_common(5)
for i in range(0,5):
    position = str(most_occur[i])
    position = position[1:-1]
    position_name = position.split(', ')[0] # make list of top 5 position names
    top_positions_sum.append(position_name[1:-1])
    position_count = int(position.split(', ')[1]) # list of top 5 positions' number of transfers
    num_transfers_sum.append(position_count)

#### Make winter top 5 positions and counts of transfers using Counter ####
top_positions_win = []
num_transfers_win = []
counter = Counter(winter_positions)
most_occur = counter.most_common(5)
for i in range(0,5):
    position = str(most_occur[i])
    position = position[1:-1]
    position_name = position.split(', ')[0] # make list of top 5 position names
    top_positions_win.append(position_name[1:-1])
    position_count = int(position.split(', ')[1]) # list of top 5 positions' number of transfers
    num_transfers_win.append(position_count)
ranks = [1,2,3,4,5]

# plot Summer top 5 positions and Winter top 5 positions vs. Number of Transfers
plt.figure(figsize=(7, 7))
plt.scatter(ranks, num_transfers_sum, color='green', linewidths = 3, label="Summer")
plt.scatter(ranks, num_transfers_win, color='blue', linewidths = 3, label="Winter")
for i in range(0,5):
    plt.text(ranks[i], num_transfers_sum[i], top_positions_sum[i], fontsize = 'small')
for i in range(0,5):
    plt.text(ranks[i], num_transfers_win[i], top_positions_win[i], fontsize = 'small')
plt.xticks(np.arange(0, 6, 1))
plt.xlabel("Rank of Position by Number of transfers")
plt.ylabel("Number of Transfers")
plt.title("Top 5 Positions in Summer and Winter Periods")
plt.legend()
plt.savefig('top-5-positions.pdf')