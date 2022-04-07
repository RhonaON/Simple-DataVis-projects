import pandas as pd
import matplotlib.pyplot as plt

# create dataframes using json file
df = pd.read_json (r'./rain.json')

# we need to set the width and the heigth of the plot before we plot the data
# first no. is width and second is height
plt.figure(figsize=(15,5))

# use pyplot to plot the temperature
plt.plot( df['Month'], df["Temperature"], label='Temperature')
# plt.show()

# use pyplot to plot the rainfall
plt.figure(figsize=(20,5))
plt.plot( df['Month'], df["Rainfall"], label='Rainfall')
# plt.show()

# plot both temp and rainfall together
plt.plot( df['Month'], df["Rainfall"], label='Rainfall')
plt.plot( df['Month'], df["Temperature"], label='Temperature')
plt.legend()
plt.show()