class Solution:
    def corpFlightBookings(self, bookings, n):
        ans = [0] * n
        
        for l, r, seats in bookings:
            ans[l - 1] += seats
            if r < n:
                ans[r] -= seats
        
        for i in range(1, n):
            ans[i] += ans[i - 1]
        
        return ans