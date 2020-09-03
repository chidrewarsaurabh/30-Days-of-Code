class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        s=max(a)-min(a)
        self.maximumDifference = s

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
