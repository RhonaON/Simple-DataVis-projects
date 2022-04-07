# jointplot means you can use two different plots from two different graphs on the same window
# eg - in the case of this exercise - showing the histograms to the side of the scatterplot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'./tempYearly.csv')
print(data)

# trying different kinds of visualisation
# sns.jointplot('Rainfall', 'Temperature', data=data, kind='hex')
sns.jointplot('Rainfall', 'Temperature', data=data, kind='reg')
plt.show()



