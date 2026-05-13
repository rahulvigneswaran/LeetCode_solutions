class DetectSquares:

    def __init__(self):
        self.memory = {}
        

    def add(self, point: List[int]) -> None:
        self.memory[tuple(point)] = self.memory.get(tuple(point), 0) + 1
        

    def count(self, point: List[int]) -> int:
        Ax, Ay = point
        count = 0
        for i in self.memory.keys():
            (Bx, By) = i

            if abs(Ax - Bx) != abs(Ay - By) or Ax == Bx:
                continue

            if (Ax,By) in self.memory and (Bx, Ay) in self.memory:
                count += self.memory[i]*self.memory[(Ax,By)]*self.memory[(Bx, Ay)]
        return count

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)