import pytest
from src.design.lru_cache import LRUCache 
from src.design.minStack import MinStack

class TestLRU():
    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    @pytest.fixture
    def myLRU(self):
        return LRUCache(2)
    
    @pytest.mark.parametrize("function, values, expected",[
        ("put", [1,1], 1),
        ("put", [2,2], 2),
        ("get", [1], -1)      
    ])
    def test_LRUcache(self, myLRU, function, values, expected):
        if function == "put":
            assert myLRU.put(values[0], values[1]) == expected
        elif function == "get":
            assert myLRU.get(values[0]) == expected


class TestMinStack():
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]

    # create singleton stack 
    _instance = None
    def myStackSingleton(self):
        if not MinStack._instance:
            MinStack._instance = MinStack()
        return MinStack._instance
        
            
    @pytest.mark.parametrize("function, val, expected", [
        ("push", -2, None),
        ("push", 0,  None),
        ("push", -3,None ),
        ("getMin",None ,-3),
        ("pop", None, None),
        ("getMin", None, 0),
        ("pop", None, None),
        ("push", -5,None ),
        ("getMin", None, -5),
    ])
    def  test_minStack(self, function, val, expected):
        myStack =  self.myStackSingleton()  
        if function == "push":    
            assert myStack.push(val) == expected    
        elif function == "getMin":
            assert myStack.getMin() == expected
        elif function == "pop":
            assert myStack.pop() == expected

pytest.main(['-v'])


# pytest.main(['-v'])