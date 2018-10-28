import re
#класс для решения уравнений
class sumAll:	
	def __init__(self, form):
		#задаем формулу
		self.result = self.form = form

		#получаем массив переменных, вводим значения
		self.args = dict.fromkeys(re.split(r'[\+\-\*\/]', self.form))
		for arg in self.args:
			self.args[arg] = input('Значение \'{0}\':'.format(arg))
			self.result = self.result.replace(arg, self.args[arg])


form = input('Введите формулу:')
test = sumAll(form)
print(eval(test.result))