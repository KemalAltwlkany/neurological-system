import sys as sys
import pickle as pickle
import plotly.graph_objects as go
import numpy as np



if __name__ == "__main__":
	
	t = np.linspace(0, 10, 1000)
	ref = 2.5*np.sin(t) + 2.5
	
	#user = 2.5*np.ones(1000)

	#user = np.concatenate((2.5*np.ones(250), ref[0:150], 5*np.ones(600)))

	#user = np.concatenate(([2.5]*300, ref[0:150], [5]*100, ref[150:450], [0]*150))

	user = np.concatenate((2.5*np.ones(30), ref))

	fig = go.Figure()

	# plot reference data
	fig.add_trace(go.Scatter(x=t, y=ref, mode='lines', name='Input: Reference sine-wave',
		line={
		'width': 17,
		'color': 'yellow',
		}))

	fig.add_trace(go.Scatter(x=t, y=user, mode='lines', name='Output: Eye-hand coordinated sine-wave',
		line={
		'width': 17, 
		'color': 'darkorchid',
		}))

	

	fig.update_layout(
    	#xaxis_title="<b>time (sec)</b>",
    	#yaxis_title="<b>voltage (V)</b>",
    	showlegend=False,
    	paper_bgcolor='white',
    	plot_bgcolor='white',
    	xaxis={'showticklabels': False},
    	yaxis={'showticklabels': False}
    	#legend_title="<b>Legend</b>",
    )

	fig.show()
