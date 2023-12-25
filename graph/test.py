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

tmp3 = df[df['version'] == '50_4']
tmp5 = df[df['version'] == '100_4']
tmp4 = df[df['version'] == 'dwave']
tmp6 = df[df['version'] == '200_4']




fig = go.Figure([
    go.Scatter(
        name = '50_4',
        x = tmp3['tests'],
        y = tmp3['0no'],
        line = dict(color = 'rgb(31,119,180)'),
        mode = 'lines',
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp3['tests'],
        y = tmp3['0no'] + 2 * tmp3['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False,
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp3['tests'],
        y = tmp3['0no'] - 2 * tmp3['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(31, 119, 180, 0.3)',
        fill = 'tonexty',
        showlegend = False,
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['0no'],
        line = dict(color = 'rgb(119,180,31)'),
        mode = 'lines',
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp5['tests'],
        y = tmp5['0no'] + 2 * tmp5['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False,
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp5['tests'],
        y = tmp5['0no'] - 2 * tmp5['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(119, 180, 31, 0.3)',
        fill = 'tonexty',
        showlegend = False,
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = tmp6['0no'],
        line = dict(color = 'rgb(180,119,31)'),
        mode = 'lines',
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp6['tests'],
        y = tmp6['0no'] + 2 * tmp6['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False,
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp6['tests'],
        y = tmp6['0no'] - 2 * tmp6['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(180, 119, 31, 0.3)',
        fill = 'tonexty',
        showlegend = False,
    ),

    go.Scatter(
        name = 'dwave',
        x = tmp4['tests'],
        y = tmp4['0no'],
        line = dict(color = 'rgb(180, 31, 119)'),
        mode = 'lines',
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp4['tests'],
        y = tmp4['0no'] + 2 * tmp4['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False,
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp4['tests'],
        y = tmp4['0no'] - 2 * tmp4['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(180, 31, 119, 0.3)',
        fill = 'tonexty',
        showlegend = False,
    ),
])
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_0no.png")
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)
fig.show()
exit(0)

df['std_dev'] = [2 * math.sqrt(i * (1 - i) / 1000) for i in df['3no']]
fig = go.Figure([
    go.Scatter(
        name = '50_4',
        x = tmp3['tests'],
        y = tmp3['3no'],
        line = dict(color = 'rgb(31,119,180)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp3['tests'],
        y = tmp3['3no'] + 2 * tmp3['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp3['tests'],
        y = tmp3['3no'] - 2 * tmp3['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(31, 119, 180, 0.3)',
        fill = 'tonexty',
        showlegend = False
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['3no'],
        line = dict(color = 'rgb(119,180,31)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp5['tests'],
        y = tmp5['3no'] + 2 * tmp5['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp5['tests'],
        y = tmp5['3no'] - 2 * tmp5['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(119, 180, 31, 0.3)',
        fill = 'tonexty',
        showlegend = False
    ),
    go.Scatter(
        name = 'dwave',
        x = tmp4['tests'],
        y = tmp4['3no'],
        line = dict(color = 'rgb(180, 31, 119)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = 'Upper Bound',
        x = tmp4['tests'],
        y = tmp4['3no'] + 2 * tmp4['std_dev'],
        mode = 'lines',
        marker = dict(color="#444"),
        line = dict(width=0),
        showlegend = False
    ),
    go.Scatter(
        name = 'Lower Bound',
        x = tmp4['tests'],
        y = tmp4['3no'] - 2 * tmp4['std_dev'],
        marker = dict(color="#444"),
        line = dict(width=0),
        mode = 'lines',
        fillcolor = 'rgba(180, 31, 119, 0.3)',
        fill = 'tonexty',
        showlegend = False
    ),
])
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_3no.png")
fig.show()
exit(0)

fig = go.Figure([
    go.Scatter(
        name = '50_4',
        x = tmp3['tests'],
        y = tmp3['time_to_solution'],
        line = dict(color = 'rgb(100,80,0)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = 'dwave',
        x = tmp4['tests'],
        y = tmp4['time_to_solution'],
        line = dict(color = 'rgb(0,100,80)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['time_to_solution'],
        line = dict(color = 'rgb(80,0,100)'),
        mode = 'lines'
    ),
])
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_time_to_solution.png")

fig = go.Figure([
    go.Scatter(
        name = '50_4',
        x = tmp3['tests'],
        y = tmp3['running_time'],
        line = dict(color = 'rgb(100,80,0)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['running_time'],
        line = dict(color = 'rgb(80,0,100)'),
        mode = 'lines'
    ),
])
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_runtime.png")
exit(0)


fig = go.Figure([
    go.Scatter(
        x=x,
        y=y,
        line=dict(color='rgb(0,100,80)'),
        mode='lines'
    ),
    go.Scatter(
        x=x+x[::-1], # x, then x reversed
        y=y_upper+y_lower[::-1], # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    )
])
#fig.show()
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig1.png")