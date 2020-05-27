import math


class BranchAndBound:
    def __init__(self, size, matrix):
        self.n = size
        self.graph = matrix
        self.maxsize = float('inf')
        self.final_path = [None] * (self.n + 1)
        self.visited = [False] * self.n
        self.final_res = self.maxsize

    def copy_to_final(self, curr_path):
        self.final_path[:self.n + 1] = curr_path[:]
        self.final_path[self.n] = curr_path[0]

    def first_min(self, i):
        minimum = self.maxsize
        for k in range(self.n):
            if self.graph[i][k] < minimum and i != k:
                minimum = self.graph[i][k]
        return minimum

    def second_min(self, i):
        first, second = self.maxsize, self.maxsize
        for j in range(self.n):
            if i == j:
                continue
            if self.graph[i][j] <= first:
                second = first
                first = self.graph[i][j]
            elif self.graph[i][j] <= second and self.graph[i][j] != first:
                second = self.graph[i][j]
        return second

    def TSPRec(self, curr_bound, curr_weight, level, curr_path):
        if level == self.n:
            if self.graph[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.graph[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_res:
                    self.copy_to_final(curr_path)
                    self.final_res = curr_res
            return
        for i in range(self.n):
            if self.graph[curr_path[level - 1]][i] != 0 and self.visited[i] == False:
                temp = curr_bound
                curr_weight += self.graph[curr_path[level - 1]][i]
                if level == 1:
                    curr_bound -= ((self.second_min(curr_path[level - 1]) + self.second_min(i)) / 2)
                else:
                    curr_bound -= ((self.first_min(curr_path[level - 1]) + self.second_min(i)) / 2)
                if curr_bound + curr_weight < self.final_res:
                    curr_path[level] = i
                    self.visited[i] = True
                    self.TSPRec(curr_bound, curr_weight, level + 1, curr_path)
                curr_weight -= self.graph[curr_path[level - 1]][i]
                curr_bound = temp
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if curr_path[j] != -1:
                        self.visited[curr_path[j]] = True

    def TSP(self):
        curr_bound = 0
        curr_path = [-1] * (self.n + 1)
        self.visited = [False] * self.n
        for i in range(self.n):
            curr_bound += (self.first_min(i) +
                           self.second_min(i))
        curr_bound = math.ceil(curr_bound / 2)
        self.visited[0] = True
        curr_path[0] = 0
        self.TSPRec(curr_bound, 0, 1, curr_path)
