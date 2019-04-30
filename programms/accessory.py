
'''
Form and get ideal coefficient K and B
'''
def get_ideal_k_and_b():
	x_1 = -60
	y_1 = 3280
	#y_1 = 3007
	x_2 = 125
	y_2 = 784
	#y_2 = 47
	k = float((y_1-y_2))/float((x_1-x_2))
	b = y_2 - k*x_2
	return k, b