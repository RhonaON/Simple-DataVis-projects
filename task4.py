# Heatmap is another tool within the seaborn library
# used to visualise when there is a low amount or a high amount of something in a dataset
# using heatmaps sometimes requires data to be reorganised
# for example when using a csv (comma separated file)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'./birthYearly.csv')

print(data)

# before we run our heatmap we need to format the data coming from our csv file
# we are going to pivot month, year and births so our data is in a nice matrix format
dataP = data.pivot('month', 'year', 'births')
# prints data out in nice matrix format
print(dataP)

# we pass heatmap our data
# annot='True' means we want our numbers inside our data on the heatmap
# fmt = format = 'd' means we want our numbers in decimal/integer data
sns.heatmap(dataP, annot=True, fmt='d')

plt.show()