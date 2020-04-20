import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


jsons = []
for num in range(23):
    with open(f"pp/_benchmarks_results/ver_test_BasicExperimentSuite_Town01-{num}/metrics.json") as fil:
        jsons.append(json.load(fil))

exp = [[], [], [], []]
for num in range(23):
    a, b ,c, d  = jsons[num]['average_speed']['1.0']
    exp[0].append(a)
    exp[1].append(b)
    exp[2].append(c)
    exp[3].append(d)
    print(a,b,c,d)

df = pd.DataFrame({
        'Scenario one':exp[0],
        'Scenario two':exp[1],
        'Scenario three':exp[2],
        'Scenario four':exp[3]
        })

bplot = sns.boxplot(data=df)
bplot.set(ylabel='Kilometres driven')
plt.tight_layout()
plt.show()

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
