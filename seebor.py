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

#pair plot
sns.pairplot(crash_df)
plt.show()