import sys as sys
import pickle as pickle
import plotly.graph_objects as go
import numpy as np



if __name__ == "__main__":
	f = float(sys.argv[1])

	# load data
	file_name = open('datalogger.pi', 'rb')
	data = pickle.load(file_name)
	start_time = data['start_time']
	stop_time = data['stop_time']
	ref_values = data['ref_values']
	ref_values = np.array(ref_values) - 2.5
	hand_values = data['hand_values']
	hand_values = np.array(hand_values) - 2.5

	# plot original data
	t = np.linspace(0, stop_time - start_time, len(hand_values))
	fig = go.Figure(go.Scatter(x=t, y=np.array(hand_values), mode='lines', name='Output: Eye-hand coordinated sine-wave',
		line={
		'width': 5, 
		'color': 'darkorchid',
		}))

	# plot reference data
	fig.add_trace(go.Scatter(x=t, y=np.array(ref_values), mode='lines', name='Input: reference sine-wave',
		line={
		'width': 5,
		'color': 'yellow',
		}))

	fig.update_layout(
		title={
    		'text': '<b>Eye-hand coordination, frequency = {}[Hz]</b>'.format(f),
			'x':0.5,
    		'xanchor': 'center',
    		'yanchor': 'top'
    	},
    	xaxis_title="<b>time (sec)</b>",
    	yaxis_title="<b>voltage (V)</b>",
    	legend_title="<b>Legend</b>",
    )

	fig.show()
