# closure2.py (closure보다 효율적이게)

class Mul:
    def __init__(self, m):
        self.m = m

    # def mul(self, n): call 함수를 쓰면 뒤에 .mul을 쓸 필요 X
    def __call__(self,n):
        return n*self.m
    
if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)
    mul7 = Mul(7)

    # print(mul3.mul(10))
    # print(mul5.mul(10))
    # print(mul7.mul(10))

    print(mul3(10))
    print(mul5(10))
    print(mul7(10))