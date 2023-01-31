# 구성 요소(메서드)      
# i.        __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
# ii.        empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.      
# iii.        top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.      
# iv.        pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.       
# v.        push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.      
# vi.        __repr__: 현재 스택의 요소들을 보여준다.

class Stack:
    def __init__(self):
        self.items = []

    # 스택이 비었다면 True를 반환하고, 아니면 False 를 반환한다
    def empty(self):
        return not bool(self.items) 

    # 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다. 
    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    # 스택의 가장 마지막 데이터 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다
    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None

    # 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.
    def push(self):
        self.items.append(elem)

    # 객체 자체가 Return 하는 것
    def __repr__(self):
        ''.join(self.items)
    
    # 객체를 Print 했을 때 나오는 값
    # def __str__(self):
    #     pass
        
my_list = list()
s = Stack()
s.push('test')
print(s.pop())