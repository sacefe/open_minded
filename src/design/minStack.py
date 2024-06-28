from collections import deque
class MinStack:
    _instance = None
    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.stack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#############################################
# to run the test here un comment this code 
# and rename the file starting with test_
##############################################
# import pytest
# class TestMinStack():
#     # ["MinStack","push","push","push","getMin","pop","top","getMin"]
#     # [[],[-2],[0],[-3],[],[],[],[]]
    
    
#     _instance = None
#     def myStackSingleton(self):
#         if not MinStack._instance:
#             MinStack._instance = MinStack()
#         return MinStack._instance
        
            
#     @pytest.mark.parametrize("function, val, expected", [
#         ("push", -2, None),
#         ("push", 0,  None),
#         ("push", -3,None ),
#         ("getMin",None ,-3),
#         ("pop", None, None),
#         ("getMin", None, 0),
#         ("pop", None, None),
#         ("push", -5,None ),
#         ("getMin", None, -5),
#     ])
#     def  test_minStack(self, function, val, expected):
#         myStack =  self.myStackSingleton()  
#         if function == "push":    
#             assert myStack.push(val) == expected    
#         elif function == "getMin":
#             assert myStack.getMin() == expected
#         elif function == "pop":
#             assert myStack.pop() == expected

# pytest.main(['-v'])