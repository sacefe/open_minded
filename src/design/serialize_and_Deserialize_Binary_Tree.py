'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a 
file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized
to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow 
this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

from typing import List, Optional

class TreeNode:
    def __init__(self, val:int):
        self.left= None
        self.right= None
        self.val = val

class CreateTree:
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

    def printTree(self, root) -> None:
        ''' convert a list in a Treenode
        :type nums: TreeNode
        :rtype: None
        '''        
        if not root:
            print(None, end=" ")
            return
        print(root.val, end=" ")
        self.printTree(root.left)
        self.printTree(root.right)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """    
        def recursiveSerialize(node:TreeNode, listNode:List[int]=[] ):
            if not node:
                listNode.append(None)
                return None
            listNode.append(node.val, )
            recursiveSerialize(node.left, listNode) 
            recursiveSerialize(node.right, listNode)
            return listNode
        
        listNode= []
        recursiveSerialize(root, listNode)
        serializedTree= ' '.join(str(i) if i !=None else 'None' for i in listNode)
        return serializedTree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """   
        def recursiveDeserialize(listNodes:List[int]) -> Optional[TreeNode]:
            ''' convert a list in a Treenode
            :type nums: List,  index: integer
            :rtype: TreeNode
            '''
            if listNodes[0] == None:
                listNodes.pop(0)
                return None
            root= TreeNode(listNodes[0])
            listNodes.pop(0)
            root.left= recursiveDeserialize(listNodes)
            root.right= recursiveDeserialize(listNodes)
            return root
    
        nodeList= [int(x) if x !='None' else None for x in data.split(' ')]
        root= recursiveDeserialize(nodeList)
        return root
    
if __name__ == '__main__':
    createTree= CreateTree()
    l= [1,2,3,None,None,4,5]
    print('org list ', l)
    tree= createTree.buildTree(l, 0)
    print("Tree map Graph: ",  end=' ')
    createTree.printTree(tree)
    print ()

    obCodec= Codec()
    ser= obCodec.serialize(tree)
    print("serialized: ", ser)

    tree= obCodec.deserialize(ser)
    print("deserialize: ", end=' ')
    createTree.printTree(tree)