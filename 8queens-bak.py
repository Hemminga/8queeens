import random


class Queen:
	"""Represents one of eight queens on the chessboard"""

	def __init__(self, col, neighbor):
		# Prevent generating the same result over and over
		self.row = random.randint(1, 8)
		self.column = col
		self.neighbor = neighbor

	def find_solution(self):
		while self.neighbor != None and \
			self.neighbor.can_attack(self.row, self.column):
			if not self.advance():
				return False
		return True

	def advance(self):
		if self.row < 8:
			self.row += 1
			return self.find_solution()
		if self.neighbor != None:
			if not self.neighbor.advance():
				return False
			if not self.neighbor.find_solution():
				return False
		else:
			self.row = 1
			return self.find_solution()
		self.row = 1
		return self.find_solution()

	def can_attack(self, test_row, test_column):
		# Horizontal
		if self.row == test_row:
			return True
		# Diagonally
		column_difference = test_column - self.column
		if self.row + column_difference == test_row or \
			self.row - column_difference == test_row:
			return True
		if self.neighbor != None:
			return self.neighbor.can_attack(test_row, test_column)
		return False

	def print(self):
		if self.neighbor != None:
			self.neighbor.print()
		# The matrix is a global two-dimensional list
		matrix[self.column-1][self.row-1] = 'Q'


if __name__ == '__main__':
	q = None
	for i in range(1, 9):
		q = Queen(i, q)
		q.find_solution()
	# This solution calculates columns so we
	# resort to a global matrix type two-dimensional
	# list to store the result.
	matrix =  [['.'] * 8 for i in range(8)]
	q.print()
	for row in matrix:
		for cell in row:
			print(cell, end='')
		print()
