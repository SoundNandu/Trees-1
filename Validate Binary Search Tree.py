Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false


Solution 1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        print(root)
        maximum = float('inf')
        minimum = -float('inf')
        return self.__helper(root,maximum,minimum)
        
    def __helper(self,root: TreeNode,maximum : int ,minimum: int) -> bool:
        #base case
        
        if not root:
            return True
        
        #logic case
        if root.val >= maximum or root.val <= minimum:
            return False
        return self.__helper(root.left,root.val,minimum) and   self.__helper(root.right,maximum,root.val)
        
   space complexity O(1)
   time complexity O(n)

 Solution 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        prev = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True
