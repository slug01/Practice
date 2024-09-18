def modify(func):
    def wrapper(self,*args):
        print(f"Adding {self.a} and {self.b}")
        return func(self,*args)
    return wrapper

class adding:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @modify
    def sum_a_b(self):
        j = self.a + self.b
        return j 
num = adding(2,3)
result = num.sum_a_b()
print(result)
    