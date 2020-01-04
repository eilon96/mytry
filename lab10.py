class A:
    def __init__(self):
        self.uuu = "a"
    def print(self):
        print(self.uuu)
        return self
    def add(self,a):

        return self
if __name__ == '__main__':
    a= A()
    a.print().add("a")
    print("commit")