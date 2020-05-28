import sys
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from naive import Naive
from backtracking import Backtracking
from branch_and_bound import BranchAndBound


class Comparison:

    def __init__(self):
        self.MinIteration = 3
        self.MaxIteration = 11
        self.IterationOfSizes = [i for i in range(self.MinIteration, self.MaxIteration)]
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
        BBAlgorithm = BranchAndBound(index, self.SymmetricalMatrix)
        start = timer()
        BBAlgorithm.TSP()
        end = timer()
        self.BranchAndBoundTime[iter] = end - start

    def backtrack_time (self, index, iter):
        BacktrackingAlgorithm = Backtracking(index, self.SymmetricalMatrix)
        start = timer()
        BacktrackingAlgorithm.tsp(0, 1, 0)
        end = timer()
        self.BacktrackingTime[iter] = end - start

    def naive_time(self, index, iter):
        NaiveAlgorithm = Naive(index, self.SymmetricalMatrix)
        start = timer()
        NaiveAlgorithm.travellingSalesmanProblem()
        end = timer()
        self.NaiveTime[iter] = end - start

    def create_plot(self):
        plt.title("TSP Algorithm's Comparison")
        plt.xlabel("Square Matrix Dimension")
        plt.ylabel("Time")
        plt.grid()
        plt.plot(self.IterationOfSizes, self.BranchAndBoundTime, label="Branch and Bound")
        plt.plot(self.IterationOfSizes, self.BacktrackingTime, label="BackTracking")
        plt.plot(self.IterationOfSizes, self.NaiveTime, label="Naive")
        plt.legend(loc='upper left')
        plt.show()


if __name__ == "__main__":
    comparison = Comparison()
    iteration = 0
    for i in range(comparison.MinIteration, comparison.MaxIteration):
        comparison.matrix_init(i)
        comparison.bb_time(i, iteration)
        comparison.backtrack_time(i, iteration)
        comparison.naive_time(i, iteration)
        iteration += 1
    comparison.create_plot()
    sys.exit()
