class Tree():
    def __init__(self):
        self.neighbours = []
        self.rank = 0

    def add_path(self,nextNode):
        self.neighbours.append(nextNode)
        self.rank += 1


