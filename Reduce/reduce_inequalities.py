
import copy

class Reduce():
	def __init__(self, filename, tablename):
		self.filename = filename
		self.tablename = tablename

	def Read_Table(self):
		"""
		Read the truth table from tablename to a list
		"""
		fileobj = open(self.tablename, "r")
		table = []
		for i in fileobj:
			table.append(list(map(int, (i.strip()).split())))
		fileobj.close()
		return table

	def ReadIne(self):
		"""
		Read the linear inequalites from filename to a list
		"""
		fileobj = open(self.filename, "r")
		ine = []
		for i in fileobj:
			ine.append(list(map(int, (i.strip()).split())))
		fileobj.close()
		return ine

	@staticmethod
	def Integer2Bitlist(n, l):
		"""
		Convert an integer n to its bitstring representation, and the length of the 
		bitstring is restricted to l. For an integer whose bitstring representation 
		with a length less than l, we add 0 ahead. This function return a list of 
		length l. 
		we assume the length of the bitstring representation of n is < 256
		"""
		s = list(map(int, list(format(n, "0256b"))))
		s = s[len(s) - l :]
		return s

	@staticmethod
	def ValueOfExpression(p, l):
		"""
		Evaluate the value of the linear inequality at point p, and l represents a linear inequality.
		"""

		assert len(p) + 1 == len(l)
		# COPY the list, since we will modify the list and this will result in a 
		# change of the list outside the function.
		temp_p = copy.deepcopy(p)
		temp_p.append(1)
		return sum([x * y for (x, y) in zip(temp_p, l)])


	def InequalitySizeReduce(self):
		"""
		Given a set of points and the corresponding H-Representation, choose a 
		subset of inequalities from H-Representation which is equivalent to 
		describe the points.
		"""
		print(self.tablename)
		points = self.Read_Table()    # 真值表的点集合
		inequalities = self.ReadIne()   # 不等式组
		assert len(points) > 0
		assert len(inequalities) > 0
		assert len(points[0]) + 1 == len(inequalities[0])
		length = len(points[0])
		# get all possible points in {0,1}^n
		apoints = [Reduce.Integer2Bitlist(i, length) for i in range(2**length)]
		# get the complementary set of points
		cpoints = [p for p in apoints if p not in points]

		print("points: len", len(points))
		print("inequalities: len", len(inequalities))
		print('apoints', len(apoints))
		print('cpoints', len(cpoints))

		ineq = copy.deepcopy(inequalities)

		# rineq stores the inequalities we choose
		rineq = []
		while len(cpoints) > 0:
			temp_p = []
			temp_l = []
			# 在当前的不等式组 rineq 中选取一个不等式，使得当前的非解集 cpoints 中不满足该不等式的点最多
			for l in ineq:
				# 选取一个不等式，将cpoints中不满足该不等式的点放入temp中
				temp = [p for p in cpoints if (Reduce.ValueOfExpression(p, l) < 0)]
				if len(temp) > len(temp_p):  # 当前不等式排除的点更多
					temp_p = temp
					temp_l = l
			for p in temp_p:
				cpoints.remove(p)
			rineq.append(temp_l)
			ineq.remove(temp_l)

		print(len(rineq))
		return rineq

