# mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__": # 파일 자체를 실행할 땐 출력 O, import 할 땐 출력 X 
    print(add(1,4))
    print(sub(4,2))