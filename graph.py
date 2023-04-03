import igraph
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go

def draw(devices, labels, labels_show, id_slave, rssi_slave, devices_type, db_color, db_color_b, type_line, master_info):

    cor_IC_315 = '#f00000'
    cor_IC_518 = '#0000ff'
    cor_IC_516 = '#00ff00'
    cor_IW_233 = '#ffff00'
    cor_IW_122 = '#ff00ff'
    cor_IT_603 = '#00ffff'
    cor_else   = '#303030'

    cor_g = '#00ff00'
    cor_r = '#ff0000'
    cor_y = '#ffff00'

  

    tamanho_master = 90
    tamanho_slave = 70

 
    tamanho = []
    device_color = []

    for id in id_slave:

        if(id == 0):
            tamanho.append(tamanho_master)
        else:
            tamanho.append(tamanho_slave)

    for type in devices_type:

        if(type == "IC-315"):
            device_color.append(cor_IC_315)
        elif(type == "IC-518"):
            device_color.append(cor_IC_518)
        elif(type == "IC-516"):
            device_color.append(cor_IC_516)
        elif(type == "IW-122"):
            device_color.append(cor_IW_122)
        elif(type == "IW-233"):
            device_color.append(cor_IW_233)
        elif(type == "IT-603"):
            device_color.append(cor_IT_603)
        else:
            device_color.append(cor_else)




    G = Graph()

    nr_vertices = len(devices) + 1
    G.add_vertices(nr_vertices)
    G.add_edges(devices)

    lay = G.layout('rt')

    position = {k: lay[k] for k in range(nr_vertices)}
    Y = [lay[k][1] for k in range(nr_vertices)]
    M = max(Y)

    es = EdgeSeq(G) # sequence of edges
    E = [e.tuple for e in G.es] # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2*M-position[k][1] for k in range(L)]
    Xe = []
    Ye = []

    Xl = []
    Yl = []

    Xt = []
    Yt = []

    for edge in E:

        Xe+=[position[edge[0]][0],position[edge[1]][0], None]
        Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

    for edge in E:
        x1 = (position[edge[0]][0])
        x2 = (position[edge[1]][0])
        y1 = (2*M-position[edge[0]][1])
        y2 = (2*M-position[edge[1]][1])
        Xl.append([x1,x2, None])
        Yl.append([y1,y2, None])

    for edge in E:
        x1 = (position[edge[0]][0])
        x2 = (position[edge[1]][0])
        y1 = (2*M-position[edge[0]][1])
        y2 = (2*M-position[edge[1]][1])
        xp = ((x2 - x1)/2 + x1)
        yp = ((y2 - y1)/2 + y1)
        Xt.append([xp,xp, None])
        Yt.append([yp,yp, None])


    #print(devices)
    #print(G)
    #print(nr_vertices)

    print(position)
    #print(Xe)
    #print(Ye)

    fig = go.Figure()

    for i in range(len(Xt)):
        fig.add_trace(go.Scatter(x=Xt[i],
                            y=Yt[i],
                            mode="text",
                            name="Text",
                            hoverinfo='text',
                            opacity=0.8,
                            text= (str(rssi_slave[i]) + "db"),

                        ))
        

            
    for i in range(len(Xl)):
        fig.add_trace(go.Scatter(x=Xl[i],
                            y=Yl[i],
                            mode="lines",
                            name="Lines",
                            line=dict(color=db_color_b[i], width=20),
                            text= (str(rssi_slave[i]) + "db"),
                            hoverinfo='text',
                        ))
        
    for i in range(len(Xl)):
        fig.add_trace(go.Scatter(
            x=Xl[i],
            y=Yl[i],
            fill='toself',
            line=dict(color=db_color[i], width=3, dash=type_line[i]),
            name= (str(rssi_slave[i]) + "db"),
            showlegend=True,
        ))

    fig.add_trace(go.Scatter(x=Xn,
                    y=Yn,
                    mode='markers',
                    name='Master <br> 182.156.433.234',
                    marker=dict(symbol='circle-dot',
                                    size= tamanho,
                                    color=device_color,    #'#DB4551',
                                    line=dict(color='rgb(50,50,50)', width=1)
                                    ),
                    text=labels_show,
                    hoverinfo='text',
                    opacity=0.8
                    ))

    axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )


    def make_annotations(pos, text, font_size=14, font_color='rgb(0,0,0)'):
        annotations = []
        for k in range(L):
            annotations.append(
                dict(
                    text=labels[k], # or replace labels with a different list for the text within the circle
                    x=pos[k][0], y=2*M-position[k][1],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )
        return annotations



    fig.update_layout(title= master_info,
                annotations=make_annotations(position, labels),
                font_size=18,
                showlegend=False,
                xaxis=axis,
                yaxis=axis,
                margin=dict(l=40, r=40, b=85, t=100),
                hovermode='closest',
                plot_bgcolor='rgb(248,248,248)'
                )



    fig.show()


