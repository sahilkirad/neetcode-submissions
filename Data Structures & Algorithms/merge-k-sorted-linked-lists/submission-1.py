import heapq

class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(0)
        tail = dummy

        heap = []
        count = 0

        for e in lists:
            if e:
                heapq.heappush(heap, (e.val, count, e))
                count += 1

        while heap:
            val, _, smallest = heapq.heappop(heap)

            tail.next = smallest
            tail = tail.next

            if smallest.next:
                heapq.heappush(
                    heap,
                    (smallest.next.val, count, smallest.next)
                )
                count += 1

        return dummy.next