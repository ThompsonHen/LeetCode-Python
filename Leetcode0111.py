"""
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明:叶子节点是指没有子节点的节点。

示例:

给定二叉树[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1
class Solution1:
    def minDepth(self, root: TreeNode) -> int:


        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = collections.deque()

        queue.append([(root, 1)])

        while queue:

            top, depth = queue.popleft()

            if not top.left and not top.right:
                return depth
            if top.left:
                queue.append((root.left, depth + 1))

            if top.right:
                queue.append((root.right, depth + 1))

        return 0


















