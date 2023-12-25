import plotly.graph_objs as go
import pandas as pd
import os
import math 

DEFAULT_PLOTLY_COLORS=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)']


mycwd = os.getcwd()
print(mycwd)
os.chdir("..")
print(os.getcwd())

fname = 'results/copy_all_results_2.csv'

df = pd.read_csv(fname)

#print(df)

print(df['version'])
df['std_dev'] = [2 * math.sqrt(i * (1 - i) / 1000) for i in df['0no']]

tmp3 = df[df['version'] == 'dwave']
tmp4 = df[df['version'] == '50_4']
tmp5 = df[df['version'] == '100_4']
tmp6 = df[df['version'] == '200_4']
tmp7 = df[df['version'] == 'GAC']

rel3 = list()
rel4 = list()
rel5 = list()
rel6 = list()
rel7 = list()

for i in tmp3['0no']:
    rel3.insert(len(rel3), i)
for i in tmp4['0no']:
    rel4.insert(len(rel4), i)
for i in tmp5['0no']:
    rel5.insert(len(rel5), i)
for i in tmp6['0no']:
    rel6.insert(len(rel6), i)
for i in tmp7['0no']:
    rel7.insert(len(rel7), i)

for i in range(0, len(rel3)):
    rel4[i] = rel4[i] / rel3[i]
    rel5[i] = rel5[i] / rel3[i]
    rel6[i] = rel6[i] / rel3[i]
    rel7[i] = rel7[i] / rel3[i]
    rel3[i] = rel3[i] / rel3[i]



fig = go.Figure([
    go.Scatter(
        name = 'dwave',
        x = tmp3['tests'],
        y = rel3,
        line = dict(color = DEFAULT_PLOTLY_COLORS[0]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '50_4',
        x = tmp4['tests'],
        y = rel4,
        line = dict(color = DEFAULT_PLOTLY_COLORS[1]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = rel5,
        line = dict(color = DEFAULT_PLOTLY_COLORS[2]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = rel6,
        line = dict(color = DEFAULT_PLOTLY_COLORS[3]),
        mode = 'lines',
    ),

    go.Scatter(
        name = 'GAC',
        x = tmp7['tests'],
        y = rel7,
        line = dict(color = DEFAULT_PLOTLY_COLORS[4]),
        mode = 'lines',
    ),
    
])
fig.update_layout(
    xaxis_title = "Deg",
    yaxis_title = "Solutions found (Relative to DWave default)",
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_0no_rel_deg.png")
fig.show()

fig = go.Figure([
    go.Scatter(
        name = 'dwave',
        x = tmp3['tests'],
        y = tmp3['0no'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[0]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '50_4',
        x = tmp4['tests'],
        y = tmp4['0no'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[1]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['0no'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[2]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = tmp6['0no'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[3]),
        mode = 'lines',
    ),

    go.Scatter(
        name = 'GAC',
        x = tmp7['tests'],
        y = tmp7['0no'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[4]),
        mode = 'lines',
    ),
    
])
fig.update_layout(
    xaxis_title = "Deg",
    yaxis_title = "Solutions found",
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_0no_abs_deg.png")
fig.update_yaxes(type='log')
fig.show()

exit(0)