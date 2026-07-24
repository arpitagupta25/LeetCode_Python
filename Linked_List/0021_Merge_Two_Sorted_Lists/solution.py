
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        dummy = ListNode(0)
        list3 = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next

            list3 = list3.next

        if list1:
            list3.next = list1
        else:
            list3.next = list2

        return dummy.next

                


        
