class Test1():

    def Met1(self):
        self.unu = 'unu'


class Test2(Test1):

    def Met2(self):
        self.unu = 'doi'


obj = Test2()
print(obj.Met1())
print(obj.Met2())
