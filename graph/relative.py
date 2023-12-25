import plotly.graph_objs as go
import pandas as pd
import os
import math 

mycwd = os.getcwd()
print(mycwd)
os.chdir("..")
print(os.getcwd())

df = pd.read_csv('results/all_results')

print(df)

print(df['version'])
df['std_dev'] = [2 * math.sqrt(i * (1 - i) / 1000) for i in df['0no']]

tmp3 = df[df['version'] == 'dwave']
tmp4 = df[df['version'] == '50_4']
tmp5 = df[df['version'] == '100_4']
tmp6 = df[df['version'] == '200_4']

rel3 = list()
rel4 = list()
rel5 = list()
rel6 = list()

for i in tmp3['0no']:
    rel3.insert(len(rel3), i)
for i in tmp4['0no']:
    rel4.insert(len(rel4), i)
for i in tmp5['0no']:
    rel5.insert(len(rel5), i)
for i in tmp6['0no']:
    rel6.insert(len(rel6), i)

for i in range(0, len(rel3)):
    rel4[i] = rel4[i] / rel3[i]
    rel5[i] = rel5[i] / rel3[i]
    rel6[i] = rel6[i] / rel3[i]
    rel3[i] = rel3[i] / rel3[i]



fig = go.Figure([
    go.Scatter(
        name = 'dwave',
        x = tmp3['tests'],
        y = rel3,
        line = dict(color = 'rgb(31,119,180)'),
        mode = 'lines',
    ),

    go.Scatter(
        name = '50_4',
        x = tmp4['tests'],
        y = rel4,
        line = dict(color = 'rgb(119,180,31)'),
        mode = 'lines',
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = rel5,
        line = dict(color = 'rgb(180,119,31)'),
        mode = 'lines',
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = rel6,
        line = dict(color = 'rgb(180, 31, 119)'),
        mode = 'lines',
    ),
])
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_0no.png")
fig.show()
exit(0)