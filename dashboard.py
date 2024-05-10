import streamlit as st
import plotly.graph_objects as go

x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17 ,18, 19 ,20, 21]

fig = go.Figure()

# Deployed
fig.add_trace(go.Scatter(
    x=x, y=[0,0,0,0,0,0,0,0,0,1,2,3,4,4,6,7,7,9,10,12,14,16],
    name='Deployed',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(29, 37, 31)'),
    stackgroup='one'
))

# Test
fig.add_trace(go.Scatter(
    x=x, y=[0,0,0,0,0,0,1,2,3,2,2,2,2,3,1,2,3,2,2,1,2,0],
    name='Test',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(96, 147, 102)'),
    stackgroup='one'
))

# Development
fig.add_trace(go.Scatter(
    x=x, y=[0,0,0,0,2,6,7,6,5,5,5,5,5,5,5,5,5,5,5,5,2,2],
    name='Development',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(65, 127, 186)'),
    stackgroup='one' # define stack group
))

# Analysis
fig.add_trace(go.Scatter(
    x=x, y=[0,0,2,7,8,5,3,3,3,3,3,3,2,2,2,2,3,3,3,3,3,3],
    name='Analysis',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(208, 72, 67)'),
    stackgroup='one'
))

# Ready
fig.add_trace(go.Scatter(
    x=x, y=[0,3,3,2,1,1,3,4,5,5,5,4,4,4,4,3,2,2,1,1,1,1],
    name='Ready',
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(155, 155, 155)'),
    stackgroup='one'
))


#fig.update_layout(xaxis_range=(0, 21))
#fig.update_layout(yaxis_range=(0, 25))

fig.update_layout(title=dict(text="Cumulative Diagram Flow", font=dict(size=25)),
                             xaxis_title='Dia', yaxis_title='Cartões Acumulados')

fig.update_xaxes(range=[0, 21], dtick=1, showgrid=True, gridwidth=1, gridcolor='rgb(255,231,237)')
fig.update_yaxes(range=[0, 25], dtick=1, showgrid=True, gridwidth=1, gridcolor='rgb(255,231,237)')

st.plotly_chart(fig)
