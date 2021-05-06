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

	fig.add_trace(go.Scatter(x=t, y=np.array(ref_values), mode='lines', name='Input: reference sine-wave',
		line={
		'width': 5,
		'color': 'yellow',
		}))

	# label hand zeros
	#hand_zeros_x, hand_zeros_y = t[hand_values == 0], hand_values[hand_values == 0]
	#fig.add_trace(go.Scatter(x=hand_zeros_x, y=hand_zeros_y, mode='markers', marker={
	#	'symbol': 'circle',
	#	'size': 15,
	#	'color': 'red',
	#	},
	#	name='Manual zeros'))

	# label reference zeros
	#ref_zeros_x, ref_zeros_y = t[ref_values == 0], ref_values[ref_values == 0]
	#fig.add_trace(go.Scatter(x=ref_zeros_x, y=ref_zeros_y, mode='markers', marker={
	#	'symbol': 'square',
	#	'size': 15,
	#	'color': 'green',
	#	},
	#	name='Reference zeros'))

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

	# find pairs of hand and reference zeros
	# delta_t = []
	#delta_phi = []
	#indices_to_skip = [0, 1, 2, 4, 5, 6, 300]
	#for ind, hand_zero in enumerate(hand_zeros_x):
	#	if ind in indices_to_skip:
	#		continue
	#	index = np.argmin(np.absolute(ref_zeros_x - hand_zero))
	#	delta_t.append(np.absolute(ref_zeros_x[index] - hand_zero))
	#	delta_phi.append(360.0 * f * delta_t[-1])
	#print('All dt = ', delta_t)
	#print('All phase lag = ', delta_phi)
	#print('Average delay = ', np.average(delta_t))
	#print('Average phase lag = ', np.average(delta_phi))
	fig.show()
