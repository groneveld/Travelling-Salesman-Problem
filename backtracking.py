
class Backtracking:
    def __init__(self, size, matrix):
        self.answer = []
        self.visited = [False for i in range(size)]
        self.visited[0] = True
        self.graph = matrix
        self.n = size

    def tsp(self, current_position, count, cost):
        if count == self.n and self.graph[current_position][0]:
            self.answer.append(cost + self.graph[current_position][0])
            return
        for i in range(self.n):
            if self.visited[i] == False and self.graph[current_position][i]:
                self.visited[i] = True
                self.tsp(i, count + 1, cost + self.graph[current_position][i])
                self.visited[i] = False