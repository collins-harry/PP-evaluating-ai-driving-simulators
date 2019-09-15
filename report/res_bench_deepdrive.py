import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pp/Deepdrive Benchmark examples__my-baseline-test_2019-08-15__11-26-14PM.csv")
# print(df['score'])
df_one = df.loc[:34, ['score', 'progress reward', 'lane deviation penalty', 'gforce penalty']]
df_one.rename(columns={
    'score': 'Total score',
    'progress reward':'Progress\nreward',
    'lane deviation penalty': 'Lane deviation\npenalty',
    'gforce penalty': 'Gforce\npenalty'}, 
    inplace=True)
# df_one.plot.box(
bplot = sns.boxplot(data=df_one)
plt.tight_layout()
plt.show()
# print(df_one)
# 'episode #',
# 'score'
# 'progress reward'
# 'lane deviation penalty'
# 'gforce penalty'
# 'got stuck'
# 'start'
# 'end'
# 'lap time'

