class NumArray:

    def __init__(self, nums: List[int]):
            self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:  
        val = 0
        for index in range(i,j+1):
            val += self.nums[index]
            
        return val
            