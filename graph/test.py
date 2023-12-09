import plotly.graph_objs as go
import pandas as pd
import os

mycwd = os.getcwd()
print(mycwd)
os.chdir("..")
print(os.getcwd())

df = pd.read_csv('results/all_results')

print(df)

print(df['version'])

tmp1 = df[df['version'] == '50_1']
tmp2 = df[df['version'] == '50_2']
tmp3 = df[df['version'] == '50_4']
tmp4 = df[df['version'] == 'dwave']

fig = go.Figure([
    go.Scatter(
        name = '50_1',
        x = tmp1['tests'],
        y = tmp1['time_to_solution'],
        line = dict(color = 'rgb(0,100,80)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = '50_2',
        x = tmp2['tests'],
        y = tmp2['time_to_solution'],
        line = dict(color = 'rgb(100,0,80)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = '50_3',
        x = tmp3['tests'],
        y = tmp3['time_to_solution'],
        line = dict(color = 'rgb(100,80,0)'),
        mode = 'lines'
    ),
    go.Scatter(
        name = 'dwave',
        x = tmp4['tests'],
        y = tmp4['time_to_solution'],
        line = dict(color = 'rgb(100,100,100)'),
        mode = 'lines'
    ),
])
fig.show()
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