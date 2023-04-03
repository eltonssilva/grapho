import plotly.graph_objs as go

# Definir os dados
Xe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Ye = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
labels = ['linha 1', 'linha 2', 'linha 3']
colors = ['rgb(255,0,0)', 'rgb(0,255,0)', 'rgb(0,0,255)']
text = ['texto 1', 'texto 2', 'texto 3']

# Definir o gráfico
fig = go.Figure()

# Loop para adicionar uma trace para cada linha
for i in range(len(Xe)):
    fig.add_trace(go.Scatter(x=Xe[i],
                             y=Ye[i],
                             mode='lines',
                             text=text[i],
                             line=dict(color=colors[i], width=2),
                             hoverinfo='text',
                             opacity=0.8,
                             name=labels[i]
                             ))

# Exibir o gráfico
fig.show()
