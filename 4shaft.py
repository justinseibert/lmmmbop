shafts = [
	[1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
	[0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0],
	[0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
	[0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
]

tieups = [
	[0,0,1,1],
	[0,1,1,0],
	[1,1,0,0],
	[1,0,0,1],
]

treadles = [
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,0,1],
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,0,1],
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,0,1],
	[0,0,1,0],
	[0,1,0,0],
	[1,0,0,0],
	[0,0,0,1],
	[0,0,1,0],
	[0,1,0,0],
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,0,1],
]

def getTieUps(col):
	return [index for index, tieup in enumerate(tieups) if tieup[col]]

def generatePattern(column_count, row_count):
	pattern = []
	for treadle in treadles:
		for treadle_col, treadle_val in enumerate(treadle):
			# if column is active, refer to tieups
			if treadle_val:
				raised_shaft_indices = getTieUps(treadle_col)
				# copy all shaft rows to active_shafts, except for rows in the raised_shaft_indices
				active_shafts = [row for index, row in enumerate(shafts) if index not in raised_shaft_indices]
				# sum each column of active_shafts into a single row
				weft = [sum(col) for col in zip(*active_shafts)]
				# for each column in the weft, append a '#' if the column is 1, or a "-" if the column is 0 to line
				line = ''.join(['#' if col else '-' for col in weft])
				# append line to pattern, expand by column_count
				pattern.append(line * column_count)
	
	# print each line of the pattern, repeat the process by row_count
	for repeat in range(row_count):
		for line in pattern:
			print(line)

generatePattern(4, 3)