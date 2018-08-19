import pandas as pd
import matplotlib.pyplot as plt


col_names = ['Date', 'Names']
df = pd.read_csv('2018-08-18-data_export.csv', names=col_names)

x = df.groupby(['Date', 'Names']).size().unstack()

my_data = x.fillna(value=0, inplace=True)

test = x.plot.bar()
test.set_ylabel("Number of Logins")

plt.show()