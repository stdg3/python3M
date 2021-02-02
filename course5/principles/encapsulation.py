"""
fonk
_ ile başlayanlar atıyorum araç rengi değişecek ama aynı zamanda trafikçilerde de gözükmesi için bilidirecek

__ ile başlayanlar asla değişmesini istemiceğin bilgileri barındırır araç altın kaplama tüm şartlarda sabit kalmasını istersin gibi
"""
class Exapmle(object):
	def __init__(self):
		self.a = 1
		self._b = 2 # dikkatli kullan
		self.__c = 3 # çoook dikkatli kullan çünkü başka yerde çağılamaz
		print("{} {} {}".format(
			self.a,
			self._b,
			self.__c))
	def call (self):
		print("called!")

ex = Exapmle()
print("a",ex.a)
print("_b",ex._b)
try:
	print("__c",ex.__c)
except AttributeError as e:
	print(e)
