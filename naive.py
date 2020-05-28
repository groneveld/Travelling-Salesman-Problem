from sys import maxsize


class Naive:
    def __init__(self, size, matrix):
        self.n = size
        self.graph = matrix
        self.s = 0
        self.min_path = maxsize

    def travellingSalesmanProblem(self):
        vertex = []
        for i in range(self.n):
            if i != self.s:
                vertex.append(i)
        self.min_path = maxsize
        while True:
            current_pathweight = 0
            k = self.s
            for i in range(len(vertex)):
                current_pathweight += self.graph[k][vertex[i]]
                k = vertex[i]
            current_pathweight += self.graph[k][self.s]
            self.min_path = min(self.min_path, current_pathweight)
            if not self.next_permutation(vertex):
                break

    def next_permutation(self, L):
        n = len(L)
        i = n - 2
        while i >= 0 and L[i] >= L[i + 1]:
            i -= 1
        if i == -1:
            return False
        j = i + 1
        while j < n and L[j] > L[i]:
            j += 1
        j -= 1
        L[i], L[j] = L[j], L[i]
        left = i + 1
        right = n - 1
        while left < right:
            L[left], L[right] = L[right], L[left]
            left += 1
            right -= 1
        return True
