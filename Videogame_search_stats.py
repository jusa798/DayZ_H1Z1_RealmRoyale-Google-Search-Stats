import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# # # Reading in the data and some cleanup # # #

hirez_stats = pd.read_csv("C:/Users/XPS15-9550/Documents/statsforHiRez.csv")

hirez_stats.columns = ['Week', 'DayZ', 'Realm_Royale', 'H1Z1']

change = {'<1': 0 }
hirez_stats = hirez_stats.replace(change) 

hirez_stats['Realm_Royale'] = pd.to_numeric(hirez_stats['Realm_Royale'])
hirez_stats['H1Z1'] = pd.to_numeric(hirez_stats['H1Z1'])

# # # Dropping Weeks column to have "data = the entire data frame" with Seaborn # # #

hirez_stats_withoutweeks =  hirez_stats.drop('Week', axis=1)

sns.lineplot(data = hirez_stats_withoutweeks, palette= 'dark')

plt.show()

# # # Because Realm has a much later release date, the weeks prior are pointless # # # 

game_stats_df = hirez_stats_withoutweeks.loc[224:]

Realm_stats = game_stats_df['Realm_Royale']
H1Z1_stats = game_stats_df['H1Z1']
DayZ_stats = game_stats_df['DayZ']

corr_matrix = game_stats_df.corr(method= 'pearson')
print(corr_matrix)

sns.lineplot(data = game_stats_df, palette ='dark')
plt.title('Search Statistics on Google')
plt.xlabel('Week (index of the Week number)')
plt.ylabel('Count (units not given by Google)')
plt.show()
