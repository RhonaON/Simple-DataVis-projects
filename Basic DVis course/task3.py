# seaborn library is built on top of matplotlib
# it is used for making statistical graphics and has fascinating themes
# whereas matplotlib is used for making basic graphs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'tempYearly.csv')

sns.set(rc={'figure.figsize':(12,6)})
# sns.scatterplot(x='Year', y='Temperature', data = df)
# regplot for regression line
sns.regplot(x='Rainfall', y='Temperature', data = df)
plt.show()
