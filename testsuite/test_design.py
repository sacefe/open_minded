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


from src.design.serialize_and_Deserialize_Binary_Tree import Codec, CreateTree
from typing import List, Optional
class TreeNode:
    def __init__(self, val:int):
        self.left= None
        self.right= None
        self.val = val

class TestCodec:
    def buildTree(self, listNodes:List[int], index:int) -> Optional[TreeNode]:
        ''' convert a list in a Treenode
        :type nums: List,  index: integer
        :rtype: TreeNode
        '''
        root= None
        if index < len(listNodes):
            if listNodes[index] == None:
                return None
            root = TreeNode(listNodes[index])       
            root.left= self.buildTree(listNodes, 2 * index + 1)  #1, 3, 7, 15, ..
            root.right= self.buildTree(listNodes,2 * index + 2)  #2, 6, 12, 25, ...
        return root
    
    @pytest.fixture
    def codecObj(self):
        return Codec()
    @pytest.mark.parametrize("root,  serialized",[
        ([1,2,3,None,None,4,5], "1 2 None None 3 4 None None 5 None None" )
    ])
    def test_serialize(self, codecObj, root,  serialized):
        tree= self.buildTree(root, 0)
        ser= codecObj.serialize(tree) 
        assert ser == serialized

    @pytest.mark.parametrize("root, serialized",[
        ([1,2,3,None,None,4,5], "1 2 None None 3 4 None None 5 None None" )
    ])
    def test_deserialize(self, codecObj, root,  serialized):
        des= codecObj.deserialize(serialized)
        tree = self.buildTree(root, 0)
        self.treeAssert(des, tree)
        
    def treeAssert(self, tree1:TreeNode, tree2:TreeNode):
        if not tree1 or not tree2:
            return 
        assert tree1.val == tree2.val
        self.treeAssert(tree1.left, tree2.left)
        self.treeAssert(tree1.right, tree2.right)




# pytest.main(['-v'])