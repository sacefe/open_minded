class ListNode:
    def __init__(self, key, val):
        self.key= key
        self.val= val
        self.prev= None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dict={}
        self.capacity= capacity
        self.head= ListNode(0,0)
        self.tail= ListNode(0,0)
        self.head.next= self.tail
        self.tail.prev= self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node= self.dict[key]
        # move node to the end
        self.remove(node)
        self.addNew(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            oldNode= self.dict[key]
            self.remove(oldNode)
        #update dict key
        newNode= ListNode(key, value)
        self.dict[key]= newNode
        #add to the end 
        self.addNew(newNode)
        #delete if capacity exceed
        if (len(self.dict) > self.capacity):
            nodeDelete= self.head.next
            self.remove(nodeDelete)
            del(self.dict[nodeDelete.key])
        return newNode.val
         
        
    def addNew(self, node):
        temp= self.tail.prev
        self.tail.prev= node
        node.next= self.tail
        temp.next= node
        node.prev= temp
      
    def remove(self, node):
        tnext= node.next
        tprev= node.prev
        tnext.prev= tprev
        tprev.next= tnext
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#############################################
# to run the test here un comment this code 
# and rename the file starting with test_
##############################################
# import pytest
# class TestLRU():
#     # ["LRUCache","put","put","get","put","get","put","get","get","get"]
#     # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
#     @pytest.fixture
#     def myLRU(self):
#         return LRUCache(2)
    
#     @pytest.mark.parametrize("function, values, expected",[
#         ("put", [1,1], 1),
#         ("put", [2,2], 2),
#         ("get", [1], -1)      
#     ])
#     def test_LRUcache(self, myLRU, function, values, expected):
#         if function == "put":
#             assert myLRU.put(values[0], values[1]) == expected
#         elif function == "get":
#             assert myLRU.get(values[0]) == expected
#            
# pytest.main(['-v'])