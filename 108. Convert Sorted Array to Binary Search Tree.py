import math as m
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        lg = m.floor(m.log2(n + 1))       
        rem = n - (2**lg - 1)             
        cnt = 0
        root = TreeNode()

        def build_tree(k: Optional[TreeNode], d: int):
            nonlocal rem, cnt
            if d < lg:
                k.left = TreeNode()
                build_tree(k.left, d + 1)

                k.val = nums[cnt]
                cnt += 1

                k.right = TreeNode()
                build_tree(k.right, d + 1)
                return

            if d == lg and rem > 0:
                rem -= 1
                k.left = TreeNode()
                build_tree(k.left, d + 1)

            k.val = nums[cnt]
            cnt += 1

            if d == lg and rem > 0:
                rem -= 1
                k.right = TreeNode()
                build_tree(k.right, d + 1)

        build_tree(root, 1)
        return root
