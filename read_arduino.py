import serial as serial
import time as time
import pickle as pickle
#from serial import Serial

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=20)
ref_values = [0] * 5000
hand_values = [0] * 5000

i = 0 

while True:
	raw_value = arduino.readline()
	
	if i == 0:
		start_time = time.time()

	value = float(raw_value[:-2:].decode('utf-8'))
	ref_values[i] = value
	
	raw_value = arduino.readline()
	value = float(raw_value[:-2:].decode('utf-8'))
	hand_values[i] = value
	
	i += 1
	print(value)
	if i >= 4500:
		break
stop_time = time.time()
file_name = open('datalogger.pi', 'wb')
data = {}
data['ref_values'] = ref_values
data['hand_values'] = hand_values
data['start_time'] = start_time
data['stop_time'] = stop_time
pickle.dump(data, file_name)
