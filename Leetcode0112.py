"""
112.路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明:叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        queue = collections.deque()

        queue.append((root, root.val))


        while queue:

            top, now_sum = queue.popleft()

            if not top.left and not top.right:
                if now_sum == sum:
                    return True
                continue

            if top.left:
                queue.append((root.left, now_sum + root.left.val))

            if top.right:
                queue.append((root.right, now_sum + root.right.val))

        return False






