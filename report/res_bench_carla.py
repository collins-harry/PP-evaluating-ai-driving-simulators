import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

with open("pp/_benchmarks_results/ver_test_BasicExperimentSuite_Town01-1/metrics.json") as f:
    bench_one = json.load(f)

print(bench_one)





# df_meas = pd.read_csv("pp/ver_test_BasicExperimentSuite_Town01-1/.csv")
# df_sum = pd.read_csv("pp/test_BasicExperimentSuite_Town01-5/summary.csv")

# print(df_sum)

# print(df['score'])
# df_one = df.loc[:34, ['score', 'progress reward', 'lane deviation penalty', 'gforce penalty']]
# df_one.rename(columns={
#     'score': 'Total score',
#     'progress reward':'Progress\nreward',
#     'lane deviation penalty': 'Lane deviation\npenalty',
#     'gforce penalty': 'Gforce\npenalty'}, 
#     inplace=True)
# # df_one.plot.box(
# bplot = sns.boxplot(data=df_one)
# plt.tight_layout()
# plt.show()
# print(df_one)
# 'episode #',
# 'score'
# 'progress reward'
# 'lane deviation penalty'
# 'gforce penalty'
# 'got stuck'
# 'start'
# 'end'
#
