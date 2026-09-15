class NumFinder:

    def __init__(self):
        self.smallest = float("inf")
        self.largest = float("-inf")

    def find(self, nums):
        for n in nums:
            if n < self.smallest:
                self.smallest = n
            if n > self.largest:
                self.largest = n


# Test run
nf = NumFinder()
nf.find([4, 25, 7, 9])

print(nf.largest)  # Outputs: 25
print(nf.smallest)  # Outputs: 4