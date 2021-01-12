class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.count = 0
        self.sum = 0
        self.data = []
        

    def next(self, val: int) -> float:
        
        if self.count < self.size:
            self.count += 1
        else:
            self.sum -= self.data.pop(0)
        
        self.data.append(val)
        self.sum += val
        return self.sum/self.count