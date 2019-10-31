#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = dummyHead = ListNode(0)
        lists = [node for node in lists if node]
        while len(lists) > 0:
            min_val = lists[0].val
            index = 0
            for i in range(len(lists)):
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    index = i

            curr.next = lists[index]
            curr = curr.next

            if lists[index].next is None:
                lists.pop(index)
            else:
                lists[index] = lists[index].next

        return dummyHead.next
# @lc code=end
