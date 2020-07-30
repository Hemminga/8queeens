from pprint import pprint

BOARD_SIZE = 8


# https://stackoverflow.com/a/5133538/9840639
def under_attack(col, queens):
    # You do not need to fill in these fields. This is a helper function for the solve function.
    left = right = col
    # Reversing queens causes them to be iterated over in reverse order.
    for _, c in reversed(queens):
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]
    # It appears that in solving this board, it solves all boards smaller than it in a recursive manner.
    smaller_solutions = solve(n - 1)
    # This line appears to be in error. Have you run this code and verified that it runs correctly?
    return [solution + [(n, i + 1)]
            for i in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(i + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)
