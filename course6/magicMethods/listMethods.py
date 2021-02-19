class DictFunctionality(object):
	def __init__(self, values = None):
		if values is None:
			self.values = {}
		elif isinstance(values, dict):
			self.values = values
		else:
			raise ValueError()
	
	# converting to string:
	def __str__(self):
		return str(self.values) if self.values else ""

	# Items management:
	def __getitem__(self, key):
		return self.values[key]
	
	def __setitem__(self, key, value):
		self.values[key] = value

	def __delitem__(self, key):
		del self.values[key]
	