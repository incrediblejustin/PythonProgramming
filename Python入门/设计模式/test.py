class A(object):
    def __init__(self, new_a):
        self.a = new_a
    def __str__(self):
        return "A::a = %d"%self.a
    def p(self):
        print("A::p")
class B(A):
    def __init__(self, new_a, new_b):
        super().__init__(new_a)
        self.b = new_b

    def __str__(self):
        return super().__str__() + '\n' + "B::b = %d"%self.b


baby = B(1,2)
print(baby)
baby.p()



