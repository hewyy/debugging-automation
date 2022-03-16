
import sys
import subprocess
from interester import MinTestSuite


class DeltaDebug:
    def __init__(self, num, log):
        self.num = num
        self.log = log
        self.interestingizer = MinTestSuite()

    def is_intersting(self, l1):
        return self.interestingizer.is_interesting(l1)

    def union_list(self, l1, l2):
        return list(set().union(l1, l2))

    def dd(self, l1, l2):

        if self.log:
            print("[log] dd(l1=", l1, " , l2=", l2, " )")

        n = len(l2)
        if n == 1:
            return l2

        split = n // 2

        # fixme - see example in lecture
        p1 = l2[:split]
        p2 = l2[split:]

        # check if intersting
        if self.is_intersting(self.union_list(l1, p1)):
            return self.dd(l1, p1)
        
        if self.is_intersting(self.union_list(l1, p2)):
            return self.dd(l1, p2)

        # interference case
        temp1 = self.dd(self.union_list(l1, p2), p1)
        temp2 = self.dd(self.union_list(l1, p1), p2)

        return self.union_list(temp1, temp2)


    def run(self):
        full_list = [i for i in range(0,self.num)]
        ret = self.dd([], full_list)
        ret.sort() # as per spec
        return ret


# get CLA
num = 1639
log = True # used for debug logging

delta_debug = DeltaDebug(num, log)
result = delta_debug.run()
print(result)