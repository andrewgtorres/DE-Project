######### LEAGUE VS. TRANSFERS #########
########################################
import json
import numpy as np
import matplotlib.pyplot as plt

#### LOAD JSON FILE CONTAINTING DATA
f = open("dataset.json")
data = json.load(f)

# create x-axis to be list of leagues
leagues = ['Premier League', 'Ligue 1', '1 Bundesliga', 'Serie A', 'Liga Nos', 'Primera Division']
# create y-axis to be list of transfers per league
num_transfers = [0]*6
# count transfers per league and store them in num_transfers
for transfers in data:
    league = transfers['league_name']
    for i in range(0,6):
        if league == leagues[i]:
            num_transfers[i] += 1

# plot League vs Transfers
plt.figure(figsize=(15, 10))
plt.bar(leagues, num_transfers, color ='blue', width = 0.3)
plt.xlabel("League")
plt.ylabel("Total Transfers")
plt.title("Transfers by League")
plt.savefig('transfers-by-league.pdf')


