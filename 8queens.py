import random


class Queen:
	"""Represents one of eight queens on the chessboard"""

	def __init__(self, row, neighbor):
		self.row = row
		# Prevent generating the same solution over and over
		self.column = random.randint(1, 8)
		self.neighbor = neighbor

	def find_solution(self):
		while self.neighbor != None and \
			self.neighbor._can_attack(self.row, self.column):
			if not self._advance():
				return False
		return True

	def _advance(self):
		if self.column < 8:
			self.column += 1
			return self.find_solution()
		if self.neighbor != None:
			if not self.neighbor._advance():
				return False
			if not self.neighbor.find_solution():
				return False
		else:
			self.column = 1
			return self.find_solution()
		self.column = 1
		return self.find_solution()

	def _can_attack(self, test_row, test_column):
		# Horizontal
		if self.column == test_column:
			return True
		# Diagonally
		row_difference = test_row - self.row
		if self.column + row_difference == test_column or \
			self.column - row_difference == test_column:
			return True
		if self.neighbor != None:
			return self.neighbor._can_attack(test_row, test_column)
		return False

	def print(self):
		if self.neighbor != None:
			self.neighbor.print()
		row = list('........')
		row[self.column-1] = 'Q'
		print(' '.join(row))


if __name__ == '__main__':
	q = None
	for i in range(1, 9):
		q = Queen(i, q)
		q.find_solution()
	q.print()
