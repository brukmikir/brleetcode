class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        for i, t in enumerate(tickets):
            if i <= k:
                time += min(t, tickets[k])
            else:
                time += min(t, tickets[k] - 1)
        return time