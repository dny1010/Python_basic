# class에서 사용하는 함수들을 초기화 할 때 __init__ => self는 무조건 들어감 매개변수로 !

class MyIterator:
    def __init__(self, data): # 변수 초기화
        self.data = data
        self.position = 0
    
    def __iter__(self): # 이터레이터로 변경
        return self
    
    def __next__(self): # 변수를 하나씩 꺼냄
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
if __name__ =='__main__':
    list = MyIterator([1,2,3])
    for item in list:
        print(item)