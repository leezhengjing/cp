from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets_req = tickets[k]
        total = 0
        for i in range(0, k + 1):
            if tickets[i] <= tickets_req:
                total += tickets[i]
            else:
                total += tickets_req
        for j in range(k + 1, len(tickets)):
            if tickets[j] < tickets_req:
                total += tickets[j]
            else:
                total += tickets_req - 1
        return total