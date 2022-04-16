import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')
for x in df.index:
    # print(df.loc[x, 'AL'])
    if df.loc[x, 'AL'] == ':':
        print('dff')
        df.drop(x, inplace=True)
df1 = df.to_csv('test1.csv')
# df.corr()
# df.describe()

df.plot(kind='scatter', x='AL', y='BE')
plt.show()

new_df = df.dropna(inplace=False)
print(df)