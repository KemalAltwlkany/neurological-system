import numpy as np
import plotly.express as px
import plotly.graph_objs as go

if __name__ == '__main__':
    w = np.array([0.05, 0.1, 0.2, 0.3, 0.5, 1, 2])*2*np.pi
    phi = -np.array([1.176, 7.7, 14.964, 21.822, 56.2, 69, 95.6])
    d = {
        'x': w,
        'y': phi
    }
    pix = px.scatter(d, x='x', y='y', trendline="ols")
    pix = pix.data[1]
    fig = go.Figure()
    fig.add_trace(go.Scatter(mode='markers', x=w, y=phi,
                             marker={
                                 'size': 15,
                                 'color': 'blue',
                                 'symbol': 'star-triangle-up'
                             },))
    fig.update_xaxes(type='log')
    fig.update_layout(
        title={
            'text': '<b>Eye-hand coordination, angular Bode plot</b>',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        showlegend=False,
        xaxis_title="<b> &#x3C9; [rad/s] </b>",  # &#x3C9; is HTML code for omega
        # https://www.htmlhelp.com/reference/html40/entities/symbols.html
        yaxis_title="<b> phase lag [&#176;] </b>",  # &#176; is HTML code for degree
    )
    fig.show()

