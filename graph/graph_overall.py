import plotly.graph_objs as go
import pandas as pd
import os
import math 

DEFAULT_PLOTLY_COLORS=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)']

versions = ['50_4', '100_4', '200_4', 'GAC', 'UTC']

categories = list()


mycwd = os.getcwd()
print(mycwd)
os.chdir("..")
print(os.getcwd())

fname = 'results/copy_all_results_2.csv' # can be input

df = pd.read_csv(fname)

#print(df)

print(df['version'])
print('X?? n, deg, max_weight')
X_name = input() # n, deg, max_weight
print('Y?? 0no, 3no, running_time, time_to_solution, chain_strength')
Y_name = input() # 0no, 3no, running_time, time_to_solution, chain_strength
print('type?? abs, rel')
type = input() # abs rel
#df['std_dev'] = [2 * math.sqrt(i * (1 - i) / 1000) for i in df['0no']]

for i in range (0, 5):
    categories.append(df[df['version'] == versions[i]])

if type == 'rel':
    for i in range(0, len(categories[0][Y_name])):
        categories[0][Y_name][i] /= categories[5][Y_name][i]
        categories[1][Y_name][i] /= categories[5][Y_name][i]
        categories[2][Y_name][i] /= categories[5][Y_name][i]
        categories[3][Y_name][i] /= categories[5][Y_name][i]


fig = go.Figure([
    go.Scatter(
        name = versions[0],
        x = categories[0][X_name],
        y = categories[0][Y_name],
        line = dict(color = DEFAULT_PLOTLY_COLORS[0]),
        mode = 'lines',
    ),

    go.Scatter(
        name = versions[1],
        x = categories[1][X_name],
        y = categories[1][Y_name],
        line = dict(color = DEFAULT_PLOTLY_COLORS[1]),
        mode = 'lines',
    ),

    go.Scatter(
        name = versions[2],
        x = categories[2][X_name],
        y = categories[2][Y_name],
        line = dict(color = DEFAULT_PLOTLY_COLORS[2]),
        mode = 'lines',
    ),

    go.Scatter(
        name = versions[3],
        x = categories[3][X_name],
        y = categories[3][Y_name],
        line = dict(color = DEFAULT_PLOTLY_COLORS[3]),
        mode = 'lines',
    ),

    go.Scatter(
        name = versions[4],
        x = categories[4][X_name],
        y = categories[4][Y_name],
        line = dict(color = DEFAULT_PLOTLY_COLORS[4]),
        mode = 'lines',
    ),
    
])
fig.update_layout(
    xaxis_title = X_name,
    yaxis_title = Y_name,
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    width = 1250,
    height = 700,
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
)

fname = "images/fig_" + type + X_name + Y_name

if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image(fname)
fig.show()

exit(0)