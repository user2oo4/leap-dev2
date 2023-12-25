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

fig = go.Figure([

    go.Scatter(
        name = '50_4',
        x = tmp4['tests'],
        y = tmp4['running_time'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[1]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '100_4',
        x = tmp5['tests'],
        y = tmp5['running_time'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[2]),
        mode = 'lines',
    ),

    go.Scatter(
        name = '200_4',
        x = tmp6['tests'],
        y = tmp6['running_time'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[3]),
        mode = 'lines',
    ),

    go.Scatter(
        name = 'GAC',
        x = tmp7['tests'],
        y = tmp7['running_time'],
        line = dict(color = DEFAULT_PLOTLY_COLORS[4]),
        mode = 'lines',
    ),
    
])
fig.update_layout(
    xaxis_title = "Deg",
    yaxis_title = "Running time (sec)",
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig_running_time_abs_deg.png")
fig.update_yaxes(type='log')
fig.show()

exit(0)