
import rrdtool

class RRDUpdate:

	def __init__(self, working_dir):
		self.working_dir=working_dir

	def log_temp(self,  sensor, temp, humidity):  

		rrdtool.update("{}/temp_{}.rrd".format(self.working_dir, sensor), 
		"N:{}:{}".format(temp, humidity))
