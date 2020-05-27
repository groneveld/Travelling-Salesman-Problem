import sys
import numpy as np
from timeit import default_timer as timer
from branch_and_bound import BranchAndBound


class Comparison:
    def __init__(self):
        self.MinIteration = 3
        self.MaxIteration = 12
        self.CurrentMatrixSize = 0
        self.BranchAndBoundTime = np.zeros(self.MaxIteration - self.MinIteration + 1)
        self.BacktrackingTime = [None]
        self.NaiveTime = [None]
        self.SymmetricalMatrix = [None]

    def matrix_init(self, maxsize):
        self.CurrentMatrixSize = maxsize
        b = np.random.randint(low=1, high=101, size=(self.CurrentMatrixSize, self.CurrentMatrixSize))
        self.SymmetricalMatrix = (b + b.T) / 2
        np.fill_diagonal(self.SymmetricalMatrix, 0)
        self.SymmetricalMatrix = self.SymmetricalMatrix.astype(int)


if __name__ == "__main__":
    comparison = Comparison()
    iteration = 0
    for index in range(comparison.MinIteration, comparison.MaxIteration):
        comparison.matrix_init(index)
        BBAlgorithm = BranchAndBound(index, comparison.SymmetricalMatrix)
        start = timer()
        BBAlgorithm.TSP()
        end = timer()
        comparison.BranchAndBoundTime[iteration] = end - start
        iteration += 1
    print(comparison.BranchAndBoundTime)
    sys.exit()
