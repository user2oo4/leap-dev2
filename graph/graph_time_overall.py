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

tmp3 = df[df['version'] == 'dwave']
tmp4 = df[df['version'] == '50_4']
tmp5 = df[df['version'] == '100_4']
tmp6 = df[df['version'] == '200_4']
tmp7 = df[df['version'] == 'GAC']

abs3 = list()
abs4 = list()
abs5 = list()
abs6 = list()
abs7 = list()
rel3 = list()
rel4 = list()
rel5 = list()
rel6 = list()
rel7 = list()

for i in tmp3['time_to_solution']:
    rel3.append(i)
for i in tmp4['time_to_solution']:
    rel4.append(i)
for i in tmp5['time_to_solution']:
    rel5.append(i)
for i in tmp6['time_to_solution']:
    rel6.append(i)
for i in tmp7['time_to_solution']:
    rel7.append(i)

for i in tmp3['running_time']:
    abs3.append(i)
for i in tmp4['running_time']:
    abs4.append(i)
for i in tmp5['running_time']:
    abs5.append(i)
for i in tmp6['running_time']:
    abs6.append(i)
for i in tmp7['running_time']:
    abs7.append(i)

for i in range(0, len(abs3)):
    abs3[i] += rel3[i]
    abs4[i] += rel4[i]
    abs5[i] += rel5[i]
    abs6[i] += rel6[i]
    abs7[i] += rel7[i]
    rel3[i] = abs3[i]
    rel4[i] = abs4[i]
    rel5[i] = abs5[i]
    rel6[i] = abs6[i]
    rel7[i] = abs7[i]

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
    
])
fig.update_layout(
    xaxis_title = "Deg",
    yaxis_title = "Find time + Time to Solution (relative to DWave)",
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_time_to_solution_rel_deg.png")
fig.show()

fig = go.Figure([
    go.Scatter(
        name = 'dwave',
        x = tmp3['tests'],
        y = abs3,
        line = dict(color = DEFAULT_PLOTLY_COLORS[0]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '50_4',
        x = tmp4['tests'],
        y = abs4,
        line = dict(color = DEFAULT_PLOTLY_COLORS[1]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = abs5,
        line = dict(color = DEFAULT_PLOTLY_COLORS[2]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = abs6,
        line = dict(color = DEFAULT_PLOTLY_COLORS[3]),
        mode = 'lines',
    ),

    go.Scatter(
        name = 'GAC',
        x = tmp7['tests'],
        y = abs7,
        line = dict(color = DEFAULT_PLOTLY_COLORS[4]),
        mode = 'lines',
    ),
    
])
fig.update_layout(
    xaxis_title = "Deg",
    yaxis_title = "Find time + Time to Solution",
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_time_to_solution_abs_deg.png")
fig.update_yaxes(type='log')
fig.show()

exit(0)