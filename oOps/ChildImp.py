from oOps.oOpsDemo import Calculator


class childImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = childImp()
print(obj.getCompleteData())
