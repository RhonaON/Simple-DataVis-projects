# pandas is a library used for data manipulation and analyis
# it is designed to use with relational or labelled data

# matplotlib is a library for creating static, animated and interactive visualisations in python

import pandas as pd
import matplotlib.pyplot as plt

# create dataframes using json file
df = pd.read_json (r'./rain.json')
print(df)

# df.describe() gives us basic statistical analysis of the json file
print('df statistics: ', df.describe())

# we plot data - we need to match what we ascribe to x and y to the headings in the json file
df.plot(x='Month', y = 'Temperature')
df.plot(x='Month', y = 'Rainfall')

# plot graph
plt.show()