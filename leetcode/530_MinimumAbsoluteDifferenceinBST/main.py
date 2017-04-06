import myModule

root = myModule.TreeNode(5)
left = myModule.TreeNode(2)
right = myModule.TreeNode(8)
root.left = left
root.right = right

mySolution = myModule.Solution()
print(mySolution.getMinimumDifference(root))
