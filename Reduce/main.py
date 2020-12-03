# After generating the H-representation of a set of points by using equality_generator function in sagemath,
# select a smaller set of linear inequalities from the H-Representation.

# Implemented by Qin haiwen


from reduce_inequalities import Reduce

if __name__ == "__main__":

	filename = "inequalities.txt"
	tablename = "truth_table.txt"

	present = Reduce(filename, tablename)
	rine = present.InequalitySizeReduce()

	filename_result = "Reduce_Inequalities.txt"
	fileobj = open(filename_result, "w")
	for l in rine:
		fileobj.write(str(l) + "\n")
	fileobj.close()
