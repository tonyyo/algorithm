class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: rootPos], postorder[: rootPos])
        root.right = self.buildTree(inorder[rootPos + 1:], postorder[rootPos: -1])
        return root

def printTree(root):
    res = []
    if root is None:
        print(res)
    queue = []
    queue.append(root)
    while len(queue) != 0:
        tmp = []
        length = len(queue)
        for i in range(length):
            r = queue.pop(0)
            if r.left is not None:
                queue.append(r.left)
            if r.right is not None:
                queue.append(r.right)
            tmp.append(r.val)
        res.append(tmp)
    print(res)


if __name__ == '__main__':
    inorder = [1, 2, 3]
    postorder = [1, 3, 2]
    print("中序遍历为：", inorder)
    print("后序遍历为：", postorder)
    solution = Solution()
    root = solution.buildTree2(inorder, postorder)
    print("构造的二叉树为：")
    printTree(root)
