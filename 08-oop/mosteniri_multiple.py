class A:
    def info(self):
        return 'Clasa A'


class B(A):
    def info(self):
        return 'Clasa B'


class C(B):
    def info(self):
        return 'Clasa C'


class D(C, B):
    # def info(self):
    #     return 'Clasa D'
    pass


class F(A):
    def info(self):
        return 'Clasa F'


class G(F, B):
    def info(self):
        return 'Clasa F'


print(D().info())
print(G().info())   # MRO error se mosteneste indirect aceleasi lucruri