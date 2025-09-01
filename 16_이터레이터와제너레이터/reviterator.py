# reverse iterator 뒤에서부터 꺼내기

class RevIterator:
    def __init__(self, data): # 변수 초기화
        self.data = data
        self.position = len(self.data)-1
    
    def __iter__(self): # 이터레이터로 변경
        return self
    
    def __next__(self): # 변수를 하나씩 꺼냄
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    
if __name__ =='__main__':
    list = RevIterator([1,2,3])
    for item in list:
        print(item)