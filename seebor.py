import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#crash dataset from seaborn built-in data
crash_df = sns.load_dataset('car_crashes')

#distribution plots
sns.displot(crash_df['not_distracted'], kde=False)

#joint plots
sns.jointplot(x='speeding', y='alcohol', data = crash_df, kind = 'hex')

#kde plot
sns.kdeplot(crash_df['alcohol'])

#pair plots
# sns.pairplot(crash_df)

tips_df = sns.load_dataset('tips')

sns.pairplot(tips_df, hue='sex', palette='Blues')

plt.show()

