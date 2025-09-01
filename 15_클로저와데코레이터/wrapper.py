# wrapper.py (closer2보다 효율적이게)
# closure 정의 면접 질문에 잘 나옴 !! 설명하기 어려움

def mul(m):
    def wrapper(n):
        return m*n
    return wrapper
    
if __name__ =='__main__':
    mul3 = mul(3)
    mul5 = mul(5)
    print(mul3(10))
    print(mul5(10))
    # 위에 수식 4개랑 밑에 2개랑 결과는 똑같이 나옴
    print(mul(3)(10))
    print(mul(5)(10))