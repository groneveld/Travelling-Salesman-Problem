import sys
import numpy as np
from timeit import default_timer as timer

from backtracking import Backtracking
from branch_and_bound import BranchAndBound


class Comparison:
    def __init__(self):
        self.MinIteration = 3
        self.MaxIteration = 12
        self.CurrentMatrixSize = 0
        self.BranchAndBoundTime = np.zeros(self.MaxIteration - self.MinIteration)
        self.BacktrackingTime = np.zeros(self.MaxIteration - self.MinIteration)
        self.NaiveTime = np.zeros(self.MaxIteration - self.MinIteration)
        self.SymmetricalMatrix = []

    def matrix_init(self, maxsize):
        self.CurrentMatrixSize = maxsize
        b = np.random.randint(low=1, high=101, size=(self.CurrentMatrixSize, self.CurrentMatrixSize))
        self.SymmetricalMatrix = (b + b.T) / 2
        np.fill_diagonal(self.SymmetricalMatrix, 0)
        self.SymmetricalMatrix = self.SymmetricalMatrix.astype(int)

    def bb_time(self, index, iter):
        BBAlgorithm = BranchAndBound(index, comparison.SymmetricalMatrix)
        start = timer()
        BBAlgorithm.TSP()
        end = timer()
        comparison.BranchAndBoundTime[iter] = end - start

    def backtrack_time (self, index, iter):
        BacktrackingAlgorithm = Backtracking(index, comparison.SymmetricalMatrix)
        start = timer()
        BacktrackingAlgorithm.tsp(0, 1, 0)
        end = timer()
        comparison.BacktrackingTime[iter] = end - start


if __name__ == "__main__":
    comparison = Comparison()
    iteration = 0
    for i in range(comparison.MinIteration, comparison.MaxIteration):
        comparison.matrix_init(i)
        comparison.bb_time(i, iteration)
        comparison.backtrack_time(i, iteration)
        iteration += 1
    print(comparison.BranchAndBoundTime)
    print(comparison.BacktrackingTime)
    sys.exit()
